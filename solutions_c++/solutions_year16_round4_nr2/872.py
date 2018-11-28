#include<bits/stdc++.h>
using namespace std;
const int maxn=210;
double f[maxn][maxn][maxn],ans,s;
int n,nk,T;
double p[maxn];
int have[maxn];
void dfs(int a,int b,double c){

	if(a>nk){
		if(b==nk/2){
			s+=c;
		}
		return;
	}
	dfs(a+1,b+1,c*p[have[a]]);
	dfs(a+1,b,c*(1-p[have[a]]));
}
void sou(int dep,int a){
	if(dep>n){
		if(a==nk){
			s=0;
			dfs(1,0,1.0);
			ans=max(ans,s);
		}
		return;
	}
	have[a+1]=dep;
	sou(dep+1,a+1);
	sou(dep+1,a);
}
	
int main(){
	freopen("t.in","r",stdin);
	freopen("t.out","w",stdout);
	scanf("%d",&T);
	for(int ti=1;ti<=T;ti++){
		printf("Case #%d: ",ti);
		scanf("%d%d",&n,&nk);
		for(int i=1;i<=n;i++)scanf("%lf",&p[i]);
		ans=0;
		sou(1,0);
		printf("%.12f\n",ans);
	}
}
					
		
