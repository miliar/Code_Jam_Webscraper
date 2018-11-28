#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int M = 100000;

double solve(double C, double F, double X){
	double res = 1e77, r = 2.0, time = 0;
	for(int i=0;i<=M+1;i++){
		res = min(res, time + X / r);
		time += C / r;
		r += F;
	}
	return res;
}

int main(){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		double C, F, X;
		cin >> C >> F >> X;
		printf("Case #%d: %.7f\n", t + 1, solve(C, F, X));
	}
	return 0;
}
