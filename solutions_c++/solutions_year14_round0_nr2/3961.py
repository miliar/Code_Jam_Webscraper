#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
double C, F, X;
double total;

void func(double curr, double P){
	if(curr == X){
		return;
	}
	if(curr >= C){
		double t1 = (X - curr)/(P);
		double t2 = (X) / (P+F);
		if(t1 <= t2){
			total += t1;
		}else{
			func(curr-C, P+F);
		}
	}else{
		if(X <= C){
			double t1 = (X-curr)/(P);
			total += t1;
		}else{
			double t2 = (C-curr)/(P);
			total += t2;
			func(C, P);
		}
	}
}

int main(){
	int tc;
	cin >> tc;
	for(int tcase=1 ; tcase<=tc; tcase++){
		cin >> C >> F >> X;
		
		total = 0;
		func(0, 2);
		
		cout << "Case #" << tcase << ": ";
		printf("%.7lf\n", total);
	}
	return 0;
}
