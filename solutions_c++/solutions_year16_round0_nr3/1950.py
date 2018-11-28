#include <cstdio>
using namespace std;
typedef long long ll;

ll t, n, j;
ll arData[35];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("c_large_output.txt", "w+", stdout);
	scanf("%lld", &t);
	ll tc = 1;
	while (t--)
	{
		scanf("%lld%lld", &n, &j);
		printf("Case #%lld:\n", tc++);
		ll nData = 1;
		for (ll i = 1; i < n; ++i)
			nData <<= 1;
		nData |= 1;
		ll nCnt = 0;
		while (1)
		{
			if (nCnt == j)
				break;
			ll nTmp = 1;
			for (ll i = 1; i < n; ++i)
				nTmp = nTmp * (-1) + ((nData >> i) & 1);
			if (nTmp == 0)
			{
				for (ll i = 0; i < n; ++i)
					printf("%lld", (nData >> i) & 1);
				for (ll i = 2; i <= 10; ++i)
					printf(" %lld", i + 1);
				printf("\n");
				nCnt++;
			}
			nData += 2;
		}
	}
}