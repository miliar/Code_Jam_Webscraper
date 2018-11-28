#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <cmath>
#define sq(x) ((x)*(x))
using namespace std;
#define N 1010
int n;

vector<double> x(N),y(N),z(N);
vector<double> vx(N),vy(N),vz(N);

int vis[2000];

void saiki(int p,double lim){
	if(vis[p]==1)return;
	vis[p]=1;
	for(int q=0;q<n;q++){
		if(pow(x[p]-x[q],2)+pow(y[p]-y[q],2)+pow(z[p]-z[q],2)<=lim*lim)saiki(q,lim);
	}
}

int main(){
	int testcases;
	scanf("%d",&testcases);
	for(int casenum=1;casenum<=testcases;casenum++){
		printf("Case #%d: ",casenum);
		int s;
		scanf("%d%d",&n,&s);
		
		
		for(int i=0;i<n;i++){
			scanf("%lf%lf%lf%lf%lf%lf",&x[i],&y[i],&z[i],&vz[i],&vy[i],&vz[i]);
		}
		
		double lb=0,ub=10000;
		for(int z=0;z<100;z++){
			double mid=(lb+ub)/2;
			for(int i=0;i<n;i++)vis[i]=0;
			saiki(0,mid);
			if(vis[1]==1)ub=mid; else lb=mid;
		}
		printf("%.10f\n",ub);
	}
}