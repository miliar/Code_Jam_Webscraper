#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
int t;
cin>>t;
for(int p=0;p<t;p++){
	
	double C,F,X;
	cin>>C>>F>>X;
	
	double time=0;
	double  inc=2;
	while(X/inc>(X/(inc+F))+C/inc){
		time+=C/inc;
		inc+=F;
	}

	time+=X/inc;
	printf("Case #%d: %.7f\n",p+1,time);
}
}
