#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define XX first
#define YY second

const int MOD = 1e9 + 7;
const int INF = 1e9 + 9;
const int N = 200+ 7;

double p[N];

int main()
{
	ios::sync_with_stdio(false);
	cout << setprecision(12) << fixed;
	int __;
	cin >> __;
	for (int _=0; _<__; _++)
	{
		cout << "Case #" << _+1 << ": ";

		int n, k;
		cin >> n >> k;
		for (int i=0; i<n; i++)
			cin >> p[i];
		double ans = 0;
		for (int i=0; i<1<<n; i++)
		{
			int pc = __builtin_popcount(i);
			if (pc != k)
				continue;
			double po = 0;
			for (int j=0; j<1<<pc; j++)
				if (__builtin_popcount(j) == pc/2)
				{
					double P = 1;
					int pos = 0;
					for (int t = 0; t<n; t++)
						if ((i >> t) & 1)
						{
							if ((j >> pos) & 1)
								P *= p[t];
							else
								P *= 1 - p[t];
							pos++;
						}
					po += P;
				}
			ans = max(ans, po);
		}
		cout << ans << "\n";
	}

	return 0;
}
