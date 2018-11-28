#include <bits/stdc++.h>

using namespace std;

const int INF = 200000;

struct Edge {
  int from, to, cap, flow, index;
  Edge(int from, int to, int cap, int flow, int index) :
    from(from), to(to), cap(cap), flow(flow), index(index) {}
};

struct Dinic {
  int N;
  vector<vector<Edge> > G;
  vector<Edge *> dad;
  vector<int> Q;
  
  Dinic(int N) : N(N), G(N), dad(N), Q(N) {}
  
  void AddEdge(int from, int to, int cap) {
    G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
    if (from == to) G[from].back().index++;
    G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
  }

  long long BlockingFlow(int s, int t) {
    fill(dad.begin(), dad.end(), (Edge *) NULL);
    dad[s] = &G[0][0] - 1;
    
    int head = 0, tail = 0;
    Q[tail++] = s;
    while (head < tail) {
      int x = Q[head++];
      for (int i = 0; i < G[x].size(); i++) {
	Edge &e = G[x][i];
	if (!dad[e.to] && e.cap - e.flow > 0) {
	  dad[e.to] = &G[x][i];
	  Q[tail++] = e.to;
	}
      }
    }
    if (!dad[t]) return 0;

    long long totflow = 0;
    for (int i = 0; i < G[t].size(); i++) {
      Edge *start = &G[G[t][i].to][G[t][i].index];
      int amt = INF;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
	if (!e) { amt = 0; break; }
	amt = min(amt, e->cap - e->flow);
      }
      if (amt == 0) continue;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
	e->flow += amt;
	G[e->to][e->index].flow -= amt;
      }
      totflow += amt;
    }
    return totflow;
  }

  long long GetMaxFlow(int s, int t) {
    long long totflow = 0;
    while (long long flow = BlockingFlow(s, t))
      totflow += flow;
    return totflow;
  }
};

vector<int> vec[1<<20];

void main2(){
	int n; cin >> n;
	for (int i=0; i<n; i++)
		vec[i].clear();
	string s; getline(cin, s);
	map<string, vector<int> > mp;
	for (int i=0; i<n; i++){
		getline(cin, s);
		stringstream inp; inp << s;
		string t; 
		while (inp >> t)
			mp[t].push_back(i);
	}
	Dinic ans(2*(int)mp.size()+2);
	int index = 0;
	int res = 0;
	int source = 2*(int)mp.size();
	int sink = 2*(int)mp.size()+1;
	for (map< string,vector<int> > :: iterator it = mp.begin(); it != mp.end(); it++, index++){
		vector<int> q = it->second;
		sort(q.begin(), q.end());
		q.resize(unique(q.begin(), q.end())-q.begin());
		if (q.size()>1 && q[0]==0 && q[1]==1){
			res++;
			continue;
		}
		int E = 2*index; 
		int F = 2*index+1;
		ans.AddEdge(F,E,INF);
		ans.AddEdge(E,F,1);
		if (q[0]==0)
			ans.AddEdge(source, E, INF);
		if (q[0]==1) 
			ans.AddEdge(F, sink, INF);
		for (int i=0; i<(int)q.size(); i++)
			vec[q[i]].push_back(index);
	}
	for (int i=0; i<n; i++){
		for (int j=0; j<(int)vec[i].size(); j++)
			for (int k=j+1; k<(int)vec[i].size(); k++){
				int x = vec[i][j];
				int y = vec[i][k];
				ans.AddEdge(2*x+1, 2*y, INF);
				ans.AddEdge(2*y+1, 2*x, INF); 
			}
	}
	cout << res + ans.GetMaxFlow(source, sink) << endl;
}

int main(){
	int tt; cin >> tt;
	for (int o=1; o<=tt; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
