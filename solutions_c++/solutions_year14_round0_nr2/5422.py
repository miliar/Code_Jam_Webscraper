#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string.h>
#include <queue>

using namespace std;

int T;

int main(){
	scanf("%d", &T);
	double C, F, X;
	for (int i = 0; i < T; i ++){
		scanf("%lf %lf %lf", &C, &F, &X);
		double Ans = 0;
		for (int j = 0;; j ++){
			if (Ans + C / ((double)j * F + 2) +  
					X / ((double)(j + 1) * F + 2)
				> Ans + X / ((double)(j) * F + 2))
			{
				Ans = Ans + X / ((double)(j) * F + 2);
				break;
			}
			Ans = Ans + C / ((double)j * F + 2);
		}
		printf("Case #%d: %.7f\n", i + 1, Ans);
	}
}

