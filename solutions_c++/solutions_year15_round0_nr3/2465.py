#include <bits/stdc++.h>
using namespace std;
typedef long long i64;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define DB(v) cerr << #v << ": " << v << endl

int snxt[4][4] = {{0, 1, 2, 3},
				  {1, 4, 3, 6},
				  {2, 7, 4, 1},
				  {3, 2, 5, 4}};
int nxt[8][8];

int dig[256];
char s[400007];

int main()
{
	cin.tie(0); ios_base::sync_with_stdio(0);
#ifdef HOME
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	forn(i, 4) forn(j, 4)
	{
		nxt[i][j] = nxt[i + 4][j + 4] = snxt[i][j];
		nxt[i + 4][j] = nxt[i][j + 4] = (4 + snxt[i][j]) % 8;
	}
	dig['1'] = 0;
	dig['i'] = 1;
	dig['j'] = 2;
	dig['k'] = 3;

	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		i64 L, X;
		cin >> L >> X >> s;

		int each = 0;
		forn(i, L) 
		{
			s[i + L] = s[i + 2 * L] = s[i + 3 * L] = s[i];
			each = nxt[each][dig[s[i]]];
		}

		int cur = 0, iMinLen = 0, kMinLen = 0;
		forn(i, 4 * L)
		{
			cur = nxt[cur][dig[s[i]]];
			if (cur == 1)
			{
				iMinLen = i + 1;
				break;
			}
		}
		if (cur != 1)
		{
			cout << "Case #" << t << ": " << "NO\n";
			continue;
		}

		cur = 0;
		ford(i, 4 * L)
		{
			cur = nxt[dig[s[i]]][cur];
			if (cur == 3)
			{
				kMinLen = 4 * L - i;
				break;
			}
		}
		if (cur != 3)
		{
			cout << "Case #" << t << ": " << "NO\n";
			continue;
		}

		cur = 0;
		i64 i = iMinLen;
		for (; i < X * L - kMinLen && (i % L); ++i)
			cur = nxt[cur][dig[s[i % L]]];
		for (; i + L < X * L - kMinLen; i += L)
			cur = nxt[cur][each];
		for (; i < X * L - kMinLen; ++i)
			cur = nxt[cur][dig[s[i % L]]];

		//DB(iMinLen); DB(kMinLen);

		cout << "Case #" << t << ": " << (cur == 2 ? "YES" : "NO") << '\n';
	}

#ifdef HOME
	//cout << "\nTime elapsed: " << clock() << '\n';
#endif
	return 0;
}
