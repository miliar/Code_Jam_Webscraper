#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

bool check(long long n) {
  vector<int> v;
  for (; n; n /= 10) {
    v.push_back(n%10);
  }
  for (size_t i=0; i<v.size(); ++i) {
    if (v[i] != v[v.size()-i-1]) return false;
  }
  return true;
}

void findAll(long long n, vector<long long> &v) {
  for (long long i = 0; i*i <= n; ++i) {
    if (!check(i)) continue;
    if (check(i*i)) v.push_back(i*i);
  }
}

int main() {
  vector<long long> v;
  findAll(100000000000000LL, v);
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    long long a, b;
    scanf("%lld%lld", &a, &b);
    int r = 0;
    for (size_t i = 0; i < v.size(); ++i) {
      if (v[i] >= a && v[i] <= b) ++r;
    }
    printf("Case #%d: %d\n", tc, r);
  }
  return 0;
}
