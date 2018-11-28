#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

#define MAXN 100001

int T;
double C, F, X;

double tme[2][MAXN];

int main(){

	scanf("%d ", &T);
	for(int cas = 1; cas <= T;cas++){
		scanf("%lf %lf %lf ", &C, &F, &X);

		tme[0][0] = X / 2.0;
		tme[1][0] = C / 2.0;

		double min = tme[0][0];

		// Iterate over number of cookie factories
		int i = 1;
		while(i < MAXN){
			tme[0][i] = tme[1][i-1] + X / (2.0 + i * F);
			tme[1][i] = tme[1][i-1] + C / (2.0 + i * F);

			if(tme[0][i] < min)
				min = tme[0][i];
			else
				break;

			i++;
							
		}
		printf("Case #%d: %.7lf\n", cas, min);


	}

	return 0;
}
