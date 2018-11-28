#include <bits/stdc++.h>
const int N=4;
double C,F,X;
int main(){
	int w=1;
	int T;scanf("%d",&T);
	while(T--){
		scanf("%lf%lf%lf",&C,&F,&X);
		double Min=1e29;
		int cnt=0;
		double nowt=0,nowF=2;
		for(int i=0;;i++){
			double a=nowt+X/nowF;
			if(Min > a){
				cnt=0;
				Min=a;
			}
			else cnt++;
			if(cnt>200)break;
			nowt+=C/nowF;
			nowF+=F;
		}
		printf("Case #%d: %.7lf\n",w++,Min);
	}
}
