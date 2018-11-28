#include<cstdio>
#include<iostream>
using namespace std;
int n,m,ans,ok,T,a[1010][1010];
char s[1010][1010];
int value[200];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	value['<']=1;value['>']=2;
	value['^']=4;value['v']=8;
	for(int test=1;test<=T;++test){
		scanf("%d%d",&n,&m);
		ok=1;ans=0;
		memset(a,0,sizeof(a));
		for(int i=1;i<=n;++i)
			scanf("%s",s[i]+1);
		for(int i=1;i<=n;++i){
			int now=1;
			while(s[i][now]=='.')++now;
			a[i][now]|=1;
			now=m;
			while(s[i][now]=='.')--now;
			a[i][now]|=2;
		}
		for(int i=1;i<=m;++i){
			int now=1;
			while(s[now][i]=='.')++now;
			a[now][i]|=4;
			now=n;
			while(s[now][i]=='.')--now;
			a[now][i]|=8;
		}
		for(int i=1;i<=n;++i)
			for(int j=1;j<=m;++j)
				if(a[i][j]==15)ok=0;
				else
					if(a[i][j] & value[s[i][j]])++ans;
		printf("Case #%d: ",test); 
		if(ok)printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
} 
