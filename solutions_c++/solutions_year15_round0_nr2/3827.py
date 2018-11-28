#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define DB(v) cerr << #v << ": " << v << endl

int p[1010];

int main()
{
	cin.tie(0); ios_base::sync_with_stdio(0);
#ifdef HOME
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		int d; cin >> d;
		forn(i, d)
			cin >> p[i];

		int ans = 1e9;
		ford(dmax, 1000) if (dmax)
		{
			int cur = dmax;
			forn(i, d)
				cur += (p[i] - 1) / dmax;
			ans = min(ans, cur);
		}
		cout << "Case #" << t << ": " << ans << '\n';
	}

#ifdef HOME
	//cout << "\nTime elapsed: " << clock() << '\n';
#endif
	return 0;
}
