#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
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

string random_string(int v, string S, const vector<vector<int> > &G){
  if (G[v].empty()){
    return string(1, S[v]);
  } else {
    int sum = 0;
    vector<string> words;
    vector<int> order;
    vector<int> pos(G[v].size());
    
    REP(i, G[v].size()){
      int w = G[v][i];
      words.push_back(random_string(w, S, G));
      sum += words.back().size();
      REP(j, words.back().size()){
        order.push_back(i);
      }
    }
    std::random_device rd;
    std::mt19937 mt(rd());
    std::shuffle(order.begin(), order.end(), mt);
    string res(order.size(), 0);
    assert(res.size() == order.size());
    REP(i, res.size()){
      int idx = order[i];
      res[i] = words[idx][pos[idx]++];
    }
    if (v != 0) res = S[v] + res;
    return res;
  }
}

void solve(){
  int N, M;
  cin >> N;
  vector<vector<int> > G(N + 1);
  string S;
  vector<string> W;
  
  REP(i, N){
    int par;
    cin >> par;
    G[par].push_back(i + 1);
  }

  cin >> S;
  S = " " + S;
  
  cin >> M;
  REP(i, M){
    string s;
    cin >> s;
    W.push_back(s);
  }

  const int num_trial = 5000;
  vector<double> score(M, 0);
  REP(i, num_trial){
    string sr = random_string(0, S, G);
    // cout << sr << endl;
    REP(j, M){
      if (sr.find(W[j]) != string::npos){
        score[j] += 1;
      }
    }
  }
  REP(i, M){
    cout << " " << score[i] / num_trial;
  }
  cout << endl;
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
