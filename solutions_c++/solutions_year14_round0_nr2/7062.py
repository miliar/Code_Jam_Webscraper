#include<iostream>
#include<stdio.h>
#include<algorithm>
double rates[3][100000];
using namespace std;
int main() {
	int test,rate=2;
	double Answer=99999999.0,C,F,X,withoutC;
	scanf("%d",&test);
	for( int tst=1; tst<=test; tst++) {
		cin >> C;cin >> F;cin >> X;
		double f=2.0;
		for( int i=0; i<100000; i++) {
			rates[0][i] = C / f;
			if( i >=1) {
				rates[0][i]+=rates[0][i-1];
				rates[1][i-1] = X / f; 
			}
			f+=F;
		}
		for( int i=0; i<100000; i++) {
			rates[2][i] = rates[0][i] + rates[1][i];
			if ( i >=1 ) {
				if ( rates[2][i] > rates[2][i-1]) {
					Answer = rates[2][i-1];
					break;
				}
			}
		}
		withoutC = X / 2.0;
		if ( withoutC < Answer ) Answer = withoutC;
		printf("Case #%d: %.7lf\n",tst,Answer);
	}
	return 0;
}
