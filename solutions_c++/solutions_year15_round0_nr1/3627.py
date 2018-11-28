#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef long double LD;

const int MX = 1e6 + 5;
int t, n;
LL res;
char a[MX];

int main()
{
	scanf("%d", &t);
	for(int i = 1; i <= t; ++ i)
	{
		res = 0;
		scanf("%d%s", &n, a);
		LL akt = 0;

		for(int j = 0; j < n+1; ++ j)
		{
			if(akt >= j)
				akt += a[j] - '0';
			else
			{
				res += j - akt;
				akt = j;
				akt += a[j] - '0';
			}
		}

		printf("Case #%d: %lld\n", i, res);
	}
	
	return 0;
}
