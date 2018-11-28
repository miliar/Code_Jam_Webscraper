#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

typedef char STR[12];

STR str[30];
int f[100][30];
int n,m;
int bo[30];
int tot;
int ans1,ans2;

void build(int x,char *p){
	if ((*p)=='\0') return ;
	//printf("%d %d----\n",x,(*p)-'a');
	int c=f[x][(*p)-'A'];
	if (c==0) c=f[x][*p-'A']=++tot;
	build(c,p+1);
}

void dfs(int x){
	//printf("%d\n",x);
	if (x>n){
		int ans=0,flag=0;
		for (int i=1; i<=m; ++i){
			tot=0;
			memset(f,0,sizeof(f));
			for (int j=1; j<=n; ++j){
				if (bo[j]!=i) continue;
				build(0,str[j]);
				//printf("#%d %d\n",j,tot);
			}
			//printf("%d\n",tot);
			ans+=tot+1;
			if (tot==0) flag=1;
		}
		//cout<<"---"<<endl;
		if (flag) return ;
		if (ans>ans1) ans1=ans,ans2=1;
		else if (ans==ans1) ++ans2;
		return ;
	}
	for (int i=1; i<=m; ++i){
		bo[x]=i;
		dfs(x+1);
		bo[x]=0;
	}
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while (T--){
		scanf("%d%d",&n,&m);
		for (int i=1; i<=n; ++i)
			scanf("%s",str[i]);
		ans1=ans2=0;
		dfs(1);
		printf("Case #%d: %d %d\n",++ca,ans1,ans2);
	}
}
