#include <iostream>
#include <vector>
#include <string.h>
#include <string>
#include <algorithm>

using namespace std;

bool F(int n, long long p, long long k)
{
	if (n == 0)
		return k < p;
	if (k == 0 || p >= 1LL << n)
		return true;
	if (p <= (1LL << (n-1)))
		return false;
	long long x = k - 1;
	return F(n - 1, p - (1LL << (n-1)), x / 2);
}

long long G(int n, long long p, long long k)
{
	if (n == 0)
		return k < p;
	if (p >= 1LL << n)
		return true;
	if (k == (1LL << n) - 1)
		return false;
	if (p >= (1LL << (n-1)))
		return true;
	long long x = (1LL << n) - 1 - k - 1;
	return G(n - 1, p, (1LL << (n-1)) - x / 2 - 1);
}

int Work()
{
	int n;
	long long p;
	cin >> n >> p;
	long long m = 1LL << n;
	long long ll = 0, rr = m - 1, mid;
	while (ll < rr)
	{
		mid = (ll + rr + 1) >> 1;
		if (F(n, p, mid))  ll = mid;
		else rr = mid - 1;
	}
	cout << " " << ll;

	ll = 0; rr = m - 1;
	while (ll < rr)
	{
		mid = (ll + rr + 1) >> 1;
		if (G(n, p, mid))  ll = mid;
		else rr = mid - 1;
	}
	cout << " " << ll;
	return 0;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt ++)
	{
		cout << "Case #" << tt << ":";
		Work();
		cout << endl;
	}
	return 0;
}