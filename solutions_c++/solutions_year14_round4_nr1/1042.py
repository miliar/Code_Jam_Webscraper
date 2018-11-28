#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cout << "Case #" << tt << ": ";
		int n, x;
		cin >> n >> x;
		vector<int> a(n);
		for (int i = 0; i < n; i++)
			cin >> a[i];
		sort(a.begin(), a.end());
		vector<bool> used(n);
		int ans = 0;
		for (int i = n - 1; i >=0; i--)
		{
			if (used[i]) continue;
			ans++;
			int cur = x - a[i];
			used[i] = true;
			for (int j = i - 1; j >= 0; j--)
				if (!used[j] && cur >= a[j])
				{
					used[j] = true;
					break;
				} 
		}
		cout << ans << "\n";
	}
}