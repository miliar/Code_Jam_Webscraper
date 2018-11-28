#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	int t;
	double c,f,x;
	cin>>t;
	double value;
	double rate = 2.0000000;
	double time;
	int tt=1;
	while(tt<=t){
		rate = 2.0000000;
		time=0;
		value=0;
		cin>>c>>f>>x;
		while(value<x){
			if(value>=c){
				if(((x-value+c)/(rate+f))<((x-value)/rate)){
					rate+=f;
					value-=c;
				}
			}
			if(value+c<x){
				time+=(c/rate);
				value+=(c);
			}
			else{
				time+=((x-value)/rate);
				value+=(x-value);
			}
		}
		printf("Case #%d: %.7f\n",tt,time);
		tt++;
	}
	return 0;
}
