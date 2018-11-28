#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int N = 1005;
char s[N];
int n;

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d%s", &n, s);
		int t = 0, ans = 0;
		for (int i = 0; i <= n; i ++)
		{
			ans = max(ans, i-t);
			t += s[i]-'0';
		}
		printf("Case #%d: %d\n", ++ cas, ans);
	}
	return 0;
}
