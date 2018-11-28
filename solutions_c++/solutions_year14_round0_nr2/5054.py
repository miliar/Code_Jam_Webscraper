#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main(){
    int T;
    double C,F,X,time,E;
    scanf("%d",&T);
    for(int t = 1; t <= T; t++){
	scanf("%lf%lf%lf",&C,&F,&X);
	time = 0.0;
	E = 2.0;
	while(1){
	   double time1 = X / E;
	   double time2 = C / E + X / (E + F);
	   if(time1 <= time2){
		time += time1;
		break;
	   }else{
		time += C / E;
		E += F;
	   }
	}
	printf("Case #%d: %.7lf\n",t,time);
    }
    return 0;
}
