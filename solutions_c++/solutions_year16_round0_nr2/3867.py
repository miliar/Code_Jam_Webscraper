#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;
typedef long long int64;
#define rep(x, n) for (int x = 1; x <= n; ++x)
#define zrp(x, n) for (int x = n; x; --x)
#define FOR(x, l, r) for (int x = l; x <= r; ++x)
#define foredge(i, x) for (int i = start[x]; i; i = e[i].l)
struct edge{int a, l;};
char s[2000];

int main()
{
	int t, ca;
	scanf("%d", &ca);
	rep(t, ca)
	{
		scanf("%s", s + 1);
		int l = 0;
		l = strlen(s + 1);
		int ans = 1;
		FOR(i, 2, l)
		{
			if (s[i] != s[i - 1])
				++ans;
		}
		if (s[l] == '+') --ans;
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
