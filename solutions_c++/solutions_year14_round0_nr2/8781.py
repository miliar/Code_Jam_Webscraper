#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

using namespace std;
int main(int argc, char ** argv) 
{
	int T;

	scanf("%d", &T);
	for(int iter = 1; iter <= T; iter++) {
		double C, F, X;
		//cin >> C >> F >> X;
		scanf("%lf %lf %lf", &C, &F, &X);
		double minTime = X/2.0;
		double a_prev = X/2.0;
		int n = 1;
		while(1) {
			double a = a_prev + C/((n - 1) * F + 2) - (X * F) / ( ((n-1)*F + 2) * (n * F + 2));
			if(a > minTime) 
				break;
			else
				minTime = a;
			a_prev = a;
			n++;
		}
		//cout << "Case #" << iter << ": " << minTime << endl;
		printf("Case #%d: %.7lf\n", iter, minTime);
	}
	return 0;
}