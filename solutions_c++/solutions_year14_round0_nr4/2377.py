#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
#define mid ((l+r)>>1)
const long long INF = 1e9 + 7;

int getans(vector<double> a, vector<double> b)
{
	int l1, l2, r1, r2;
	l1 = l2 = 0;
	r1 = r2 = b.size() - 1;
	int ans = 0;
	while (l1 <= r1 && l2 <= r2)
	{
		if (a[l1] < b[l2])
		{
			l1++;
			r2--;
			continue;
		}
		if (a[l1] > b[l2])
		{
			l1++;
			l2++;
			ans++;
		}
	}
	return ans;
}
int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int ncase;
	cin >> ncase;
	vector<double> a, b;
	int ks = 1;
	while (ncase--)
	{
		a.clear();
		b.clear();
		int n;
		cin >> n;
		a.resize(n);
		b.resize(n);
		for (int i = 0; i < n; i++) cin >> a[i];
		for (int j = 0; j < n; j++) cin >> b[j];
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		printf("Case #%d: %d %d\n", ks++, getans(a, b), n - getans(b, a));
	}
	return 0;
}