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

const int PMAX = 10005;
const int NMAX = 70;

ll e[NMAX][PMAX]; 
ll f[NMAX][PMAX];
int p;
ll s[NMAX];
bool ok;

void rec(int n, int p)
{
	if (ok) return;

	if (p == 1 && f[n][0] == 1 && e[n][0] == 0)
	{
		ok = true;
		return;	       	
	}

	forn(i, p)
	{
		s[n] = e[n][i];
		if (e[n][i] == 0)
		{
			bool can = true;
			forn(j, p)
			{
				if (f[n][j] & 1) can = false;                	
			}
			if (!can) continue;

			forn(j, p)
			{
				f[n + 1][j] = f[n][j] / 2;
				e[n + 1][j] = e[n][j];
			}
			rec(n + 1, p);
			if (ok) return;
		}

		if (e[n][i] > 0)
		{
			bool can = true;
			forn(j, p)
			{
				f[n + 1][j] = f[n][j];
			}

			int l = 0;
			int r = 0;
			while (l < p)
			{
				while (l < p && f[n + 1][l] == 0) l++;

				if (l == p) break;

				while (r < p && e[n][l] + s[n] > e[n][r]) r++;
				if (r == p || e[n][r] < e[n][l] + s[n] || f[n + 1][r] < f[n + 1][l])
				{
					can = false;
					break;
				}

				f[n + 1][r] -= f[n + 1][l];

				l++;
			}

			if (!can) continue;

			int p1 = 0;
			forn(i, p)
			{
				if (f[n + 1][i] > 0)
				{
					e[n + 1][p1] = e[n][i];
					f[n + 1][p1] = f[n + 1][i];
					p1++;
				}
			}

			rec(n + 1, p1);
			if (ok) return;
		}	
	}	
}

void solve(int test)
{
    printf("Case #%d:", test);

    scanf("%d", &p);
    forn(i, p) 
    {
    	cin >> e[0][i];
    }
    ll cnt = 0;
    forn(i, p)
    {
    	cin >> f[0][i];
    	cnt += f[0][i];
    }

    int n;
    forn(i, 62) 
    	if (cnt & (1LL << i)) n = i;

    ok = false;
    rec(0, p);

    forn(i, n)
    {
    	cout << " " << s[i];
    }
    cout << endl;
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
