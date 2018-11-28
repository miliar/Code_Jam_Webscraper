#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<time.h>
using namespace std;

long long div(long long x)
{
	for (long long i = 2; i <= 200; i ++)
		if (x % i == 0)
			return i;
	return -1;
}

bool ok(long long x)
{
	vector<long long> divs;
	for (long long b = 2; b <= 10; b++)
	{
		long long y = x;
		long long res = 0;
		long long pw = 1;
		while (y > 0)
		{
			res += pw * (y & 1);
			y >>= 1;
			pw *= b;
		}

		if (div(res) == -1)
			return 0;
		divs.push_back(div(res));
	}

	string t = "";
	while (x > 0)
	{
		t = (char)('0' + (x & 1)) + t;
		x >>= 1;
	}
	cout << t << " ";

	for (long long d : divs)
		cout << d << " ";
	cout << endl;
	return 1;
}

void solve()
{
	long long n, k;
	cin >> n >> k;

	long long done = 0;
	n--;
	for (long long x = (1 << n) + 1; ; x += 2)
	{
		done += ok(x);
		cerr << x << endl;
		if (done == k)
			return;
	}
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	long long T;
	cin >> T;
	for (long long t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ":\n";
		solve();
		cout << endl;
		cerr << t << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}
}