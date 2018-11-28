#include<bits/stdc++.h>
using namespace std;
typedef long double LD;
const LD EPS=(LD)1e-9;
bool zero(LD x){
	if(-EPS<x&&x<EPS) return true;
	return false;
}

main(){
	int test;scanf("%d",&test);
	for(int tnu=1;tnu<=test;tnu++){
		int n;scanf("%d",&n);
		LD v,x;scanf("%Lf%Lf",&v,&x);
		LD r1,c1;scanf("%Lf%Lf",&r1,&c1);
		if(n==1){
			printf("Case #%d: ",tnu);
			if(!zero(x-c1)) puts("IMPOSSIBLE");
			else printf("%.12Lf\n",v/r1);
			continue;
		}
		LD r2,c2;scanf("%Lf%Lf",&r2,&c2);
		printf("Case #%d: ",tnu);
		if((c1>x+EPS&&c2>x+EPS)||(c1<x-EPS&&c2<x-EPS)) { puts("IMPOSSIBLE");continue;}
		if(zero(c1-x)&&zero(c2-x)) printf("%.12Lf\n",v/(r1+r2));
		if(zero(c1-x)&&zero(c2-x)) continue;
		if(zero(c1-x)) printf("%.12Lf\n",v/(r1));
		if(zero(c2-x)) printf("%.12Lf\n",v/(r2));
		if(zero(c1-x)||zero(c2-x)) continue;
		if(c1>x+EPS) swap(c1,c2),swap(r1,r2);
		LD vv1=x-c1,vv2=c2-x;
		LD k=vv2/vv1;
		//printf("k==%.6Lf ",k);
		LD v1=v*k/(k+1.),v2=v*1/(k+1.);
		LD wyn=max(v1/r1,v2/r2);
		printf("%.12Lf\n",wyn);
	}
}
		
		
