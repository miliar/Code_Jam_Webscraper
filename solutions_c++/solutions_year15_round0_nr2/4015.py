#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define fortodo(i,a,b) for (int i=(a);i<=(b);i++)
using namespace std;
const int maxn=100;
int a[maxn],T,n,ans;

inline void judge(){
	freopen("in.txt","r",stdin);
	freopen("std.txt","w",stdout);
}

inline void dfs(int n,int tick){
	if (tick>ans) return;
	bool flag=true;
	fortodo(i,1,n)
		if (a[i]!=0){
			flag=false;
			break;
		}
	if (flag){
		ans=min(ans,tick);
		return;
	}
	int b[maxn];
	fortodo(i,1,n) b[i]=a[i];
	fortodo(i,1,n) a[i]=max(a[i]-1,0);
	dfs(n,tick+1);
	fortodo(i,1,n) a[i]=b[i];
	int jl=1;
	fortodo(i,2,n) if (a[i]>a[jl]) jl=i;
	fortodo(i,1,a[jl]-1){
		a[n+1]=i;
		a[jl]-=i;
		dfs(n+1,tick+1);
		a[jl]=b[jl];
	}
}
int main(){
	judge();
	cin>>T;
	fortodo(p,1,T){
		cin>>n;
		fortodo(i,1,n) cin>>a[i];
		ans=1<<29;
		dfs(n,0);
		printf("Case #%d: %d\n",p,ans);
	}
	return 0;
}

