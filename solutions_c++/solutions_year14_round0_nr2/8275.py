#include<stdio.h>
#include <iostream>
using namespace std;
double sum =0;

void func(double c,double f,double x,double param){
	double val1 = x/param;
	double val2 = c/param;
	if(val1 < (val2 + x/(param+f)) ){
		sum +=val1;
	//	printf("yoyo %lf\n",sum);
		return;
	} else {
		sum +=val2;
	//printf("toto %lf\n",sum);
		func(c,f,x,param+f);
	}
	
}
int main() {
	// your code goes here
	int t;
	double c,f,x;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		sum = 0;
		func(c,f,x,2);
		printf("Case #%d: %.7lf\n",i+1,sum);
	}
	return 0;
}