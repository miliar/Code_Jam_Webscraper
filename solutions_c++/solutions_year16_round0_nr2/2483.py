#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
const int N = 105;
char s[N];
int f[N][2];
int main()
{
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --)
	{
		scanf("%s", s + 1);
		int n = strlen(s + 1);
		f[0][0] = f[0][1] = 0;
		for (int i = 1; i <= n; ++ i)
		{
			f[i][0] = (s[i] == '+' ? f[i - 1][0] : f[i - 1][1] + 1);
			f[i][1] = (s[i] == '-' ? f[i - 1][1] : f[i - 1][0] + 1);
		}
		printf("Case #%d: %d\n", ++ zzz, f[n][0]);
	}
}

