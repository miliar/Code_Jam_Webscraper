#include <bits/stdc++.h>
using namespace std;

const int MX = 1005;
int t, n, p[MX];

int suf(int a, int b)
{
	if(a % b == 0)
		return a / b;
	return 1 + a / b;
}

bool ok(int t)
{
	for(int s = 0; s < t; ++ s)
	{
		int usedSpecials = 0;
		for(int i = 0; i < n; ++ i)
		{
			int x = suf(p[i], t - s) - 1;
			usedSpecials += x;
		}
		if(usedSpecials <= s)
			return true;
	}
	return false;
}

int BS(int pocz, int konc)
{
	int sro = (pocz + konc) / 2;

	if(sro == pocz)
	{
		if(ok(pocz))
			return pocz;
		return konc;
	}

	if(ok(sro))
		return BS(pocz,sro);
	else
		return BS(sro+1,konc);
}

int main()
{
	scanf("%d", &t);
	for(int cases = 1; cases <= t; ++ cases)
	{
		scanf("%d", &n);
		for(int i = 0; i < n; ++ i)
			scanf("%d", &p[i]);

		printf("Case #%d: %d\n", cases, BS(0,1005));
	}
	return 0;
}
