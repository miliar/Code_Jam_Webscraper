/* Written by Filip Hlasek 2016 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

int N;

long long gen_coin() {
  long long coin = 1;
  REP(i, N - 2) coin = 2 * coin + rand() % 2;
  return 2 * coin + 1;
}

set<long long> jamcoins;

bool is_jamcoin(long long coin) {
  if (jamcoins.count(coin)) return false;
  vector<int> d;
  FOR(base, 2, 10) {
    bool prime = true;
    for (int p = 2; p < 100; ++p) {
      long long number = 0;
      long long m = 1;
      REP(i, N) {
        if (coin & (1LL << i)) number = (number + m) % p;
        m = (m * base) % p;
      }
      if (number == 0) {
        prime = false;
        d.push_back(p);
        break;
      }
    }
    if (prime) return false;
  }
  jamcoins.insert(coin);
  FORD(i, N - 1, 0) {
    if (coin & (1LL << i)) printf("1");
    else printf("0");
  }
  REP(i, d.size()) printf(" %d", d[i]);
  printf("\n");
  return true;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  while (T--) {
    printf("Case #1:\n");
    int J;
    scanf("%d%d", &N, &J);
    while (J) {
      if (is_jamcoin(gen_coin())) J--;
    }
  }
  return 0;
}
