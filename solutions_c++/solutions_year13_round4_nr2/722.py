#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

long long m, p;
int n;

int main()
{
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		cin >> n >> p;
		long long hzero = 0, bp = p;
		//--p;
		for (hzero = n; p != 0 && hzero >= 0; hzero--)
		{
			p >>= 1;
		}
		long long x = 1LL << (n - 1);
		int h2 = 0;
		p = bp;
		//p -= 1;
		for (long long s = 0; s < p && x != 0; )
		{
			s += x;
			++h2;
			if (s >= p)
				break;
			x >>= 1;
			//cout << s << ' ' << x << endl;
		}
		++hzero;
		if (x != 0) --h2;
		long long m = 1LL << n;
		//m -= 1;
		//cout << h2 << endl;
		//cout << hzero << endl;
		printf("Case #%d: ", tt);
		long long ans1 = (1LL << (h2 + 1)) - 2;
		if (ans1 >= m) ans1 = m - 1;
		cout << ans1 << ' ' << m - (1LL << hzero) << endl;
	}
	return 0;
}
