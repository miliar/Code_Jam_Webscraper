#include <cstdio>
#include <cstring>
const double eps = 1e-6;

double C, F, X, ans;
int t;

double calc(int k)
{
  double v = 2, t = 0;
  for (int i = 1; i <= k; ++i) {
    t += C / v;
    v += F;
  }
  t += X / v;
  if (ans - t > eps) ans = t;
  return t;
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);
  for (int cases = 1; cases <= t; ++cases) {
    scanf("%lf%lf%lf", &C, &F, &X);
    ans = X / 2;
    int l = 0, r = 1000000;
    for (int lr, rl; l + 2 < r; ) {
      int step = (r - l + 1) / 3;
      double ansl = calc(lr = l + step);
      double ansr = calc(rl = r - step);
      if (ansl - ansr > eps)
	l = lr;
      else
	r = rl;
    }
    for (int i = l; i <= r; ++i)
      calc(i);
    printf("Case #%d: ", cases);
    printf("%.7lf", ans);
    if (cases < t) printf("\n");
  }
  return 0;
}
