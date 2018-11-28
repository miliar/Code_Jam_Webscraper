#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int ans,num,n,m,a[10],next[1000][30];
char s[10][20];
void check(){
	int tot=0,root;
	for(int i=1;i<=m;++i){
		root=++tot;
		memset(next,0,sizeof(next));
		bool ok=0;
		for(int j=1;j<=n;++j)
			if(a[j]==i){
				ok=1;
				int p=root;
				for(int k=0;k<strlen(s[j]);++k){
					if(!next[p][s[j][k]-'A'])
						next[p][s[j][k]-'A']=++tot;
					p=next[p][s[j][k]-'A'];
				}	
			}
		if(!ok)return;
	}
	if(tot>ans){
		ans=tot;
		num=1;
	}else if(tot==ans)++num;
}
void dfs(int xx){
	if(xx==n+1){
		check();
		return;
	}
	for(int i=1;i<=m;++i){
		a[xx]=i;
		dfs(xx+1);
	}
}
void work(int te){
	printf("Case #%d: ",te);
	ans=0;num=0;
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;++i)scanf("%s",s[i]);
	dfs(1);
	printf("%d %d\n",ans,num);
}
int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	for(int i=1;i<=tt;++i)work(i);
	return 0;
}
