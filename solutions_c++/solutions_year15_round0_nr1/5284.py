#include <iostream>
#include <cstdio>

#define MAXN 1024

using namespace std;

int N;
char s[MAXN];

void read()
{
	scanf("%d", &N);
	scanf("%s", &s);
}

void solve()
{
	int ans = 0;
	int cnt = s[0] - '0';

	for(int i = 1; i <= N; i++)
	{
		int dig = s[i] - '0';
		
		if(i > cnt)
		{
			ans += (i - cnt);
			cnt = i;
		}

		cnt += dig;
	}

	printf("%d\n", ans);
}

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int test = 1; test <= T; test++)
	{
		read();
		printf("Case #%d: ", test);
		solve();
	}

	return 0;
}
