#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

class MaxFlow
{
private:
	
	struct Edge
	{
		Edge(int s, int d, int cap, int res): source(s), dest(d), capacity(cap), residue(res) { }
		int source, dest, capacity, residue;
	};

	int N;
	vector<vector<int> > graph;
	vector<Edge> edges;

public:

	void Init(int n)
	{
		Clear();
		N = n;
		graph.resize(N);
	}

	void AddEdge(int source, int dest, int cap1, int cap2)
	{
		if (source >= N || dest >= N) { N = max(source,dest)+1; graph.resize(N); }
		graph[source].push_back(edges.size());
		graph[dest].push_back(edges.size()+1);
		edges.push_back(Edge(source, dest, cap1, cap1));
		edges.push_back(Edge(dest, source, cap2, cap2));
	}

	void Clear() { N = 0; graph.clear(); edges.clear(); }

	int Flow(int source, int dest)
	{
		int res = 0;

		vector<int> prev(N);
		while (1)
		{
			for (int i = 0; i < N; ++i)
				prev[i] = -1;
			prev[source] = -2;
			queue<int> manage;
			manage.push(source);

			while (!manage.empty() && prev[dest] == -1)
			{
				int node = manage.front();
				manage.pop();

				for (int i = 0; i < graph[node].size(); ++i)
					if (edges[graph[node][i]].residue > 0)
					{
						int next = edges[graph[node][i]].dest;
						if (prev[next] == -1)
						{
							prev[next] = graph[node][i];
							manage.push(next);
						}
					}
			}
			if (prev[dest] == -1) break;

			int fl = 2000000000;
			int node = dest;
			while (prev[node] != -2)
			{
				fl = min(fl, edges[prev[node]].residue);
				node = edges[prev[node]].source;
			}

			node = dest;
			while (prev[node] != -2)
			{
				edges[prev[node]].residue -= fl;
				edges[prev[node]^1].residue += fl;
				node = edges[prev[node]].source;
			}
			res += fl;
		}

		return res;
	}
};


const int MAX = 200;
int N;
map<string, int> w2i;
vector<int> words[MAX];

int get(string & word) {
	map<string, int>::iterator iter = w2i.find(word);
	if (iter != w2i.end())
		return iter->second;
	int index = w2i.size();
	return w2i[word] = index;
}

void read(vector<int> & words) {
	words.clear();
	string line;
	getline(cin, line);
	string word;
	istringstream is(line);
	while (is >> word) {
		words.push_back(get(word));
	}
	sort(words.begin(), words.end());
}

int common(vector<int> & v1, vector<int> & v2) {
	int res = 0, i1 = 0, i2 = 0;
	while (i1 < v1.size() && i2 < v2.size()) {
		if (v1[i1] == v2[i2]) {
			++res;
			++i1;
			++i2;
		} else if (v1[i1] < v2[i2])
			++i1;
		else
			++i2;
	}
	return res;
}

void Solve(int tc)
{
	w2i.clear();
	scanf("%d\n", &N);
	REP(i, N) read(words[i]);
	int M = w2i.size();

	MaxFlow mf;
	mf.Init(N+2*M);
	/*REP(i, N) REP(j, i) {
		int x = common(words[i], words[j]);
		mf.AddEdge(i, j, x, x);
	}*/
	REP(i, M) {
		mf.AddEdge(N+2*i, N+2*i+1, 1, 0);
	}
	REP(i, N) REP(j, words[i].size()) {
		mf.AddEdge(i, N+2*words[i][j], 1, 0);
		mf.AddEdge(N+2*words[i][j]+1, i, 1, 0);
	}
	printf("Case #%d: %d\n", tc, mf.Flow(0, 1));
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) {
		cerr << "Test case: " << tc << endl;
		Solve(tc);
	}

	return 0;
}