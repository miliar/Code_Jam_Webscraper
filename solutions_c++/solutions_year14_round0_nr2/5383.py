#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
	freopen("1.txt","r",stdin);
	freopen("1.out","w",stdout);
	int T,Tnum=0;
	scanf("%d",&T);
	for (;T;--T){
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double ans=X/2;
		double V=2,t=0;
		for (int i=1; i<=1000000;++i){
			double t1=C/V;
			if (t>ans)break; 
			ans=min(ans,t+X/V);
			//printf("%f %f %f\n",t,X/V);
			t=t+t1;
			V+=F;
		}
		printf("Case #%d: %.10f\n",++Tnum,ans);
	}
}
