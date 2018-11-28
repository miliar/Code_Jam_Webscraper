#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <map>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, pll> tll;

// globals starts here

int k, n;
vector<double> p;

bool next_combination(vector<int> & a, int n) {
	int k = (int)a.size();
	for (int i = k - 1; i >= 0; --i)
		if (a[i] < n - k + i + 1) {
			++a[i];
			for (int j = i + 1; j < k; ++j)
				a[j] = a[j - 1] + 1;
			return true;
		}
	return false;
}

double tieprob(const vector<double> &probs)
{
	vector<int> yes;
	for (int i = 0; i < probs.size() / 2; ++i)
	{
		yes.push_back(i + 1);
	}

	double ans = 0;

	do
	{
		double mul = 1;
		vector<bool> good(probs.size());
		for (int i = 0; i < yes.size(); ++i)
		{
			good[yes[i] - 1] = true;
		}

		for (int i = 0; i < probs.size(); ++i)
		{
			if (good[i])
			{
				mul *= probs[i];
			}
			else
			{
				mul *= (1 - probs[i]);
			}
		}

		ans += mul;

	} while (next_combination(yes, probs.size()));

	return ans;
}

double tiegood(const vector<double> &probs)
{
	vector<double> g(probs.size(), 0);
	g[0] = 1;

	for (int i = 0; i < probs.size(); ++i)
	{
		vector<double> d(probs.size(), 0);

		for (int j = 0; j < probs.size(); ++j)
		{
			if (j)
			{
				d[j] += probs[i] * g[j - 1];
			}
			d[j] += (1 - probs[i]) * g[j];
		}

		g = d;
	}

	return g[probs.size() / 2];
}

double solve()
{
	sort(p.begin(), p.end());

	double best = 0;

	for (int i = 0; i <= k; ++i)
	{
		vector<double> probs;
		for (int j = 0; j < i; ++j)
		{
			probs.push_back(p[j]);
		}
		for (int j = i; j < k; ++j)
		{
			probs.push_back(p[n - 1 - (j - i)]);
		}

		double res = tiegood(probs);
		best = max(best, res);
	}

	return best;
}

double solvestupid()
{
	vector<int> combi;
	for (int i = 0; i < k; ++i)
	{
		combi.push_back(i + 1);
	}

	double best = 0;

	vector<int> bestc;

	do
	{
		vector<double> probs;
		for (int i = 0; i < k; ++i)
		{
			probs.push_back(p[combi[i] - 1]);
		}

		double tie = tieprob(probs);
		if (tie > best)
		{
			best = tie;
			bestc = combi;
		}

	} while (next_combination(combi, n));

	cout << "n = " << n << "; ";
	for (int x : bestc)
	{
		cout << x << " ";
	}

	return best;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tests;
	cin >> tests;

	for (int tc = 1; tc <= tests; ++tc)
	{
		cin >> n >> k;
		p.clear();
		for (int i = 0; i < n; ++i)
		{
			double x;
			cin >> x;
			p.push_back(x);
		}

		double ans2 = solve();
		/*double ans = solvestupid();

		if (fabs(ans - ans2) > 1e-7)
		{
			cout << "WARN!" << endl;
			cout << ans << endl << ans2 << endl;
		}*/

		printf("Case #%d: %.8lf\n", tc, ans2);
	}

	return 0;
}