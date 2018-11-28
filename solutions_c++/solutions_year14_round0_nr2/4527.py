#include<cstdio>
#include<iostream>
using namespace std;

double solve(double C,double F,double X){
	double result=X;
	double buy_farm_time=0.0;
	for(double rate=2.0;;rate+=F){
		if(result>buy_farm_time+X/rate){
			result=buy_farm_time+X/rate;
		}else
			break;
		buy_farm_time+=C/rate;
	}
	return result;
}


int main(){
	
	int T;
	double C,F,X,answer;
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		scanf("%lf %lf %lf",&C,&F,&X);
		//cin>>C>>F>>X;
		answer=solve(C,F,X);
		printf("Case #%d: %.7lf\n",testcase,answer);
	}
	
	return 0;
}
