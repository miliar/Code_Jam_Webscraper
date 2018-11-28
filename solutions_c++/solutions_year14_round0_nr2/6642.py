#include <cstdio>
#include <iostream>
using namespace std;

double cost, farmProd, X;

int main() {

	int cases;
	scanf("%d", &cases);
	for(int T=1; T<=cases; ++T) {

		scanf("%lf %lf %lf", &cost, &farmProd, &X);

		double ans = 0.0;
		int own = 0;
		while(1) {

			double buying = X/((own+1)*farmProd+2.0) + cost/(own*farmProd+2.0);
			double notBuying = X/(own*farmProd+2.0);

			if(buying > notBuying) {
				ans += notBuying;
				break;
			}
			else {
				ans += cost/(own*farmProd+2);
				++own;
			}

		}

		printf("Case #%d: %.7lf\n", T, ans);

	}

	return 0;

}
