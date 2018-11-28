#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <functional>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <iostream>

#define ENP     printf("**Entry Point**\n")
#define A       first
#define B       second
#define MP      make_pair

using namespace std;

typedef long long ll;

const int INF = 0x60000000;
const int MINF = -1000000000;
const ll mod = 1000000007;
const int cons = 50000001;
const double pi = 3.141592653589793;

ll dat[1000001];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	memset(dat, -1, sizeof(dat));

	for (int i = 1; i <= 1000000; i++)
	{
		int chk = 0;

		ll tmp = (ll)i;
		int cnt = 1;
		while (1)
		{
			tmp = (ll)i*cnt;
			while (tmp)
			{
				int t = (int)(tmp % 10LL);
				chk |= 1 << t;
				tmp /= 10;
			}

			if (chk == (1 << 10) - 1)break;
			cnt++;
		}

		dat[i] = (ll)cnt*i;
	}

	int testCases;
	scanf("%d", &testCases);

	for (int testNum = 1; testNum <= testCases; testNum++)
	{
		printf("Case #%d: ", testNum);
		int x;
		scanf("%d", &x);
		if (dat[x] == -1)
		{
			puts("INSOMNIA");
		}
		else
		{
			printf("%lld\n", dat[x]);
		}
	}

	return 0;
}