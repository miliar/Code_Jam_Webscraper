#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;


double C,F,X;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,tt=0;
	scanf("%d",&t);
	while(t--){
		scanf("%lf %lf %lf",&C,&F,&X);
		double ans = X / 2;
		double tmp=0.0;
		double rate = 2.0;
		double now;
		int i = 0;
		while(true){
			tmp += C/rate;
			rate += F;
			now = tmp + X / rate;
			if(now < ans){
				ans = now;
			}
			else break;
		}
		printf("Case #%d: %.7lf\n",++tt,ans);
	}
	return 0;
}
