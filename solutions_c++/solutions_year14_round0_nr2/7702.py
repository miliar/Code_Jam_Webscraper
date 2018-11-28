#include<stdio.h>
using namespace std;

int main(){
	int t,cnt=1;
	scanf("%i",&t);
	while(t--){
		double temp,curr=0,rate=2;
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		do{
			temp=curr+x/rate;
			curr+=c/rate;
			rate+=f;
		}while(curr+x/rate<temp);
		printf("Case #%i: %.7lf\n",cnt,temp);
		cnt++;
	}
}