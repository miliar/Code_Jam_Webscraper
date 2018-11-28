#include<bits/stdc++.h>
#define N 1010
using namespace std;
int f[N],x[N],y[N],z[N];
pair<int,int> p[N*N];
int find(int x){
	if(f[x]==x) return x;
	return f[x]=find(f[x]);
}
void uni(int x,int y){
	int fx=find(x),fy=find(y);
	if(fx!=fy) f[fx]=fy;
}
inline int sq(int a){
	return a*a;
}
int dis(int a,int b){
	return sq(x[a]-x[b])+sq(y[a]-y[b])+sq(z[a]-z[b]);
}
bool cmp(pair<int,int> a,pair<int,int> b){
	return dis(a.first,a.second)<dis(b.first,b.second);
}
int main(){
	int T,g;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		int n,now=0;
		double ans=0;
		scanf("%d%d",&n,&g);
		for(int i=0;i<n;i++) scanf("%d%d%d%d%d%d",&x[i],&y[i],&z[i],&g,&g,&g),f[i]=i;
		for(int i=0;i<n*n;i++) p[i].first=i/n,p[i].second=i%n;
		sort(p,p+n*n,cmp);
		while(find(0)!=find(1)){
			uni(p[now].first,p[now].second);
			ans=sqrt(dis(p[now].first,p[now].second));
			now++;
		}
		printf("Case #%d: %.12f\n",cs,ans);
	}
	return 0;
}
