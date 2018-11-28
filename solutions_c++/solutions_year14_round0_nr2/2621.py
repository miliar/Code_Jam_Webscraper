#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define PRINTCASE printf("Case #%d: ",case_n++)
#define PRINTCASE_ printf("Case #%d:\n",case_n++)
#define RD(a) scanf("%d", &a)
#define RDD(a, b) scanf("%d%d", &a, &b)

double C, F, X;

double cal_time(int n){
	double rate = 2, time = 0;
	while(n--){
		time += C / rate;
		rate += F;
	}
	return time + X / rate;
}

double go(){
	double o = cal_time(0);
	for(int i = 1; ; ++i){
		double tmp = cal_time(i);
		if(tmp < o){
			o = tmp;
		}else{
			return o;
		}
	}
}

int main(){
	freopen("large-in.txt", "r", stdin);
	freopen("large-out.txt", "w", stdout);
	CASET{
		cin >> C >> F >> X;
		PRINTCASE;
		printf("%.7lf\n", go());
	}
	return 0;
}