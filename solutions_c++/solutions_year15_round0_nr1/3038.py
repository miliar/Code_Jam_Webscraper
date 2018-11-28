#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <map>
#define clr(a,b)	memset(a,b,sizeof(a))
using namespace std;

typedef long long LL;

int T;
char s[1111];
int smax;

int main()
{
	freopen("A-large.in","r", stdin);
	freopen("out", "w", stdout);

	int cas = 1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%s", &smax, s);
		int cur = 0, ans = 0;

		for(int i=0; i<=smax; i++)
		{
			int a = s[i] - '0';
			if(a == 0)	continue;

			if(cur >= i)
				cur += a;
			else
			{
				int d = i - cur;
				ans += d;
				cur = cur + d + a;
			}
		}
		printf("Case #%d: %d\n", cas++, ans);
	}




    return 0;
}
