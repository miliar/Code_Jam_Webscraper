#include <cstdio>
#include <algorithm>
using namespace std;

int T;
double C, F, X;

int main()
{
	scanf("%d", &T);
	for(int t=0;t++<T;){
		scanf("%lf%lf%lf", &C, &F, &X);

		double ret = X / 2;
		double time = 0, cps = 2;
		for(int i=1;i<=1000000;i++){
			time += C / cps;
			cps += F;
			ret = min(ret, time + X / cps);
		}

		printf("Case #%d: %.7f\n", t, ret);
	}

	return 0;
}
