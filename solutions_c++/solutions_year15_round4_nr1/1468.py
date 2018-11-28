#include <algorithm>
#include <vector>
#include <string>
#include <ctime>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

const int N = 105;
int n, m;
char s[N][N];

int dir[4][2] = { 0, 1, -1, 0, 0, -1, 1, 0 };
int sr[N], sc[N];
map<char, int> mp;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	mp['>'] = 0;
	mp['^'] = 1;
	mp['<'] = 2;
	mp['v'] = 3;
	int t;
	cin >> t;
	for (int tt = 0; tt < t; ++tt)
	{
		memset(sr, 0, sizeof(sr));
		memset(sc, 0, sizeof(sc));
		cin >> n >> m;
		for (int i = 0; i < n; ++i)
			scanf("%s", s[i]);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (s[i][j] != '.')
					sr[i]++, sc[j]++;
		int ans = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if (s[i][j] != '.')
				{
					bool fnd = 0;
					int dr = mp[s[i][j]];
					for (int ii = i + dir[dr][0], jj = j + dir[dr][1];
						ii >= 0 && ii < n && jj >= 0 && jj < m;
						ii += dir[dr][0], jj += dir[dr][1])
						if (s[ii][jj] != '.')
						{
							fnd = 1;
							break;
						}
					if (!fnd) ++ans;
					if (sc[j] == 1 && sr[i] == 1)
					{
						ans = -1;
						break;
					}
				}
			}
			if (ans == -1)
				break; 
		}
		if (ans != -1)
		printf("Case #%d: %d\n", tt + 1, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", tt + 1);

	}


	return 0;
}

/*

*/