#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <cstring>
#define mod 1000002013
#define maxm 1005
using namespace std;

long long getSum(int n,int d) {
  if (d == 0) return 0;
  return (1LL * d * (n * 2 - d + 1)/2) % mod;
}

int T,n,m;
pair<int,int> S[maxm],F[maxm];

void solveCase(int it) {
  scanf("%d %d", &n, &m);
  long long origCost = 0;
  for (int i = 0; i < m; i++) {
    int from, to, cnt;
    scanf("%d %d %d", &from, &to, &cnt);
    S[i] = make_pair(from,cnt);
    F[i] = make_pair(to,cnt);
    origCost += getSum(n,to - from) * cnt;
    origCost %= mod;
  }
  sort(S,S + m);
  sort(F,F + m);
  long long finalCost = 0;
  for (int i = m - 1; i >= 0; i--)
    for (int j = 0; j < m; j++) if (S[i].first <= F[j].first) {
      int cnt = min(S[i].second,F[j].second);
      finalCost += getSum(n,F[j].first - S[i].first) * cnt;
      finalCost %= mod;
      S[i].second -= cnt;
      F[j].second -= cnt;
    }
  long long delta = (origCost - finalCost + mod) % mod;
  printf("Case #%d: %lld\n", it, delta);
}

int main() {
  scanf("%d", &T);
  for (int it = 1; it <= T; it++) solveCase(it);
}
