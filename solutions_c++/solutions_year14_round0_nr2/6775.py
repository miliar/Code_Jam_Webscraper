#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	int z;
	scanf("%d",&z);
	for(int k = 1; k<=z; k++){
		double C,F,X,cpr = 2.0,time = 0;
		scanf("%lf%lf%lf",&C,&F,&X);
		while(true){
			if( C/cpr + X/(cpr+F) < X/cpr){
				time += C/cpr;
				cpr += F;
			}
			else{
				time += X/cpr;
				break;
			}
		}
		printf("Case #%d: %.7lf\n",k,time);
	}
}
