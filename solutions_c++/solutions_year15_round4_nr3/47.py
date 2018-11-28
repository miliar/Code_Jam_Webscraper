#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<functional>
#include<map>

using namespace std;

typedef long long ll;
typedef pair<double,double> pdd;

const int MX = 105;

#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

typedef long long int64;
typedef pair<int, int> pii;

struct edge {
	int u, v, flow, cap;
	edge() {}
	edge(int u, int v, int flow, int cap): u(u), v(v), flow(flow), cap(cap) {}
	inline int residual() {
		return cap - flow;
	}
};

struct Dinic {
	vector<edge> edges; 
	vector<vector<int> > graph;
	vector<int> dist, vst, ptr;
	int n, m;
	static const int FLOW_INF = 1000000000; // 10^9
	Dinic() {}
	Dinic(int vertices) {
		clear();
		n = vertices;
		graph.assign(n, vector<int>());
	}
	void clear() {
		n = m = 0;
		edges.clear(), graph.clear(), dist.clear(), vst.clear();
	}
	void addEdge(int u, int v, int cap) {
		edges.push_back(edge(u, v, 0, cap	));
		graph[u].push_back(m++);
		edges.push_back(edge(v, u, 0, 0	));
		graph[v].push_back(m++);
	}
	bool NotMaxFlow(int start, int dest) {
		queue<pii> q;
		while (!q.empty())
			q.pop();
		dist.clear(), vst.clear();
		dist.resize(n), vst.resize(n);
		for (int i = 0; i < n; i++)
			dist[i] = n, vst[i] = false;
		q.push(pii(start, 0));
		while (!q.empty()) {
			pii cur = q.front();
			int u = cur.first, d = cur.second;
			q.pop();
			if (vst[u]) continue;
			vst[u] = true;
			dist[u] = d;
			for (int ed = 0; ed < (int)graph[u].size(); ed++) {
				int edgeNum = graph[u][ed];
				edge &e = edges[edgeNum];
				if (vst[e.v] || e.residual() <= 0)
					continue;
				q.push(pii(e.v, d+1));
			}
		}
		return dist[dest] < n;
	}
	int BlockingFlow(int u, int dest, int deltaFlow) {
		if (u == dest) return deltaFlow;
		for (int &ed = ptr[u]; ed < (int)graph[u].size(); ed++) {
			edge &e = edges[graph[u][ed]];
			edge &rev = edges[graph[u][ed]^1];
			if (dist[e.v] == dist[u] + 1 && e.residual() > 0) {
				int ret = BlockingFlow(e.v, dest, min(deltaFlow, e.residual()));
				if (ret == 0) continue;
				e.flow += ret;
				rev.flow -= ret;
				return ret;
			}
		}
		return 0;
	}
	int MaxFlow(int source, int sink) {
		int ans = 0;
		ptr.clear();
		ptr.resize(n);
		while (NotMaxFlow(source, sink)) {
			for (int i = 0; i < n; i++)
				ptr[i] = 0;
			while (int deltaFlow = BlockingFlow(source, sink, FLOW_INF))
				ans += deltaFlow;
		}
		return ans;
	}
}flow;

map<string, int> DB;
vector<int> word[205];

int main()
{
	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		int N, cnt = 0;

		DB.clear(); flow.clear();
		scanf("%d\n", &N);
		for(int i = 1; i <= N; i++){
			word[i].clear();
			char buf[10000] = "", *loc = buf;
			gets(buf);
			while(*loc != 0){
				char buf2[100];
				sscanf(loc, "%s", buf2);
				loc++;
				while(*loc != ' ' && *loc != 0 ) loc++;
				string w = buf2;
				if( DB.find(w) == DB.end() ) DB[w] = ++cnt;
				word[i].push_back(DB[w]);
			}
		}
		flow = Dinic(cnt*2+2);
		bool chk[10005][2] = {};
		for(int c : word[1]) chk[c][0] = true;
		for(int c : word[2]) chk[c][1] = true;
		for(int i = 1; i <= cnt; i++){
			if( chk[i][0] ) flow.addEdge(0, i, 100000);
			else flow.addEdge(0, i, 1);
			if( chk[i][1] ) flow.addEdge(i+cnt, cnt*2+1, 100000);
			else flow.addEdge(i+cnt, cnt*2+1, 1);
			flow.addEdge(i, i+cnt, 2);
		}
		for(int i = 1; i <= N; i++){
			for(int c : word[i]){
				for(int d : word[i]){
					flow.addEdge(c+cnt, d, 100000);
				}
			}
		}
		printf("%d\n", flow.MaxFlow(0, cnt*2+1) - cnt);
	}
	return 0;
}