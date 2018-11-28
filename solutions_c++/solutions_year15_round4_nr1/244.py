#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <string.h>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <set>
#include <cassert>
#include <ctime>
#include <cstdlib>

using namespace std;

#define ll long long
#define ld long double
#define ull unsigned long long
#define uint unsigned int
#define fst first
#define snd second
#define pb push_back
#define mp make_pair
#define y0 alfdjasldfjeao
#define y1 safiodjafis

const int maxn = 111;

map < char, int > ch;
string s[maxn];
bool flag[4];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	ch['^'] = 0, ch['>'] = 1, ch['v'] = 2, ch['<'] = 3;
	for (int test = 1; test <= T; test++)
	{
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			cin >> s[i];
		bool bl = true;
		int ans = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (s[i][j] != '.')
				{
					for (int i = 0; i < 4; i++)
						flag[i] = false;
					for (int g = i - 1; g >= 0; g--)
						if (s[g][j] != '.')
							flag[0] = true;
					for (int g = i + 1; g < n; g++)
						if (s[g][j] != '.')
							flag[2] = true;
					for (int g = j - 1; g >= 0; g--)
						if (s[i][g] != '.')
							flag[3] = true;
					for (int g = j + 1; g < m; g++)
						if (s[i][g] != '.')
							flag[1] = true;
					if (flag[ch[s[i][j]]])
						continue;
					else if (flag[0] || flag[1] || flag[2] || flag[3])
						ans++;
					else
						bl = false;
				}
		cout << "Case #" << test << ": ";
		if (bl)
			cout << ans << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}
