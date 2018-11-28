#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

const int NMAX = 105;

int n, m;
char a[NMAX][NMAX];

string s = "<>^v";
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int get_idx(char c)
{
	forv(i, s)
		if (s[i] == c) return i;
	return -1;
}

bool valid(int x, int y)
{
	return x >= 0 && x < n && y >= 0 && y < m;
}

void solve(int test)
{
    printf("Case #%d: ", test);

	scanf("%d %d\n", &n, &m);
	forn(i, n)
	{
		forn(j, m)
		{
			scanf("%c", &a[i][j]);
		}
		scanf("\n");
	}

	int ans = 0;

	forn(i, n)
	{
		forn(j, m)
		{
			if (a[i][j] != '.')
			{
				int k = get_idx(a[i][j]);
				int x = i;
				int y = j;

				do
				{
					x += dx[k];
					y += dy[k];
				}
				while (valid(x, y) && a[x][y] == '.');

				if (!valid(x, y))
				{
					ans++;
					bool f = false;
					forn(k1, 4)
					{
						if (k1 == k) continue;
						x = i; y = j;
						do
						{
							x += dx[k1];
							y += dy[k1];
						}
						while (valid(x, y) && a[x][y] == '.');

						if (valid(x, y))
						{
							f = true; break;	
						}
					}
					if (!f)
					{
						cout << "IMPOSSIBLE\n";
						return;
					}
				}
			}
		}
	}
	cout << ans << endl;
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
