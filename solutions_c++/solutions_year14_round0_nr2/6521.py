#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int t,TESTCASE;
	double c,f,x,rate;
	double time,ans,fact;
	cin >> TESTCASE;
	for(t=1;t<=TESTCASE;t++){
		cin >> c >> f >> x;
		rate=2; time=x/rate; ans=time; fact=0;
		while(ans>=time){
			ans=time;
			fact+=(c/rate);
			rate+=f;
			time=fact+(x/rate);
		}
		printf("Case #%d: %.7f\n",t,ans);
	}
	return 0;
}
