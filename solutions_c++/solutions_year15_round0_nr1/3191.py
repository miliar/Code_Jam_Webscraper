#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>

using namespace std;

typedef long long LL;

char s[2000];
int T,n,dq,ans;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for (int z=1;z<=T;++z)
	{
		scanf("%d",&n);
		dq=0;
		ans=0;
		scanf("%s",s);
		for (int i=0;i<=n;++i)
		{
			if (dq>=i)
			{
				dq+=s[i]-'0';
			}
			else
			{
				ans+=i-dq;
				dq=i+s[i]-'0';
			}
		}
		printf("Case #%d: %d\n",z,ans);
	}	
	return 0;
}
