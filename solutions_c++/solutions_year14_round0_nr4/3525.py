#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <string>
using namespace std;
int t;

void solve()
{
	int n;
	vector<double> a, b;
	vector<int> used;
	cin >> n;
	a.resize(n);
	b.resize(n);
	used.assign(n, false);
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	for (int i = 0; i < n; ++i)
		cin >> b[i];

	sort(a.begin(), a.end());
	sort(b.begin(), b.end());

	int maxa = -1;
	for (int j = 0; j < n; ++j)
	{
		int curans = 0;
		for (int i = j; i < n; ++i)
			curans += a[i] > b[i - j];
		maxa = max(maxa, curans);
	}

	cout << maxa << " ";	

	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());

	int l = 0;
	for (int i = 0; i < n; ++i)
	{
		bool found = false;
		int j;
		for (j = n - 1; j >= 0; --j)
		{
			if (!used[j] && b[j] > a[i])
			{
				found = true;
				break;
			}
		}
		if (found)
		{
			used[j] = true;
		}
		else
		{
			j = n - 1;
			while (used[j]) --j;
			used[j] = true;
			++l;
		}
	}

	cout << l << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}