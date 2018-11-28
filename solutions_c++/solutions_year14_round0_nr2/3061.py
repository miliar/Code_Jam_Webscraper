#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void Solution(){
	double C, F, X;
	cin>>C>>F>>X;
	
	double R = X / 2;
	double T = 0;
	double I = 2;
	for(int i = 0;;i++){
		if(T > R)break;
		T += C / I;
		I += F;
		double TEMP = T + X / I;
		if(TEMP < R)R = TEMP;
	}
	printf("%.7lf\n", R);
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin>>t;
	for(int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		Solution();
	}
	return 0;
}
