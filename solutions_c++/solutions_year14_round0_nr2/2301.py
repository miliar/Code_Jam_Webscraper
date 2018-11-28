#include"stdio.h"
#include"stdlib.h"
#include"math.h"
using namespace std;

int T, t;
double c, f, x, ans, rate, buyFarm, notBuy;
int main() {
	freopen("2.in", "r", stdin);
	freopen("2.txt", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		ans = 0;
		rate = 2;
		scanf("%lf%lf%lf", &c, &f, &x);
		if (c >= x) {
			
		}
		while (true) {
			notBuy = (x / rate);
			buyFarm = (c / rate) + (x / (rate + f));
			if (notBuy < buyFarm) break;
			ans += (c / rate);
			rate += f;
		}
		ans += notBuy;
		printf("Case #%d: %.7lf\n", t, ans);
	}
}
