#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define maxn 1080
int a[maxn];
char s[maxn];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas = 1;cas <= t;cas++)
	{
		int n;
		scanf("%d",&n);
		scanf("%s",s);
		for(int i = 0;i <= n;i++)
		{
			a[i] = s[i] - '0';
		}
		int ans = 0,sum = a[0];
		for(int i = 1;i <= n;i++)
		{
			if(a[i] && sum < i)
				ans = max(ans,i-sum);
			sum += a[i];
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}