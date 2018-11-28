#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
using namespace std;
typedef long long LL;
int f[35];
int ans[20],cnt;
LL isprime(LL k)
{
	for(LL i=2;i*i<=k;++i)
		if(k%i==0) return i;
	return 0;
}
void solve()
{
	for(int i=2;i<=10;++i)
	{
		LL num=0,k=1;
		for(int j=16;j>=1;--j)
		{
			num+=f[j]*k;
			k*=i;
		}
		LL x=isprime(num);
		if(!x) return;
		ans[i]=x;
	}
	++cnt;
	for(int i=1;i<=16;++i) printf("%d",f[i]);
	for(int i=2;i<=10;++i) printf(" %d",ans[i]);
	printf("\n");
	if(cnt==50) exit(0);
	return;
}
void DFS(int i)
{
	if(i==16)
	{
		solve();
		return ;
	}
	f[i]=0;
	DFS(i+1);
	f[i]=1;
	DFS(i+1);
	return;
}
int main()
{
	int a,b,c;
	cin>>a>>b>>c;
	f[16]=1;
	f[1]=1;
	printf("Case #1:\n");
	DFS(2);
	return 0;
}