#include <bits/stdc++.h>
using namespace std;
int Test,N;
double S;
class rec{
	public:
	double x,y,z,vx,vy,vz;
}P[1010];
bool vis[1010];
int q[1010];
double dist(int x,int y){
	double res=0;
	res+=(P[x].x-P[y].x)*(P[x].x-P[y].x);
	res+=(P[x].y-P[y].y)*(P[x].y-P[y].y);
	res+=(P[x].z-P[y].z)*(P[x].z-P[y].z);
	return sqrt(res);
}
bool check(double lim){
	memset(vis,0,sizeof(vis));
	vis[0]=1;
	int l,r;
	for (q[l=r=0]=0;l<=r;l++){
		int x=q[l];
		for (int i=0;i<N;i++)
			if (!vis[i]&&dist(x,i)<lim){
				vis[i]=1;
				q[++r]=i;
			}
	}
	if (vis[1])return 1;
	return 0;
}
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&Test);
	for (int tt=1;tt<=Test;tt++){
		scanf("%d%lf",&N,&S);
		for (int i=0;i<N;i++)
			scanf("%lf%lf%lf%lf%lf%lf",&P[i].x,&P[i].y,&P[i].z,&P[i].vx,&P[i].vy,&P[i].vz);
		double l=0,r=0;
		for (int i=0;i<N;i++)
			for (int j=0;j<N;j++)
				r=max(r,dist(i,j));
		while (r-l>1e-6){
			double mid=(l+r)/2;
			if (check(mid))r=mid;
			else l=mid;
		}
		printf("Case #%d: %.5lf\n",tt,r);
	}
}