#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#define N 5
using namespace std;
char p[N][N];
int hehe[N][N],nmb[N],v[N],used;
int test,n,ans;
bool dfs3(int dep)
{
	//cout<<dep<<endl;
	if (dep==n) return 1;
	bool ret=0;
	for (int i=0;i<n;i++)
	if (hehe[nmb[dep]][i])
	{
		ret=1;
		int temp[N];
		for (int j=0;j<n;j++) temp[j]=hehe[j][i];
		for (int j=0;j<n;j++) hehe[j][i]=0;
		if (!dfs3(dep+1)) return 0;
		for (int j=0;j<n;j++)  hehe[j][i]=temp[j];
	}
	return ret;
}
bool dfs2(int dep)
{
	if (dep==n)
	{
		return dfs3(0);
	}
	bool ret=1;
	for (int i=0;i<n;i++)
	if (!v[i]) 
	{
		nmb[dep]=i;
		v[i]=1;
		ret=ret&&dfs2(dep+1);
		v[i]=0;
	}
	return ret;
}
void dfs(int a,int b)
{
	if (a==n)
	{
	//	cout<<used<<endl;
	//	cout<<"1111"<<endl;
		if (used>=ans) return;
		for (int i=0;i<n;i++)
		for (int j=0;j<n;j++)
		hehe[i][j]=p[i][j]-'0';
		memset(v,0,sizeof(v));
		if (dfs2(0)) ans=used;
	}
	else if (b==n) dfs(a+1,0);
	else if (p[a][b]=='1')
	{
		dfs(a,b+1);
	}
	else 
	{
		p[a][b]='1';
		used++;
		dfs(a,b+1);
		used--;
		p[a][b]='0';
		dfs(a,b+1);
	}
	
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("41.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		printf("Case #%d: ",kk);
		cin>>n;
		ans=n*n;
		for (int i=0;i<n;i++)
		scanf("%s",p[i]);
		dfs(0,0);
		cout<<ans<<endl;
	}
	return 0;
}
