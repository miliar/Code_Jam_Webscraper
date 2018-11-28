#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;


int main(){

	int t;
	cin>>t;
	int c = 1;
	while(t--){
		double Cs = 2;
		double C,F,X;
		cin>>C>>F>>X;
		double Timemin = X/Cs;
		double Timeini = 0.0;
		while(1){
			Timeini+=C/Cs;
			Cs+=F;
			if(Timemin<Timeini + X/Cs)
				break;
			Timemin = min(Timemin,Timeini + X/Cs);
		}
		printf("Case #%d: %.7lf\n", c++,Timemin);

	}

	return 0;
}