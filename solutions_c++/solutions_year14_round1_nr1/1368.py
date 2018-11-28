#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<string>
#include<iostream>
using namespace std;
string a[155],b[155],e[155],f[155];
int c[45],d[45],n,m,flag,ans,p;
void change(int x,int y){
	if(y==1){
		for(int i=1;i<=n;i++){
			if(a[i][x]=='1') e[i][x]='0';
			else e[i][x]='1';
		}
	}
	else{
		for(int i=1;i<=n;i++){
			e[i][x]=a[i][x];
		}
	}
}
void add(int x,int y){
	if(y==1){
		for(int i=1;i<=n;i++){
			if(a[i][x]=='1') e[i]+='0';
			else e[i]+='1';
		}
	}
	else{
		for(int i=1;i<=n;i++){
			e[i]+=a[i][x];
		}
	}
}
bool pipei(int x){
	for(int i=1;i<=n;i++){
		f[i]=e[i];
	}
	sort(f+1,f+n+1);
	for(int i=1;i<=n;i++){
		for(int j=0;j<=x;j++){
			if(f[i][j]!=b[i][j]) return 0;
		}
	}
	return 1;
}
void dfs(int x,int t){
	if(flag) return;
	if(x==m){
		ans=min(ans,t);
		return;
	}
	if(c[x]==d[x] && c[x]*2==n){
		p=min(x,p);
		add(x,0);
		if(pipei(x)){
			dfs(x+1,t);
		}
		else{
			change(x,1);
			if(pipei(x)){
				dfs(x+1,t+1);
			}
			else flag=1;
		}
	}
	else if(c[x]==d[x]){
		add(x,0);
		if(pipei(x)){
			dfs(x+1,t);
		}
		else flag=1;
	}
	else if(n-c[x]==d[x]){
		add(x,1);
		if(pipei(x)){
			dfs(x+1,t+1);
		}
		else flag=1;
	}
	else flag=1;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,T,vcase=0;
	scanf("%d",&T);
	while(T--){
		p=999999999;
		flag=0;
		ans=999999999;
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++){
			e[i].clear();
			f[i].clear();
		}
		for(i=0;i<m;i++){
			c[i]=0;
			d[i]=0;
		}
		for(i=1;i<=n;i++){
			cin>>a[i];
			for(j=0;j<m;j++){
				if(a[i][j]=='1') c[j]++;
			}
		}
		for(i=1;i<=n;i++){
			cin>>b[i];
			for(j=0;j<m;j++){
				if(b[i][j]=='1') d[j]++;
			}
		}
		sort(b+1,b+n+1);
		dfs(0,0);
		if(p!=999999999){
			for(i=1;i<=n;i++){
				e[i].clear();
				f[i].clear();
			}
			flag=0;
			for(i=1;i<=n;i++){
				if(a[i][p]=='1') a[i][p]='0';
				else a[i][p]='1';
			}
			dfs(0,1);
		}
		if(ans==999999999){
			printf("Case #%d: NOT POSSIBLE\n",++vcase);
		}
		else{
			printf("Case #%d: %d\n",++vcase,ans);
		}
	}
	return 0;
}