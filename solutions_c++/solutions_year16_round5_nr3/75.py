#include<stdio.h>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;
int n,la;
int ace[1111];
int ancestor(int x){return x-ace[x]?ace[x]=ancestor(ace[x]):x;}
pair<double,pair<int,int> > a[1111*1111];
double x[1111],y[1111],z[1111];
double sqr(double x){
	return x*x;
}
int main(){
	int _;
	scanf("%d",&_);
	for(int T=1; T<=_; T++){
		scanf("%d%*d",&n);
		la=0;
		for(int i=0; i<n; i++){
			scanf("%lf%lf%lf",&x[i],&y[i],&z[i]);
			scanf("%*lf%*lf%*lf");
			ace[i]=i;
		}
		for(int i=0; i<n; i++)
			for(int j=i+1; j<n; j++)
				a[la++]=make_pair(sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j])+sqr(z[i]-z[j])),make_pair(i,j));
		sort(a,a+la);
		double res=1e9;
		for(int i=0; i<la; i++){
			int x=a[i].second.first,y=a[i].second.second;
			ace[ancestor(x)]=ancestor(y);
			if(ancestor(0)==ancestor(1)){
				res=a[i].first;
				break;
			}
		}
		printf("Case #%d: %lf\n",T,res);
	}
	return 0;
}