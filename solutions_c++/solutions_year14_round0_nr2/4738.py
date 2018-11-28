#include<iostream>
#include<vector>
#include<string.h>
#include<fstream>
#include<stdio.h>
#include<cmath>
using namespace std;

double timeToGetXFarms(int X, double F, double C){
	double rate = 2.0;
	double secs = 0.0;
	for(int i = 0; i < X; ++ i){
		secs += C/rate;
		rate += F;
	}
	return secs;
}
double solve(int farms, double F, double C, double X){
	double secs = timeToGetXFarms(farms, F, C);
	secs += X/(2.0 + F*farms);
	return secs;
}
double search(int start, double F, double C, double X){
	double prev = solve(start,F,C,X);
	for(int i = start+1;; i ++){
		double tmp = solve(i, F, C, X);
		if(abs(tmp - prev) < 0.0000001 || prev < tmp){
			prev = min(tmp,prev);
			break;
		}
		prev = tmp;
	}
	return prev;
}
int main(){
	ifstream in("B-small-attempt1.in");
	FILE *pFile = fopen("B.out", "w");
	int t, mxFarms;
	double C, F, X;
	in >> t;
	for(int x = 1; x <= t; ++ x){
		in >> C >> F >> X;
		mxFarms = X/((F+2.0)*0.0000001) + 0.5; 
		fprintf(pFile, "Case #%d: %0.7f\n", x, search(0, F, C, X));
	}
	return 0;
}