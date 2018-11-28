#include<bits/stdc++.h>
using namespace std;
#define eb emplace_back
#define pb push_back
#define mp make_pair
const int md=1e9+7;
const int inf=1e9;
const int maxn=1234567;
int T,n,m,nq,ns,x;
struct node{
	int x,y,z;
}e[maxn];
int fa[maxn],a[maxn],b[maxn],c[maxn],d[maxn],va[maxn],vb[maxn],vc[maxn];
bool cmp(node a,node b){
	return a.z<b.z || (a.z==b.z && a.x<b.x)||(a.z==b.z && a.x==b.x && a.y<b.y);
}
int get(int x){
	if(x==fa[x]) return x;
	return fa[x]=get(fa[x]);
}
int sqr(int x){
	return x*x;
}
void task(){
	scanf("%d%d",&n,&ns);
	for(int i=1;i<=n;i++){
		scanf("%d%d%d%d%d%d",&a[i],&b[i],&c[i],&va[i],&vb[i],&vc[i]);
	}
	int num=0;
	for(int i=1;i<=n;i++){
		for(int j=i+1;j<=n;j++){
			e[++num].x=i;
			e[num].y=j;
			e[num].z=sqr(a[i]-a[j])+sqr(b[i]-b[j])+sqr(c[i]-c[j]);
		}
	}
	sort(e+1,e+num+1,cmp);
	for(int i=1;i<=n;i++)fa[i]=i;
	for(int i=1;i<=num;i++){
		int x=e[i].x,y=e[i].y,z=e[i].z;
		int fx=get(x),fy=get(y);
		if(fx!=fy){
			fa[fx]=fy;
			if(get(1)==get(2)){
				printf("%.8f\n",sqrt(e[i].z));
				return;
			}
		}
	}
}
int main(){		
	scanf("%d",&T);
	for(int ti=1;ti<=T;ti++){
		printf("Case #%d: ",ti);
		task();
	}
	
}
