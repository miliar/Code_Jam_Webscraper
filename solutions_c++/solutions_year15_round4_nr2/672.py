#include<set>
#include<map>
#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<queue>
#include<math.h>
using namespace std;
int n;
double v,x;
struct P{
	double r,c;
}p[100];
bool cmp(P a,P b){
	return a.c<b.c;
}
double eps=1e-9,eps1=1e-12;
bool _more(double ti,double vv,double xx){
	double sv=0,st=0;
	for(int i=n-1;i>=0;i--){
		double tv=min(vv-sv,p[i].r*ti);
		sv+=tv;
		st+=tv*p[i].c;
	}
	return sv+eps1>vv&&st/sv>xx-eps1;
}
bool _less(double ti,double vv,double xx){
	double sv=0,st=0;
	for(int i=0;i<n;i++){
		double tv=min(vv-sv,p[i].r*ti);
		sv+=tv;
		st+=tv*p[i].c;
	}
	return sv+eps1>vv&&st/sv<xx+eps1;
}
int main(){
	int ca;
	scanf("%d",&ca);
	for(int cas=1;cas<=ca;cas++){
		scanf("%d%lf%lf",&n,&v,&x);
		for(int i=0;i<n;i++)
			scanf("%lf%lf",&p[i].r,&p[i].c);
		sort(p,p+n,cmp);
		printf("Case #%d: ",cas);
		double low=0,high=100000000;
		if(p[0].c>x+eps||p[n-1].c<x-eps)printf("IMPOSSIBLE\n");
		else{
			while(high-low>eps){
				double mid=(high+low)/2;
				if(_less(mid,v,x)&&_more(mid,v,x))high=mid;
				else low=mid;
			}
			printf("%.8lf\n",low);
		}
	}
}
