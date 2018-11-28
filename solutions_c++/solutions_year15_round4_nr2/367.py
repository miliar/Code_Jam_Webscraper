#include<cstdio>
#include<cmath>
#include<algorithm>
#define N 110
#define eps 1e-8
using namespace std;
bool same(double a,double b){
	return a<b+eps&&b<a+eps;
}
int main(){
	int T,cs,n,i;
	double x,v;
	double c[N],r[N];
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++){
		scanf("%d",&n);
		scanf("%lf%lf",&v,&x);
		for(i=0;i<n;i++){
			scanf("%lf%lf",&r[i],&c[i]);
		}
		printf("Case #%d: ",cs);
		if(n==1){
			if(same(c[0],x)) printf("%.7f\n",v/r[0]);
			else printf("IMPOSSIBLE\n");
		}
		else{
			if(same(c[0],c[1])){
				if(same(c[0],x)){
					printf("%.7f\n",v/(r[0]+r[1]));
				}
				else printf("IMPOSSIBLE\n");
			}
			else if((c[0]+eps<x&&c[1]+eps<x)||(c[0]-eps>x&&c[1]-eps>x)){
				printf("IMPOSSIBLE\n");
			}
			else{
				printf("%.7f\n",max(v*(c[1]-x)/(c[1]-c[0])/r[0],v*(x-c[0])/(c[1]-c[0])/r[1]));
			}
		}
	}
	return 0;
}