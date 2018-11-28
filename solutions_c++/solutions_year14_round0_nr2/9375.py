// codejam-cookie-clicker-alpha.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

//#define ONLINE
void online(){
#ifdef ONLINE
#else
	#pragma warning(disable:4996)
	freopen("F:\\新的桌面文件\\tmp\\0.txt","r",stdin);
	freopen("F:\\新的桌面文件\\tmp\\1.txt","w",stdout);
#endif
}

int T;
double C;
double F;
double X;

double buy_k_farm( double k, double inc, double farm_cost,  double farm_inc ) {
	if (k == 0) {
		return 0.0;
	} else {
		double cost = 0.0;
		for (int i=0; i<k; ++i) {
			cost += farm_cost/(inc+i*farm_inc);
		}
		return cost;
	}
}

int main() {

	online();
	scanf("%d",&T);
	for (int k=1; k<=T; ++k) {
		scanf("%lf%lf%lf", &C, &F, &X);

		double result = X/2.0;
		double cost   = buy_k_farm(1.0, 2.0, C, F) + X/(2.0+F);
		double i = 2.0;
		while (cost <= result) {
			result = cost;
			cost   = buy_k_farm( i, 2.0, C, F) + X/(2.0+i*F);
			i = i+1.0;
		}
		printf("Case #%d: %.7lf\n", k, result);
	}
	return 0;
}
