#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
double C, F, X;
#define EPS 1E-7
#pragma comment(linker, "/STACK:10000000")


double f(double money, double time, double prod, int turn){
	if(X<=C){
		return X/2;
	}
	if(money>=X){
		return time;
	}
	double f1 = (C-money)/prod; //build new
	f1 = max(0.,f1);
	double f2 = (X-money)/prod; //straight
	if(turn>106100)return (time+f2);
	return min(f(0,time+f1,prod+F,turn+1), time+f2);
}


int main(){
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i=0; i<t; ++i){
		scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: %.9lf\n", i+1, f(0,0,2,0));
	}
	
	return 0;
}