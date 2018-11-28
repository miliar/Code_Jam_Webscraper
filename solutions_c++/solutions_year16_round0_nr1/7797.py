#include <bits/stdc++.h>
using namespace std;
int curr;
int get_length(int x)
{
	int ans=0;
	while(x)
	{
		x/=10;
		ans++;
	}
	return ans;
}
void check(long long x)
{
	while(x)
	{
		int tmp=x%10;
		curr=curr|(1<<tmp);
		x/=10;
	}
}
int main()
{
	freopen ("A.inp","r",stdin);
	freopen ("A.out","w",stdout);
	int test;
	int testcase;
	scanf("%d",&test);
	for(int testcase=1;testcase<=test;testcase++)
	{
		long long n,x=0;
		curr=0;
		scanf("%lld",&n);
		for(int i=1;i<=1000000;i++)
		{
			x+=n;
			check(x);
			if(curr==(1<<10)-1) break;
		}
		printf("Case #%d: ",testcase);
		if(curr==(1<<10)-1) printf("%lld\n",x);
		else printf("INSOMNIA\n");

	}
}