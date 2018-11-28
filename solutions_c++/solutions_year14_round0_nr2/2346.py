#include <iostream>
#include <cstdio>
using namespace std;

int t;
double f,c,x;
const double eps=1e-12;

int main(){
	scanf("%d",&t);
	for(int tt=1; tt<=t; tt++){
		printf("Case #%d: ",tt);	
		scanf("%lf %lf %lf",&c,&f,&x);
		double tot=x;
		double ans=x/2.0,lt=0;
		int cnt=0;
		while(tot-ans > eps){
			tot=ans;
			lt+=c/(2.0+cnt*f);
			cnt++;
			ans=x/(2.0+cnt*f)+lt;
		}
		ans=min(ans,tot);
		printf("%.7lf\n",tot);
	}
	return 0;
}
