#pragma comment(linker, "/STACK:256000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
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

#define pi 3.1415926535897932

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;

#define NMAX 2005

int n;
int a[NMAX], b[NMAX];
int p[NMAX];
bool used[NMAX];
int prv[NMAX], nxt[NMAX];

void solve(int test)
{
	printf("Case #%d:", test);

	cin >> n;
	forn(i, n) cin >> a[i];
	forn(i, n) cin >> b[i];

	memset(used, 0, sizeof(used));

	for1(k, n)	
	{
		forn(i, n)
		{
			prv[i] = nxt[i] = 0;
		}

		forn(i, n)
		{
			if (used[i])
			{
				prv[i] = max(prv[i], a[i]);
			}
			if (i > 0) prv[i] = max(prv[i], prv[i - 1]);
		}
		for (int i = n - 1; i >= 0; i--)
		{
			if (i < n - 1) nxt[i] = max(nxt[i], nxt[i + 1]);
			if (used[i])
			{
				nxt[i] = max(nxt[i], b[i]);
			}
		}

		bool f = false;

		vector<int> pos;

		forn(i, n)
		{
			if (used[i]) continue;

			int reqa = prv[i] + 1;
			int reqb = nxt[i] + 1;

			if (a[i] == reqa && b[i] == reqb)
			{
				pos.pb(i);		
			}
		}

		forv(i, pos)
		{
			bool ok = true;
			forv(j, pos)
			{
				if (j < i && b[pos[j]] < b[pos[i]] + 1) ok = false;
				if (j > i && a[pos[j]] < a[pos[i]] + 1) ok = false;
			}
			if (ok)
			{
				f = true;
				used[pos[i]] = true;
				p[pos[i]] = k;
				break;
			}
		}
		assert(f);

	}

	forn(i, n)
	{
		cout << " " << p[i];
	}
	cout << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc; scanf("%d\n", &tc);

    forn(it, tc) solve(it + 1);

    return 0;
}
