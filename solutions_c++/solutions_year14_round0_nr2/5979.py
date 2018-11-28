#include<iostream>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<iomanip>
using namespace std;
long double C, F, X;

int main(){
	int testcase;
	int cnt=0;
	scanf("%d", &testcase);
	while(testcase--){
		scanf("%LF%LF%LF", &C, &F, &X);
		long double tmp = 0.0;
		long double time = 0.0;
		//double farm = 0;
		long double rate = 2;
		while(C/rate + X/(rate+F) < X/rate){
			time += C/rate;
			tmp += time;
			rate+=F;
		}
		time += X/rate;
		printf("Case #%d: %.7LF\n", ++cnt, time);
	}
	return 0;
}
