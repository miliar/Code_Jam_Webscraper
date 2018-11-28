#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int T,n,S,a[101000];
bool use[101000];

int main()
{
	scanf("%d",&T);
	for (int testcase=1;testcase<=T;testcase++)
	{
		scanf("%d%d",&n,&S);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
		}
		sort(&a[1],&a[n+1]);
		int j=1;
		int ans=0;
		memset(use,false,sizeof(use));
		for (int i=n;i>=1;i--)
		{
			if (use[i]) break;
			if (a[i]+a[j]>S || j>=i) ans++;
			else
			{
				use[j]=true;
				j++;
				ans++;
			}
		}
		printf("Case #%d: %d\n",testcase,ans);
	}

	return 0;
}