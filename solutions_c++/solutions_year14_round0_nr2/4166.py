#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int T;
double C, F, X;
double F0 = 2;
double Fs, Ts;
double mint, calt;


int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &T);
//	printf("%d\n", T);
	int nCase = 1;
	while (T-- > 0){

		scanf("%lf", &C);
//		printf("%lf ", C);
		scanf("%lf", &F);
//		printf("%lf ", F);
		scanf("%lf", &X);
//		printf("%lf\n", X);

		
		Fs = F0;
		Ts = 0;
		mint = X/Fs;

		while (1){
			
			Ts = Ts + C / Fs;
			Fs += F;
			calt = Ts + X / Fs;
			if (calt < mint){
				mint = calt;
				continue;
			}
			else{
				break;
			}	
		}

		printf("Case #%d: %.7f\n", nCase, mint);	
		nCase++;
	}

	return 0;
}