#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
FILE *of;
char w[111][111];
int i,j,k,n,m,p[1111],len[111],a1,a2,tests,cc,t[1111][31],tot;
void ins(int x){
	int p,i;
	for (p=1,i=0;i<len[x];i++){
		if (!t[p][w[x][i]-'A']) t[p][w[x][i]-'A']=++tot,memset(t[tot],0,sizeof(t[tot]));
		p=t[p][w[x][i]-'A'];
	}
}
void check(){
	int res=0,i,j;
	for (i=1;i<=m;i++){
		tot=1;memset(t[1],0,sizeof(t[1]));
		for (j=1;j<=n;j++)
		 if (p[j]==i) ins(j);
		if (tot==1) return;
		res+=tot;
	}
	if (res>a1) a1=res,a2=1;else if (res==a1) a2++;
}
void dfs(int x){
	int i;
	if (x>n){
		check();return;
	}
	for (i=1;i<=m;i++){
		p[x]=i;dfs(x+1);
	}
}
int main(){
	scanf("%d",&tests);of=fopen("DS0bf.out","w");
	for (cc=1;cc<=tests;cc++){
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;i++) scanf("%s",w[i]),len[i]=strlen(w[i]);
		a1=0;dfs(1);
		fprintf(of,"Case #%d: %d %d\n",cc,a1,a2);
		printf("%d\n",cc);
	}
	return 0;
}
