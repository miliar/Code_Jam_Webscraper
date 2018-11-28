#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;
typedef long long LL;
#define For(i,a,b) for (int i = (a); i <= (b); i++)
#define Cor(i,a,b) for (int i = (a); i >= (b); i--)
#define rep(i,a) for (int i = 0; i < a; i++)
#define Fill(a,b) memset(a,b,sizeof(a))
char s[100000];
int main()
{
	freopen("t.in", "r", stdin);
	freopen("t.out", "w", stdout);
	int _;
	scanf("%d", &_);
	for (int t = 1; t <= _; t++)
	{
		int n, k;
		scanf("%s %d", s, &k);
		n = strlen(s);
		int ans = 0;
		for (int i = 0; i < n - k + 1; i++)
		{
			if (s[i] == '+')
				continue;
			for (int j = i; j < i + k; j++)
			{
				if (s[j] == '+')
					s[j] = '-';
				else
					s[j] = '+';
			}
			ans++;
		}
		bool vad = 1;
		for (int i = 0; i < n; i++)
			if (s[i] == '-')
			{
				vad = 0;
				break;
			}
		if (vad)
			printf("Case #%d: %d\n", t, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}
