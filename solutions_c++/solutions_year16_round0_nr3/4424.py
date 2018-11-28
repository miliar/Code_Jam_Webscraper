//be naame khodaa

#include <bits/stdc++.h>

using namespace std;

long long a[20];

long long prime(long long n)
{
	if (n == 1) return -1;
	for (long long x = 2; x*x <= n; x++)
		if (n%x == 0)
			return x;
	return -1;
}

int main()
{
	int n = 16, J = 50, cnt = 0;
	cout << "Case #" << 1 << ":\n";
	for (int i = 0; i < (1 << n); i++)
	{
		if (((i >> 0)&1) == 0) continue;
		if (((i >> (n-1))&1) == 0) continue;
		bool ok = true;
		for (int b = 2; b <= 10; b++)
		{
			long long cur = 0;
			for (int j = 0; j < n; j++)
			{
				cur *= b;
				if ((i >> j)&1)
					cur++;
			}
			a[b] = prime(cur);
			if (a[b] == -1)
			{
				ok = false;
				break;
			}
		}
		if (ok)
		{
			for (int j = 0; j < n; j++)
				cout << ((i >> j)&1);
			for (int b = 2; b <= 10; b++)
				cout << ' ' << a[b];
			cout << endl;
			cnt++;
			if (cnt == J) break;
		}
	}
	return 0;
}
