#include <iostream>
#include <stdio.h>
#include <cmath>
#define FOR(i,j) for(int i=0;i<j;i++)
using namespace std;

int main(){
	int T;
	double C,F,X,ted,minbet,sum,rate=2;
	cin>>T;
	int casenum=0;
	while(casenum<T){
		casenum++;
		cin>>C>>F>>X;
		minbet=X/rate;
		sum=X/rate;
		FOR(i,1000000) {
			sum+=(C/(rate+(i*F)));
			sum-=(X/(rate+(i*F)));
			sum+=(X/(rate+((i+1)*F)));
			if (sum<minbet) minbet=sum;
		}
		printf("Case #%d: %.7f\n",casenum,minbet);/* code */
	
	}

}