#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int T,i=1;
	for(cin>>T;T--;i++){
		double c=0,C,F,X,t=0,r=2;
		cin>>C>>F>>X;
		t+=C/r;
		while(X/(r+F)<(X-C)/r){
			r+=F;
			t+=C/r;
		}
		t+=(X-C)/r;
		printf("Case #%d: %.7lf\n", i, t);
	}
	return 1;
}