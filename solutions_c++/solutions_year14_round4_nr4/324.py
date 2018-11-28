#include<cstdio>
#include<cstring>
using namespace std;
int n,m,l[10],t[1000][27],tot,ans,num,a[10],TT,T,i;
char s[10][100];
void insert(int rt,int x){
	for(int i=0;i<l[x];i++){
		if(t[rt][s[x][i]-'A']==0){
			t[rt][s[x][i]-'A']=++tot;
		}
		rt=t[rt][s[x][i]-'A'];
	}
}
void solve(){
	int i,j;
	tot=m;memset(t,0,sizeof(t));
	for(i=1;i<=n;i++){
		insert(a[i],i);
	}
	for(i=1;i<=m;i++){
		for(j=1;j<=n;j++)if(a[j]==i)break;
		if(j>n)tot--;
	}
	if(tot==ans)num++;
	if(tot>ans)ans=tot,num=1;
}
void dfs(int v){
	if(v>n){
		solve();return;
	}
	for(int i=1;i<=m;i++){
		a[v]=i;dfs(v+1);
	}
}
int main(){
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&TT);
	for(T=1;T<=TT;T++){
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++){
			scanf("%s",s[i]);
			l[i]=strlen(s[i]);
		}
		ans=0;num=0;
		dfs(1);
		printf("Case #%d: %d %d\n",T,ans,num);
	}
}