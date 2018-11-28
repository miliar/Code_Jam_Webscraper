//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 5;
typedef long long ll;

bool g[N][N], g2[N][N];

int main()
{
	int _t = in();
	for(int t = 1; t <= _t; t++)
	{
		cout << "Case #" << t << ": ";
		int n = in();
		string s;
		for(int i = 0; i < n; i++)
		{
			cin >> s;
			for(int j = 0; j < n; j++)
				g[i][j] = (s[j] == '1');
		}
		int m = n * n;
		int MAX = (1 << m);
		int ans = m;
		for(int mask = 0; mask < MAX; mask++)
		{
			bool bad = 0;
			int cost = 0;
			for(int i = 0; i < n; i++)
				for(int j = 0; j < n; j++)
				{
					g2[i][j] = (mask >> (i * n + j) & 1);
					if(g[i][j] && !g2[i][j])
						bad = 1;
					cost += g2[i][j];
					cost -= g[i][j];
				}
			if(bad)
				continue;
			for(int i = 0; !bad && i < n; i++)
			{
				bool found = 0;
				for(int sm = 0; sm < (1 << n); sm++)
				{
					bool is = 1;
					for(int j = 0; j < n; j++)
						is &= !(g2[i][j] ^ (sm >> j & 1));
					if(!is)
						continue;
					int cnt = 0;
					for(int j = 0; j < n; j++)
						if(j != i)
						{
							bool have = 0;
							for(int k = 0; !have && k < n; k++)
								have |= (g2[j][k] && (sm >> k & 1));
							cnt += have;
						}
					if(cnt < __builtin_popcount(sm))
					{
						found = 1;
						break;
					}
				}
				bad |= (!found);
			}
			if(!bad)
				ans = min(ans, cost);
		}
		cout << ans << endl;
	}
}
