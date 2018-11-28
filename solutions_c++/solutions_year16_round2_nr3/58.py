#include<bits/stdc++.h>
using namespace std;


const int MAX_V = 5010;
int V = 5010;
vector<int> G[MAX_V];
int match[MAX_V];
bool used[MAX_V];

void add_edge(int u , int v) {
  G[u].push_back(v);
  G[v].push_back(u);
}
bool dfs(int v) {
  used[v] = true;
  for(int i=0; i<G[v].size(); i++) {
    int u = G[v][i] , w  =match[u];
    if(w<0 || !used[w] && dfs(w)) {
      match[v] = u;
      match[u] = v;
      return true;
    }
  }
  return false;
}

int bipartite_matching() {
  int res = 0;
  //  memset(match , -1,  sizeof(match));
  for(int i=0; i<MAX_V; i++) match[i] = -1;
  for(int v=0; v<V; v++) {
    if(match[v]<0) {
      for(int i=0; i<MAX_V; i++) used[i] = false; 
      //      memest(used,0,sizeof(used));
      if(dfs(v)) res++;
    }
  }
  return res;
}
/*

Vに必ずなにか入れましょう
ICPC形式だと、必ずG[i]をすべて初期化するようにしましょう


ここまでコピペしましょう
*/





int  solve() {
	int N;
	cin >> N;
	
	for(int i=0; i<MAX_V; i++)
		G[i].clear();
	map<string, int> first, second;
	int iter = 0;
	for(int i=0; i<N; i++) {
		string s,t;
		cin >> s >> t;
		if( first.find(s) == first.end() ) {
			first[s] = iter;
			iter++;
		}
		if( second.find(t) == second.end()) {
			second[t] = iter;
			iter++;
		}
		add_edge(first[s], second[t]);
	}
	return N - (iter - bipartite_matching());
	
}

int main() {
	int N;
	cin >> N;
	for(int i=0; i<N;i ++) {
		
		int ans = solve();
		cout << "Case #" << i+1 << ": " << ans << endl;
		
	}
	
	return 0;
	
}

