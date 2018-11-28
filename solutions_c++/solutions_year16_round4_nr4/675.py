#include<bits/stdc++.h>
using namespace std;
const int maxn=210;
int a[maxn][maxn],ans,v[maxn],cho[maxn],p[maxn],q[maxn];
int n,nk,T;

char s[maxn];
int have[maxn];
bool  dfs(int dep){
	if(dep>n) {
		//for(int i=1;i<=n;i++)cerr<<cho[i]<<" ";cerr<<endl;
		return true;
	}
	bool ok=false;
	for(int i=1;i<=n;i++)if(a[q[dep]][i] && v[i]){
		v[i]=0;
		cho[q[dep]]=i;
		if(dfs(dep+1)==false){
			v[i]=1;
			 return false; 
		}else ok=true;
		v[i]=1;
		
	}
	return ok;
}
bool work(int dep){
	if(dep>n){
		return dfs(1);
	}
	for(int i=1;i<=n;i++) if(p[i]){
		p[i]=0;
		q[dep]=i;
		if(work(dep+1)==false) {
			p[i]=1;
			return false;
		}
		p[i]=1;
	}
	return true;
}
void sou(int x,int y,int z){
	//cerr<<x<<" "<<y<<" "<<z<<" "<<a[x][y]<<endl;
	if(z>=ans) return;
	if(x>n) {
		//cerr<<"z="<<z<<endl;
		if(work(1) && ans>z) {
			ans=z;
		/*	for(int i=1;i<=n;i++){
				for(int j=1;j<=n;j++)cout<<a[i][j];
				cout<<endl;
			}*/
		}
		return;
	}
	if(y>n){
		sou(x+1,1,z);
		return;
	}
	if(a[x][y]==1){
		sou(x,y+1,z);
	}
	else{
		a[x][y]=1;
		sou(x,y+1,z+1);
		a[x][y]=0;
		sou(x,y+1,z);
	}
}
	
int main(){
	freopen("t.in","r",stdin);
	freopen("t.out","w",stdout);
	scanf("%d",&T);
	for(int ti=1;ti<=T;ti++){
		printf("Case #%d: ",ti);
		scanf("%d",&n);
		for(int i=1;i<=n;i++){
			scanf("%s",s+1);
			for(int j=1;j<=n;j++) a[i][j]=s[j]-'0';
		}
		for(int i=1;i<=n;i++)v[i]=1,p[i]=1;
		ans=10000000;
		sou(1,1,0);
		cout<<ans<<endl;
	}
}
					
		
