#include<stdio.h>
using namespace std;
int main(){
	int t,count=0,end;
	scanf("%d",&t);
	double c,x,f,ans,speed;
	while(t--){
		count++;
		ans=0;
		end=1;
		speed=2;
		scanf("%lf %lf %lf",&c,&f,&x);
		while(end){
			if(x/(speed+f)<(x-c)/speed){
				ans+=c/speed;
				speed+=f;
			}
			else
			{
				ans+=x/speed;
				end=0;
			}
		}
		printf("Case #%d: %f\n",count,ans);
	}
}
