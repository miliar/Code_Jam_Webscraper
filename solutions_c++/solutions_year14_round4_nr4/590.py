#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int a[2000000],b[2000000],next[200000][27];
int ss,tot,ans,anss,n,m,t;
char c[2000][2000];
void origin()
{
	for (int i=0;i<=ss;i++)
		for (int j=0;j<='Z'-'A';j++)
			next[i][j]=0;
	ss=m;
}
void ins(int s,char *c)
{
	int len=strlen(c);
	for (int i=0;i<len;i++) {
		int chr=c[i]-'A';
		if (!next[s][chr]) next[s][chr]=++ss,tot++;
		s=next[s][chr];
	}
}
int check()
{
	/*for (int i=1;i<=m;i++)
		if (!b[i]) return -1;*/
	origin();
	tot=0;
	for (int i=1;i<=n;i++) 
		ins(a[i],c[i]);
	for (int i=1;i<=m;i++)
		tot+=(b[i]!=0);
	return tot;
}
void dfs(int x)
{
	if (x>n) {
		int sum=check();
		//if (sum!=-1) cout<<sum<<' '<<ss<<endl;
		if (sum==ans) anss++;
		else if (sum>ans) 
			ans=sum,anss=1;
		return ;
	}
	for (int i=1;i<=m;i++) {
		a[x]=i,b[i]++;
		dfs(x+1);
		a[x]=0,b[i]--;
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int test=1;t;t--,test++) {
		printf("Case #%d: ",test);
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++) scanf("%s",c[i]);
		ans=0,anss=0;
		dfs(1);
		printf("%d %d\n",ans,anss);
	}
	return 0;
}
