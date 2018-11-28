#include<cstdio>
#include<cmath>
#include<iostream>
using namespace std;

bool check(long double time,long double c,long double f,long double x){
	long double gain=2.0;
	while(time>0){
		if(time*gain-x>1e-9)return true;
		long double farm=c/gain;
		time-=farm;
		gain+=f;
	}
	return false;
}

void f(){
	long double c,f,x;
	scanf("%Lg%Lg%Lg",&c,&f,&x);
//	printf("%Lf %Lf %Lf\n",c,f,x);
	long double a=0,b=(long double)(x)/2;
	while(b-a>1e-8){
		long double k=(a+b)/2;
		//printf("%Lf\n",k);
		if(check(k,c,f,x))b=k;
		else a=k;
	}
	printf("%.7Lf\n",a);
}

int main(){
	int a;
	scanf("%d",&a);
	for(int i=1;i<=a;i++){
		printf("Case #%d: ",i);
		f();
	}
}
