#include <iostream>
#include <cstdio>
using namespace std;


long double C;
long double F;
long double X;

long double CPC;

int main() {
	int testcase = 0;

	cin >> testcase;
	for (int tCase = 1; tCase <=testcase; ++tCase) {
		cin >> C >> F >> X;

		long double currentTime = 0;
		CPC = 2;
		while (1) {
			long double expectTimeWhenNotBuyFarm = currentTime + (X / CPC);

			long double timeToBuyFarm = C / CPC;
			long double CPCAfterBuyFarm = CPC + F;
			long double expectTimeWhenBuyFarm= currentTime + timeToBuyFarm + (X / CPCAfterBuyFarm);

			if (expectTimeWhenNotBuyFarm < expectTimeWhenBuyFarm) {
				currentTime = expectTimeWhenNotBuyFarm;
				break;
			}
			currentTime += timeToBuyFarm;
			CPC += F;

		}

		printf("Case #%d: %.7Lf\n", tCase, currentTime);
	}

}
