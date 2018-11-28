#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


map < int, double > cost;

double getCost(int n, double C, double F) {
  if (n == 0) {
    cost[0] = .0;
    return .0;
  }
  double res = cost[n - 1] + C / (F * (n - 1) + 2);
  return cost[n] = res;
}

void doit() {
  double C, F, X;
  double res = .0;


  scanf("%lf %lf %lf", &C, &F, &X);

  res = X / 2;

  for (int c = 0, cMax = (int)(X / C) + 1; c <= cMax; c += 1) {
    double tmp = getCost(c, C, F);
    tmp += X / (2 + c * F);
    if (tmp < res) {
      res = tmp;
    }
  }

  printf("%.7lf", res);
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T;
  scanf("%d\n", &T);
  for (int tc = 0; tc < T; tc += 1) {
    printf("Case #%d: ", tc + 1);
    doit();
    printf("\n");
  }

  return 0;
}
