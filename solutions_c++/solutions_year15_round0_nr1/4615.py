#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
#include <cstring>
#include <queue>
#include <map>
#include <cmath>
using namespace std;
int main()
{
	int t,n;
	int ans,tot;
	char str[1005];
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&n);
		scanf("%s",str);
		ans = 0;
		tot = 0;
		for(int j=0;j<=n;j++)
		{
			if(tot<j)
			{
				ans = ans + j - tot;
				tot = tot + j - tot;
			}
			tot = tot + (int)(str[j]-'0');
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}