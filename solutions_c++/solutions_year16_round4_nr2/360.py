#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long
#define double long double

const int N = 200 + 23;
double a[N], f[N][N], g[N][N];

double go(vector <double>& p)
{
	int k = p.size();
	for (int i = 0; i <= k / 2; i++)
		for (int j = 0; j <= k / 2; j++)
			f[i][j] = 0;

	f[1][0] = p[0], f[0][1] = 1 - p[0];
	for (int pos = 1; pos < k; pos++)
	{
		for (int i = 0; i <= k / 2; i++)
			for (int j = 0; j <= k / 2; j++)
				g[i][j] = 0;

		for (int i = 0; i <= k / 2; i++)
			for (int j = 0; j <= k / 2; j++)
			{
				if (i + 1 <= k / 2)
					g[i + 1][j] += f[i][j] * p[pos];
				if (j + 1 <= k / 2)
					g[i][j + 1] += f[i][j] * (1 - p[pos]);
			}

		for (int i = 0; i <= k / 2; i++)
			for (int j = 0; j <= k / 2; j++)
				f[i][j] = g[i][j];
	}
	return f[k / 2][k / 2];
}

double sol(int n, int k)
{
	double ret = 0;
	for (int i = 0; i <= k; i++)
	{
		vector <double> p;
		int cur = 0, ru = 0;
		while (cur < i)
		{
			p.push_back(a[ru++]);
			cur++;
		}
		ru = n - 1;
		while (cur < k)
		{
			p.push_back(a[ru--]);
			cur++;
		}
		ret = max(ret, go(p));
	}
	return ret;
}

#undef int
int main()
{
#define int long long
	int t; cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cerr << "Executing Case #" << tt << "\n";

		int n, k; cin >> n >> k;
		for (int i = 0; i < n; i++) cin >> a[i];
		sort(a, a + n);
		cout << fixed << setprecision(20);
		cout << "Case #" << tt << ": " << sol(n, k) << "\n";
	}
	return 0;
}
