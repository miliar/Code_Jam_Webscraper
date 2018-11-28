#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stdexcept>

using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;

typedef long long i64;
typedef unsigned long long u64;

int N, K;
double P[200];

int bits(int a) {
  return !a ? 0 : bits(a>>1) + (a&1);
}


double G[203][203];

double calc(int s) {
  memset(G, 0, sizeof(G));
  G[0][K/2 + 1] = 1;

  int k = 0;
  REP(i, N) if (s & (1<<i)) {
    k++;
    for (int j = -k; j <= k; j++) {
      int p = j + K / 2 + 1;
      G[k][p] = G[k-1][p+1] * (1 - P[i]) + G[k-1][p-1] * P[i];
    }
  }
  return G[K][K/2 + 1];
}

void go() {
  double best = 0;
  REP(i, 1<<N) if (bits(i) == K) {
    double temp = calc(i);
    if (temp > best) {
      best = temp;
    }
  }
  cout << best;
}

int main() {
  int T;
  cin>>T;
  for (int t = 1; t <= T; t++) {
    cin >> N >> K;
    REP(i, N) cin >> P[i];
    cout << "Case #" << t << ": ";
    go();
    cout << endl;
  }
  return 0;
}
