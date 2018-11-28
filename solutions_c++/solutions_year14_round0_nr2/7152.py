#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main() {
	int t;
	double C, F, X;
	scanf("%d", &t);
	for(int cnt = 1; cnt <= t; cnt++) {
		scanf("%lf %lf %lf", &C, &F, &X);
		double min = -1.0;
		double rate = 2.0;
		double time = 0.0;
		while(true) {
			long double check = time+(X/rate);
			if(min == -1.0) min = check;
			else if(check < min) min = check;
			else break;
			time += C/rate;
			rate += F;
		}
		printf("Case #%d: %lf\n", cnt, min);
	}
}
