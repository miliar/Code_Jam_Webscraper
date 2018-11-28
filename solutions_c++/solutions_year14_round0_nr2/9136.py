#include <cstdio>

int T;
double c, f, x;
double buy[1000005], speed[1000005];

double buyTimes(int n) {
	return buy[n] + x / speed[n];
}

double min(const double& a, const double& b) {
  if (a < b)
    return a;
  return b;
}

void init() {
	buy[0] = 0.0;
	speed[0] = 2.0;
	for (int i = 1; i <= 1000000; ++i) {
    buy[i] = buy[i - 1] + c / speed[i - 1];
	  speed[i] = speed[i - 1] + f;
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++Case) {
	  scanf("%lf %lf %lf", &c, &f, &x);
	  init();
	  int bot = 0, top = 1000000;
	  while (true) {
		  int mid1 = (2 * bot + top) / 3;
		  int mid2 = (2 * top + bot) / 3;
		  if (mid1 == mid2)
		    break;
		  if (buyTimes(mid1) < buyTimes(mid2))
		    top = mid2 - 1;
		  else
		    bot = mid1 + 1;
		}
	  printf("Case #%d: %.7lf\n", Case, min(buyTimes(bot), buyTimes(top)));
	}
}
