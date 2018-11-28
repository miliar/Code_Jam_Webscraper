#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
double C, F, X;
double calc(double n){
	if (n<=0) return X/2;
	double tot = 0;
	for (int i = 0; i<n; i++){
		tot += C/(2+i*F);
	}
	tot += X/(2+n*F);
	return tot;
}
int main(){
	int T, cas = 0;
	for (cin>>T; T--;){
		cout<<"Case #"<<++cas<<": ";
		cin>>C>>F>>X;
		int n = X/C-2.0/F;
		double minx = X/2;
		minx = min(minx, calc(n));
		minx = min(minx, calc(n+1));

		printf("%.7f\n", minx);
	}
	return 0;
}

