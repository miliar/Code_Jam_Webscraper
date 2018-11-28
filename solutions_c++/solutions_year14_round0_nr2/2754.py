#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
	int T, n;
	double C, F, X, R;
	cin>>T;
	for(n=1; n<=T; n++){
		C=F=X=0;
		R=2.0;
		double total=0,time=0, arr[999];
		int ar=0;
		cin>>C>>F>>X;
		while(1){
			if( (X/R) < ( C/R + X/(R+F) ) ){
				time=time+X/R;
				break;
			}
			else{
				time=time+C/R;
				R=R+F;
			}
		}
		printf("Case #%d : %.7lf\n",n,time);
	}
	return 0;
}
