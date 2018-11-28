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

template <typename S, typename T> ostream &operator<<(ostream &out, const pair<S, T> &p) {
  out << "(" << p.first << ", " << p.second << ")";
  return out;
}

template <typename T> ostream &operator<<(ostream &out, const vector<T> &v) {
  out << "[";
  REP(i, v.size()){
    if (i > 0) out << ", ";
    out << v[i];
  }
  out << "]";
  return out;
}

typedef long long ll;

const ll inf = 1e15;
const ll mod = 1000 * 1000 * 1000 + 7;
const double eps = 1e-9;

class BipartiteMatching{
  int V;
  int W;
  vector<int> match;
  vector<int> level;
  vector<vector<int> > graph;
  
  int bfs(){
    fill(level.begin(), level.end(), -1);
    queue<int> que;
    for(int v = 0; v < V; v++){
      if(match[v] == -1){
        que.push(v);
        level[v] = 0;
      }
    }
    bool done = true;
    while(!que.empty()){
      int v = que.front(); que.pop();
      for(size_t i = 0; i < graph[v].size(); i++){
        int w = graph[v][i], nextv = match[w];
        if(nextv == -1){
          done = false;
        }else if(level[nextv] == -1){
          level[nextv] = level[v] + 1;
          que.push(nextv);
        }
      }
    }
    return !done;
  }
  
  bool dfs(int v){
    for(size_t i = 0; i < graph[v].size(); i++){
      int w = graph[v][i], nextv = match[w];
      if(nextv == -1 || (level[nextv] == level[v] + 1 && dfs(nextv))){
        match[v] = w;
        match[w] = v;
        return true;
      }
    }
    level[v] = -2;
    return false;
  }

public:
  BipartiteMatching(int _V, int _W) :
    V(_V), W(_W),
    match(vector<int>(V + W, -1)),
    level(vector<int>(V)),
    graph(vector<vector<int> >(V)){}
  
  void add_edge(int from, int to){
    assert(0 <= from && from < V && 0 <= to && to < W);
    graph[from].push_back(V + to);
  }
  
  int solve(){
    int ans = 0;
    while(bfs()){
      for(int v = 0; v < V; v++){
        if(match[v] == -1 && dfs(v)) ans++;
      }
    }
    return ans;
  }
};

bool ok(const vector<string> &B){
  REP(i, B.size()){
    BipartiteMatching bm(B.size(), B.size());
    REP(j, B.size()) if (j != i){
      REP(k, B.size()) if (B[j][k] == '1' && B[i][k] == '1'){
        bm.add_edge(j, k);
      }
    }
    int c = count(ALL(B[i]), '1');
    if (bm.solve() == c) return false;
  }
  return true;
}

void solve(){
  int N;
  cin >> N;
  vector<string> B(N);
  REP(i, N) cin >> B[i];

  int score = N * N;
  REP(mask, 1 << (N * N)){
    vector<string> B2 = B;
    int count = 0;
    REP(i, N) REP(j, N){
      if (B[i][j] == '0' && (mask & (1 << (i * N + j)))){
        B2[i][j] = '1';
        count++;
      }
    }
    if (ok(B2) && count < score){
      score = count;
    }
    
  }
  cout << score << endl;
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
