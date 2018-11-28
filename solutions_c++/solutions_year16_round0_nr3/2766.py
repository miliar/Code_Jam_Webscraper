#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int T, n, j;
int a[18], prime[30002], top;
long long b[12];
int ans[12];

int work2(long long x)
{
	for (int i=1;prime[i]<x && i<=top;i++)
	if (x%prime[i]==0)
		return prime[i];
	return 0;
}
	
bool work()
{
	for (int k=2;k<=10;k++)
	{
		long long tt=1;
		b[k]=0;
		for (int i=n;i>=1;i--)
		{
			if (a[i])
				b[k]+=tt;
			tt*=k;
		}
		int x=work2(b[k]);
		if (x==0)
			return false;
		ans[k]=x;
	}
	return true;
		
}
void dfs(int x)
{
	if (j==0)
		return ;
		
	if (x==n)
	{
		if (work())
		{
			j--;
			for (int i=1;i<=n;i++)
				printf("%d",a[i]);
			for (int i=2;i<=10;i++)
				printf(" %d",ans[i]);
			printf("\n");
		}
		return ;
	}
	
	for (int i=0;i<=1;i++)
		a[x]=i, dfs(x+1);
}

bool check(int x)
{
	for (int j=2;j*j<=x;j++)
	if (x%j==0)
		return false;
	return true;
}
void getprime()
{
	for (int i=2;i<=65535;i++)
	if (check(i))
		prime[++top]=i;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	
	scanf("%d",&T);
	scanf("%d%d",&n, &j);
	
	printf("Case #1:\n");
	getprime();
	a[1]=1, a[n]=1;
	dfs(2);
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}





