#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

vector<int> a, b, c;

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cout << "Case #" << tt << ": ";
		int n;
		cin >> n;
		vector<pair<int, int> > a(n);
		vector<int> p(n);
		for (int i = 0; i < n; i++)
			cin >> p[i], a[i] = {p[i], i};
		sort(a.begin(), a.end());
		for (int i = 0; i < n; i++)
			p[i] = a[i].second; //, cerr << p[i] << " ";
			 
		vector<vector<int> > d(n + 1, vector<int>(n + 1));
		vector<int> inv(n);
		
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				inv[i] += p[j] < p[i];
		int ans = n * n;

		for (int i = 0; i <= n; i++)
			for (int j = 0; i + j <= n; j++)
			{
				int k = i + j - 1;
				if (i + j == 0) continue;
				d[i][j] = n * n * n;
				if (i) d[i][j] = min(d[i][j], d[i-1][j] + inv[k]);
				if (j) d[i][j] = min(d[i][j], d[i][j-1] + n - i -j -inv[k]);
				if (i + j == n) ans = min(ans, d[i][j]);
			}   
	   cout << ans << "\n";
	}
}

