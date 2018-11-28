#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

int main() {
	int T,tc,i;
	freopen("input.in","r",stdin);
	freopen("ans.txt","w",stdout);
	double C,F,X;
	scanf("%d",&T);
	for(tc=1;tc<=T;tc++) {
		scanf("%lf%lf%lf",&C,&F,&X);
		double ans=1e30,sum=0;
		double D=2;
		for(i=0;;i++) {
			double tmp=sum+X/D;
			ans=min(ans,tmp);
			if(tmp>ans) break;
			sum+=C/D;
			D+=F;
		}
		printf("Case #%d: %.8lf\n",tc,ans);
	}
}



