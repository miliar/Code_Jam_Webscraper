#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define FOREACH(i, c) for(auto i = (c).begin(); i != (c).end(); ++i)
#define BIT(n, m) (((n) >> (m)) & 1)

typedef long long ll;

const ll inf = 1e15;
const ll mod = 1000 * 1000 * 1000 + 7;
const double eps = 1e-9;

#include <vector>
#include <queue>
#include <cstdlib>
#include <algorithm>
#include <climits>

class MaxFlow{
  typedef long long ll;
  
  struct edge{
    int to;
    ll cap;
    int rev;
    edge(){}
    edge(int to, ll cap, int rev) : to(to), cap(cap), rev(rev){}
  };
  
  std::vector<std::vector<edge> > G;
  std::vector<int> level;
  std::vector<int> iter;

  void bfs(int s){
    std::fill(level.begin(), level.end(), -1);
    std::queue<int> que;
    level[s] = 0;
    que.push(s);
    while(!que.empty()){
      int v = que.front(); que.pop();
      for(int i = 0; i < (int)G[v].size(); i++){
        edge &e = G[v][i];
        if(e.cap > 0 && level[e.to] < 0){
          level[e.to] = level[v] + 1;
          que.push(e.to);
        }
      }
    }
  }

    
  ll dfs(int v, int t, ll f){
    if(v == t) return f;
    
    for(int &i = iter[v]; i < (int)G[v].size(); i++){
      edge &e = G[v][i];
      if(e.cap > 0 && level[e.to] > level[v]){
        ll d = dfs(e.to, t, std::min(f, e.cap));
        if(d > 0){
          e.cap -= d;
          G[e.to][e.rev].cap += d;
          return d;
        }
      }
    }
    return 0;
  }
  
public:
  MaxFlow(int V) :
    G(std::vector<std::vector<edge> >(V)),
    level(std::vector<int>(V)),
    iter (std::vector<int>(V)) { }
  
  void add_edge(int from, int to, ll cap){
    G[from].push_back(edge(to, cap, G[to].size()));
    G[to].push_back(edge(from, 0, G[from].size() - 1));
  }

  ll solve(int s, int t){
    ll res = 0, f;
    for(;;){
      bfs(s);
      if(level[t] < 0) break;
      std::fill(iter.begin(), iter.end(), 0);
      while((f = dfs(s, t, LONG_LONG_MAX)) > 0) res += f;
    }
    return res;
  }
};



void solve(){
  
  int N;
  string S;
  cin >> N; getline(cin, S);
  vector<set<string> > words(N);
  map<string, int> dict;

  REP(i, N){
    getline(cin, S);
    string word;
    istringstream iss(S);
    while (iss >> word){
      words[i].insert(word);

      if (dict.count(word) == 0){
        int id = dict.size();
        dict[word] = id;
      }
    }
  }

  int M = dict.size();
  MaxFlow mf(N + M * 2);

  REP(i, M){
    mf.add_edge(i + N, i + M + N, 1);
    mf.add_edge(i + N + M, i + N, 1);
  }
  
  REP(i, N) REP(j, N) if (i != j){
    int count = 0;
    for (const auto &w : words[i]){
      if (words[j].count(w)){
        int id_en = N + dict[w];
        int id_fr = N + M + dict[w];
        mf.add_edge(i    , id_en, 1e9);
        mf.add_edge(id_fr, j    , 1e9);
      }
    }
  }
  cout << mf.solve(0, 1) << endl;
}
 
int main(){
  int T;
  cin >> T;
  REP(t, T){
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
