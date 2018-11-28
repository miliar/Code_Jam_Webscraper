#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <cstdlib>
#include <utility>

using namespace std;

int main() {
  int T; cin >> T;
  for(int tt = 1; tt <= T; tt++) {
    cout << "Case #" << tt << ": ";

    int N;
    long long P;
    cin >> N >> P;


    long long r2 = 0;
    for(int i = 1; i <= 63 - __builtin_clzll(P); i++) {
      r2 |= 1LL << (N - i);
    }

    long long r1 = 0;
    long long PR = (1LL << N) - P;
    for(int i = 1; i <= 63 - __builtin_clzll(PR); i++) {
      r1 |= 1LL << (N - i);
    }
    r1 = (1LL << N) - r1 - 2;

    if(P == 1LL << N) {
      r1 = (1LL << N) - 1;
    }

    cout << r1 << ' ' << r2 << endl;
  }
  return 0;
}
