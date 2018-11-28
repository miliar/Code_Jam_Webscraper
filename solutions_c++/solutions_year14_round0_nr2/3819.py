#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <list>
#include <iostream>
#include <cmath>
#define eps 1e-7
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;

double getTimeTo(double rate, double X) {
  return X / rate;
}

int main()
{
  freopen("B-large.in","r",stdin);
  freopen("B-saida-large.out","w",stdout);
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    double C,F,X;
    scanf("%lf %lf %lf", &C, &F, &X);
    double min_time = getTimeTo(2.0, X);
    double now_time = 0.0;
    double rate = 2.0;
    int ct = 0;
    while (ct++ < 100010) {
      double ans_now = now_time + getTimeTo(rate, X);
      min_time = min(min_time, ans_now);
      now_time += getTimeTo(rate, C);
      rate += F;
    }
    printf("Case #%d: %.7lf\n",t, min_time);
  }
  return 0;
}
