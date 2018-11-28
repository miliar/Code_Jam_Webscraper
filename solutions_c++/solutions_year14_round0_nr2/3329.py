#include <cstdio>

double min(double a, double b) { return (a < b) ? a : b; }

//[x][y]
int grid[5][5];

int main() {
	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++) {
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);

		double cookies = 0;
		int farms = 0;
		double tim = 0;
		bool stop = false;
		while (true) {
			double cookiesToFarm = C-cookies;
			double timeToFarm = cookiesToFarm/(2+farms*F);

			if (X-cookies <= cookiesToFarm) {
				tim += (X-cookies)/(2+farms*F);
				break;
			}

			cookies += cookiesToFarm;
			tim += timeToFarm;

			while (cookies >= C) {
				double rate1 = (X-cookies)/(2 + farms*F);
				double rate2 = (X-cookies+C)/(2 + (farms+1)*F);
				if (rate2 < rate1) {
					farms++;
					cookies -= C;
				} else {
					tim += rate1;
					stop = true;
					break;
				}
			}

			if (stop) break;

		}

		double maxTime = X/2;
		printf("Case #%d: %.7lf\n", i, min(tim, maxTime));
	}

	return 0;
}