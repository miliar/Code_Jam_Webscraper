#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#define maxn 3010
using namespace std;
int ans,n,a[maxn];
void read()
{
	cin>>n;
	for(int i=1;i<=n;++i)
		cin>>a[i];
	ans=1<<30;
	int t=*max_element(a+1,a+n+1);
	for(int x=1;x<=t;++x)
	{
		int sum=0;
		for(int i=1;i<=n;++i)
			sum+=(a[i]-1)/x;
		ans=min(ans,sum+x);
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,C=0;
	for(cin>>T;T;--T)
	{
		read();
		printf("Case #%d: %d\n",++C,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
