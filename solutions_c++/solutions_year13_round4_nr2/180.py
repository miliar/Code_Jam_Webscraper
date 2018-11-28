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
using namespace std;

int T,n;
long long p;

long long sub1() {
  if (p == 1LL << n) return (1LL << n) - 1;
  long long last = 0;
  long long segment = 1LL << n,sum = 0;
  while (1) {
    segment /= 2;
    if (!segment) break;
    sum += segment;
    last = last * 2 + 1;
    if (p <= sum) return last - 1;
  }
}

long long sub2() {
  if (p == 1LL << n) return (1LL << n) - 1;
  long long ans = 0;
  for (int i = n; i > 0; i--)
    if (p >= (1LL << n)/(1LL << i)) ans = (1LL << n) - (1LL << i);
  return ans;
}

void solveCase(int it) {
  cin >> n >> p;
  printf("Case #%d: %lld %lld\n", it, sub1(), sub2());
}

int main() {
  scanf("%d", &T);
  for (int it = 1; it <= T; it++) solveCase(it);
}
