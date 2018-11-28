#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
const double eps = 1e-8;

int main()
{
	freopen("B--small-attempt0.in", "r", stdin);
	freopen("B--small-attempt0.out", "w", stdout);
	int T;
	double C, F, X;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		double sum = 0.0;
		double curObtain = 2.0;
		while (1) {
			double t1 = sum + X / curObtain;
			double nextObtain = curObtain + F;
			double t2 = sum + C / curObtain + X / nextObtain;
			if (t1<t2 || abs(t1-t2)<eps) {
				sum += X / curObtain;
				break;
			} else {
				sum += C / curObtain;
				curObtain = nextObtain;
			}
		}
		printf("Case #%d: %.7lf\n", t, sum);
	}
	return 0;
}