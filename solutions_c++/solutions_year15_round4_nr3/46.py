#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <sstream>
#include <algorithm>

using namespace std;

#define foreach(e,x) for(__typeof((x).begin()) e=(x).begin(); e!=(x).end(); ++e)

const int N = 200 + 10;
const int INF = N * N + 10;

struct MaxFlow //最大流类，包括了建图和最大流，只可整数流使用
{
	struct Edge { //边类
		Edge *nextEdge; //邻接表的下一条边
		Edge *reverseEdge; //邻接表的反边
		long long capacity; //可行流量
		int toID; //邻接表的指向点的ID
		Edge() {}
		Edge(Edge *nextEdge, long long capacity, int toID) //构造函数
			: nextEdge(nextEdge), capacity(capacity), toID(toID) {
			}
	};

	int vertexCount; //点数
	int source; //源
	int destination; //汇
	long long infinite; //最大可能流量
	vector<Edge*> firstEdge; //邻接表的初始弧

	MaxFlow() {}
	~MaxFlow() { //析构函数
		for(int i = 0; i < vertexCount; ++ i) {
			for( ; firstEdge[i]; ) {
				Edge *edge = firstEdge[i];
				firstEdge[i] = edge->nextEdge;
				delete edge;
			}
		}
	}

	Edge* makeEdge(int from, int to, long long capacity) { //加边函数
		Edge *edge = new Edge(firstEdge[from], capacity, to);
		firstEdge[from] = edge;
		return edge;
	}

	void addEdge(int from, int to, long long capacity) { //加边函数
		Edge *edgeFromTo = makeEdge(from, to, capacity);
		Edge *edgeToFrom = makeEdge(to, from, 0);
		edgeFromTo->reverseEdge = edgeToFrom;
		edgeToFrom->reverseEdge = edgeFromTo;
	}

	//建图函数，参数分别为点数，源，汇，边集
	void createGraph(int vertexCount, int source, int destination, vector<int> from, vector<int> to, vector<long long> capacity) {
		this->vertexCount = vertexCount;
		this->source = source;
		this->destination = destination;
		firstEdge.resize(vertexCount);
		fill(firstEdge.begin(), firstEdge.end(), (Edge*)NULL);
		infinite = 0;
		for(int i = 0; i < (int)to.size(); ++ i) {
			addEdge(from[i], to[i], capacity[i]);
			infinite = max(infinite, capacity[i]);
		}
	}

	int iSAP() { //iSAP算法求最大流，具体算法请自行百度
		int *countLabel = new int[vertexCount + 1]; //标号计数
		int *label = new int[vertexCount]; //距离标号
		long long *aug = new long long[vertexCount]; //可增广量
		vector<Edge*> currentEdge(firstEdge); //当前弧
		vector<Edge*> previousEdge(vertexCount); //记录增广路径的边
		queue<int> bfsQueue; //bfs使用的队列

		fill(countLabel, countLabel + vertexCount + 1, 0);
		fill(label, label + vertexCount, vertexCount);
		label[destination] = 0;
		bfsQueue.push(destination);

		for( ; ! bfsQueue.empty(); ) { //bfs过程
			int u = bfsQueue.front();
			bfsQueue.pop();
			++ countLabel[label[u]];
			for(Edge *edge = firstEdge[u]; edge; edge = edge->nextEdge)
				if (edge->reverseEdge->capacity && label[edge->toID] == vertexCount) {
					label[edge->toID] = label[u] + 1;
					bfsQueue.push(edge->toID);
				}
		}

		long long flow = 0; //记录流量
		int currentNode = source; //当前需要增广的节点
		aug[source] = infinite;
		for( ; label[source] < vertexCount; ) {
			Edge* edge;
			for(edge = currentEdge[currentNode]; edge; edge = edge->nextEdge)
				if (edge->capacity && label[edge->toID] + 1 == label[currentNode])
					break;
			if (edge) {
				int nextNode = edge->toID;
				currentEdge[currentNode] = previousEdge[nextNode] = edge;
				aug[nextNode] = min(aug[currentNode], edge->capacity);
				if ((currentNode = nextNode) == destination) { //如果发现一条增广路，增广
					long long by = aug[destination];
					for( ; currentNode != source; ) {
						edge = previousEdge[currentNode];
						edge->capacity -= by;
						edge->reverseEdge->capacity += by;
						currentNode = edge->reverseEdge->toID;
					}
					flow += by;
				}
			} else { //否则进行重标号
				if (!--countLabel[label[currentNode]]) return flow;
				label[currentNode] = vertexCount;
				for(edge = firstEdge[currentNode]; edge; edge = edge->nextEdge)
					if (edge->capacity && label[currentNode] > label[edge->toID] + 1)
						label[currentNode] = label[edge->toID] + 1, currentEdge[currentNode] = edge;
				++countLabel[label[currentNode]];
				if (currentNode != source)
					currentNode = previousEdge[currentNode]->reverseEdge->toID;
			}
		}

		return flow;
	}
};

int n, m;
vector<string> a[N];
map<string, int> tid;

void solve()
{
	cin >> n;
	string buf;
	getline(cin, buf);
	tid.clear();
	m = 0;
	for(int i = 0; i < n; ++ i) {
		a[i].clear();
		getline(cin, buf);
		stringstream ss(buf);
		for( ; ss >> buf; ) {
			a[i].push_back(buf);
			if (tid.count(buf) == 0) {
				tid[buf] = m ++;
			}
		}
	}

	MaxFlow *maxflow = new MaxFlow();
	int cnt = 2 * m + n;
	int s = cnt ++;
	int t = cnt ++;
	vector<int> from, to;
	vector<long long> c;
	for(int i = 0; i < m; ++ i) {
		from.push_back(s); to.push_back(i); c.push_back(0);
		from.push_back(i); to.push_back(i + m); c.push_back(1);
		from.push_back(i + m); to.push_back(t); c.push_back(0);
	}
	for(int i = 0; i < n; ++ i) {
		from.push_back(s); to.push_back(2 * m + i); c.push_back(i == 0 ? 0 : INF);
		from.push_back(2 * m + i); to.push_back(t); c.push_back(i == 1 ? 0 : INF);
		for(int j = 0; j < a[i].size(); ++ j) {
			int w = tid[a[i][j]];
			from.push_back(2 * m + i); to.push_back(w); c.push_back(INF);
			from.push_back(w + m); to.push_back(2 * m + i); c.push_back(INF);
		}
	}
	//cout << m << endl;
	for(int i = 0; i < from.size(); ++ i) {
		//cout << from[i] << ' ' << to[i] << ' ' << c[i] << endl;
	}
	maxflow->createGraph(cnt, s, t, from, to, c);
	cout << maxflow->iSAP() - (n - 2) * INF << endl;
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		cerr << i << endl;
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
