#include <bits/stdc++.h>

using namespace std;

double prob[300];
int n, k;

int main()
{
	cout.precision(20);
	int T;
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		cin >> n >> k;
		for (int i = 0; i < n; i++) cin >> prob[i];
		double best = 0;
		for (unsigned int i = 0; i < (1u<<n); i++)
		{
			if (__builtin_popcount(i) != k) continue;
			double cura = 0;
			vector<double> cur;
			for (int j = 0; j < n; j++)
				if ((1<<j) & i) cur.push_back(prob[j]);
			for (unsigned int j = 0; j < (1u<<k); j++)
			{
				if (__builtin_popcount(j) != k/2) continue;
				double b = 1;
				for (int l = 0; l < k; l++)
				{
					if ((1<<l) & j) b *= cur[l];
					else b *= 1-cur[l];
				}
				cura += b;
			}
			best = max(best, cura);
		}
		cout << fixed << "Case #" << C << ": " << best << '\n';
	}
	return 0;
}

