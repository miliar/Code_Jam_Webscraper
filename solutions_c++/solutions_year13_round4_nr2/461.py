#include <iostream>
#include <cstring>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

int n;
long long p, m;

bool ok(long long x)
{
	long long r = 1;
	for (int i = 0; i < n; ++i)
	{
		if (x == 0) {
			r = 1;
			for (int j = i; j < n; ++j)
				r *= 2;
			break;
		}
		x = (x - 1) / 2;
	}
	return m - r + 1 <= p;
}
bool ok2(long long x)
{
	long long r = 1;
	x = m - x - 1;
	for (int i = 0; i < n; ++i)
	{
		if (x == 0) {
			r = 1;
			for (int j = 0; j < n - i; ++j)
				r *= 2;
			break;
		}
		x = (x - 1) / 2;
	}
	return r <= p;
}
int main()
{
	int cases;
	cin >> cases;
	for (int tcase = 1; tcase <= cases; ++tcase) {
		cin >> n >> p;
		m = 1; for (int i = 0; i < n; ++i) m *= 2;
		long long f = 0, r = m - 1;
		while (f < r)
		{
			long long mid = (f + r + 1) / 2;
			if (ok(mid)) f = mid;
				else r = mid - 1;	
		}
		cout << "Case #" << tcase << ": " << f << " " ;
		f = 0, r = m - 1;
		while (f < r)
		{
			long long mid = (f + r + 1) / 2;
			if (ok2(mid)) f = mid;
				else r = mid - 1;	
		}
		cout << f << endl;
	}
	return 0;
}
