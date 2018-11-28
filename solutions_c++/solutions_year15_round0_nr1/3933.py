#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define DB(v) cerr << #v << ": " << v << endl

char s[1025];

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
		int n; cin >> n;
		cin >> s;
		int sum = 0, add = 0;
		forn(i, n + 1) 
		{
			int cnt = int(s[i] - '0');
			if (!cnt) continue;
			add += max(0, i - sum);
			sum += cnt + max(0, i - sum);
		}
		cout << "Case #" << t << ": " << add << '\n';
	}

#ifdef HOME
	//cout << "\nTime elapsed: " << clock() << '\n';
#endif
	return 0;
}
