#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#define eps 1e-11
using namespace std;
int n;
double r[110],c[110],V,X;

 double fuck()
 {
 	int i;
 	double x1,x2,d;
 	scanf("%d%lf%lf",&n,&V,&X);
 	for(i=1;i<=n;i++)
 		scanf("%lf%lf",&r[i],&c[i]);
 	if(n==1){
 		if(fabs(X-c[1])>eps) return -1;
 		else return V/r[1];
 	}
 	if(n==2){
 		if(fabs(c[1]-c[2])<eps){
 			if(fabs(X-c[1])>eps) return -1;
 			return V/(r[1]+r[2]);
 		}
 		d=1/(r[1]*r[2]*(c[2]-c[1]));
 		x1=d*(r[2]*c[2]*V-r[2]*V*X);
 		x2=d*(-r[1]*c[1]*V+r[1]*V*X);
 		if(x1<0||x2<0) return -1;
 		else return max(x1,x2);
 	}
 }

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,k;
	double a;
	scanf("%d",&t);
	for(k=1;k<=t;k++){
		printf("Case #%d: ",k);
		a=fuck();
		if(a<0) printf("IMPOSSIBLE\n");
		else printf("%.9lf\n",a);
	}
 return 0;
}

