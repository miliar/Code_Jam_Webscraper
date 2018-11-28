#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <climits>
#include <sstream>
#include <cstring>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <map>
#include <set>

#define INF (INT_MAX/2)
#define INFLL (1000000000000000000LL)

typedef long long lint;

using namespace std;

bool possible(vector<int> &x, lint maxs) {
  int many = 0;
  lint s = 0;
  for (int i = 0; i < (int)x.size(); i++) {
    if (s + x[i] <= maxs) {
      s += x[i];
    } else {
      many++;
      s = 0;
      if (s + x[i] <= maxs) {
	s += x[i];
      } else
	return false;
    }
  }
  if (s > 0) many++;
  return many <= 3;
}

int main(int argc, char ** argv)
{
  int ntest;

  scanf("%d", &ntest);

  for (int t = 0; t < ntest; t++) {
    int n, p, q, r2, s;

    scanf("%d %d %d %d %d", &n, &p, &q, &r2, &s);

    vector<int> x(n);
    for (int i = 0; i < n; i++) x[i] = (((lint)i * p + q) % r2 + s);

    lint sum = 0;
    for (int i = 0; i < n; i++) sum += x[i];

    lint l = 1, r = sum;

    while (l < r) {
      lint m = l + (r-l)/2LL;
      if (possible(x, m)) r = m;
      else l = m+1;
    }

    double result = 1.0 - 1.0 * l / sum;

    printf("Case #%d: %.10f\n", t+1, result);
  }

  return 0;
}
