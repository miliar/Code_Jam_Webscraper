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

void solve()
{
	long long n;
	cin >> n;
	if (n == 0)
	{
		cout << "INSOMNIA";
		return;
	}

	set<int> ds;
	int i = 1;
	while (true)
	{
		long long x = n * i;
		while (x > 0)
		{
			ds.insert(x % 10);
			x /= 10;
		}

		if (ds.size() == 10)
		{
			cout << n * i;
			return;
		}

		i++;
	}
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << t << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}
}