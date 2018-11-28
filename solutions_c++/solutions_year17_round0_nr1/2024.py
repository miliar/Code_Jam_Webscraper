#define _author "zys"
#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>

#include<iostream>
#include<queue>
#include<stack>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<algorithm>
#define mem(a, x) mesmet(a, x, sizeof(a))
using namespace std;

typedef long long ll;
typedef long long LL;
typedef unsigned long long ull;
typedef unsigned int ui;

typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;
typedef pair<string, int> Psi;

const int INF = 0x3fffffff;
const double eps = 1e-6;
const int mod = 1000000007;
const double pi = acos(-1.0);

const int maxn = (int)1e3 + 5;

int k, len, res;
char str[maxn];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int Case = 1;
	for (T, scanf("%d", &T); T; T--)
	{
		scanf("%s %d", str, &k);
		res = 0;
		int len = strlen(str);
		for (int i = 0; i <= len - k; i++)
		{
			if (str[i] == '-')
			{
				for (int j = 0; j < k; j++)
				{
					if (str[i + j] == '-')str[i + j] = '+';
					else str[i + j] = '-';
				}
				res++;
			}
		}
		bool flag = 1;
		for (int i = 0; i < len; i++)
			if (str[i] == '-')flag = 0;
		printf("Case #%d: ", Case++);
		if (flag)printf("%d\n", res);
		else printf("IMPOSSIBLE\n");
	}

	return 0;
}