#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef vector<P> Vp;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<string> Vs;

const int INF = 1000000000;

int N, M;
Vs V;
Mi arr;

int maxim;
int quants;

int fun() {
  int res = 0;
  for (int i = 0; i < N; ++i) {
    set<string> st;
    for (int j = 0; j < int(arr[i].size()); ++j) {
      const string& s = V[arr[i][j]];
      for (int k = 0; k <= int(s.size()); ++k) {
        st.insert(s.substr(0, k));
      }
    }
    res += st.size();
  }
  return res;
}

void bt(int p) {
  if (p == M) {
    int t = fun();
    if (t > maxim) {
      maxim = t;
      quants = 1;
    }
    else if (t == maxim) {
      ++quants;
    }
    return;
  }
  
  for (int i = 0; i < N; ++i) {
    arr[i].push_back(p);
    bt(p + 1);
    arr[i].pop_back();
  }
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> M >> N;
    V = Vs(M);
    for (int i = 0; i < M; ++i) cin >> V[i];
    
    maxim = 0;
    quants = 0;
    arr = Mi(N);
    bt(0);
    
    cout << "Case #" << cas << ": " << maxim << " " << quants << endl;
  }
}
