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

const int N = 2005;
int fr[N];
int n;

int mx[N];

void solve()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> fr[i];
		fr[i]--;
		mx[i] = 0;
	}

	int ans = 0;

	//loops
	for (int i = 0; i < n; i++)
	{
		set<int> v;
		int cur = fr[i];

		while (true)
		{
			if (v.count(cur))
				break;
			if (cur == i)
			{
				ans = max(ans, (int)v.size() + 1);
				break;
			}

			v.insert(cur);
			cur = fr[cur];
		}
	}

	//parts
	for (int i = 0; i < n; i++)
	{
		set<int> v;
		v.insert(i);
		int cur = fr[i];

		while (true)
		{
			if (v.count(cur))
				break;

			v.insert(cur);
			if (v.count(fr[cur]) == 0)
				mx[cur] = max(mx[cur], (int)v.size() - 1);
			cur = fr[cur];
		}
	}

	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		int j = fr[i];
		if (fr[j] != i || i > j)
			continue;

		sum += 2 + mx[i] + mx[j];
	}
	ans = max(ans, sum);

	cout << ans;
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
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << t << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}
}