#include<bits/stdc++.h>
using namespace std;

#define MAX 1005

int t, n;
char s[MAX];

int main()
{
	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		scanf("%d %s ", &n, s);

		int sol = 0, cnt = 0;
		for(int i=0; i<=n; ++i)
		{
			int a = s[i] - '0';
			if(a != 0)
			{
				if(i > cnt) sol += i-cnt, cnt = i;
				cnt += a;
			}
		}
		
		printf("Case #%d: %d\n", tc, sol);
	}

	return 0;
}
