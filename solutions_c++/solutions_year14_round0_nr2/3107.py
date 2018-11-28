#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++){
		double c,f,x;
		double sum=0;
		cin>>c>>f>>x;
		double tt=0;
		double speed=2;
		while(sum<x){
			if(sum+c>=x){
				tt+=(x-sum)/speed;
				break;
			}
			sum+=c;
			tt+=c/speed;
			if((x-sum)/speed>(x-sum+c)/(speed+f)){
				sum-=c;
				speed+=f;
			}
		}
		printf("Case #%d: ",ii);
		printf("%.7lf\n",tt);

	}
}