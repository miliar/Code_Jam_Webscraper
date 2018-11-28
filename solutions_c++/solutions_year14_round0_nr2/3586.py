#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;

int main(){
	freopen("bsmall.in", "r", stdin);
	freopen("bsmall.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tcase = 1; tcase <= t; ++tcase){
		printf("Case #%d: ", tcase);
		double c, f, x, production = 2, ans = 0;
		scanf("%lf %lf %lf", &c, &f, &x);
		while (1){
			if (x / production > c / production + x / (production + f)){
				ans += c / production;
				production += f;
			} else {
				ans += x / production;
				printf("%.7lf\n", ans);
				break;
			}
		}
	}
	return 0;
}
