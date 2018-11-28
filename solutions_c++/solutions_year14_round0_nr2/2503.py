#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int T;
double c,f,x;
int main(){
	scanf("%d",&T);
	for(int tt=1;tt<=T;++tt){
		printf("Case #%d: ",tt);
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=x/2.0,tmp=0.0;
		int cnt=0;
		int tot=100000;
		while(tot--){
			tmp+=c/(2.0+cnt*f);
			cnt++;
			ans=min(ans,tmp+x/(2.0+cnt*f));
		}
		printf("%.7lf\n",ans);
	}	
	return 0;
}
