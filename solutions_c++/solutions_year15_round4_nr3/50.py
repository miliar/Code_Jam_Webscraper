#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>
#include <list>
#include <stack>
#include <valarray>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef unsigned long long UInt;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }
double fin() { double x; scanf("%lf", &x); return x; }
Int lin() { Int x; scanf("%lld", &x); return x; }

vector<int> S[256];
int E[4096], F[4096];

void solve() {
  memset(E, 0, sizeof(E));
  memset(F, 0, sizeof(F));
  map<string, int> W;
  int N = in();

  for (int i = 0; i < N; ++i) {
    string line, word;
    cin >> ws;
    getline(cin, line);
    stringstream ss;
    ss << line;
    
    vector<int> ws;
    while (ss >> word) {
      if (W.count(word)) {
        ws.push_back(W[word]);
      } else {
        int wid = W.size();
        W[word] = wid;
        ws.push_back(W[word]);
      }
    }
    S[i] = ws;

    if (i <= 1) {
      for (const int w : S[i]) {
        if (i == 0) E[w] = 1;
        if (i == 1) F[w] = 1;
      }
    }
  }

  int C = W.size();
  int res = INF;
  for (int i = 0; i < (1 << (N - 2)); ++i) {
    for (int j = 2; j < N; ++j) {
      int ef = (i >> (j - 2)) & 1;
      for (const int w : S[j]) {
        if (ef == 0) ++E[w];
        else         ++F[w];
      }
    }
    int cnt = 0;
    for (int k = 0; k < C; ++k) {
      if (E[k] && F[k]) ++cnt;
    }
    chmin(res, cnt);
    for (int j = 2; j < N; ++j) {
      int ef = (i >> (j - 2)) & 1;
      for (const int w : S[j]) {
        if (ef == 0) --E[w];
        else         --F[w];
      }
    }
  }

  printf("%d\n", res);
}

int main() {
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
