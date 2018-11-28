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

const int N = 10;

int R, C;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int a[N][N];

bool good(int x, int y)
{
	int cnt = 0, emp = 0;
	forn(k, 4)
	{
		int x1 = x + dx[k];
		int y1 = y + dy[k];
		if (y1 == -1) y1 = C - 1;
		if (y1 == C) y1 = 0;
		if (x1 < 0 || x1 >= R) continue;

		if (a[x1][y1] == a[x][y]) cnt++;
		if (a[x1][y1] == 0) emp++;
	}

	return a[x][y] >= cnt && a[x][y] <= cnt + emp; 
}

set<vector<vector<int> > > ans;

void rec(int x, int y)
{
	if (y == C)
	{
		x++;
		y = 0;
	}

	if (x == R)
	{
		vector<vector<int> > v(C);
		forn(i, C)
		{
			v[i].resize(R);
			forn(j, R)
				v[i][j] = a[j][i];
		}

		vector<vector<int> > best = v;

		forn(i, C)
		{	
			rotate(v.begin(), v.begin() + 1, v.end());
			if (v < best) best = v;
		}

		ans.insert(best);
		return;
	}

	for (int c = 1; c <= 3; c++)
	{
		a[x][y] = c;

		if (!good(x, y)) continue;

		bool ok = true;
		forn(k, 4)
		{
			int x1 = x + dx[k];
			int y1 = y + dy[k];
			if (y1 == C) y1 = 0;
			if (y1 == -1) y1 = C - 1;
			if (x1 < 0 || x1 >= R || a[x1][y1] == 0) continue;

			if (!good(x1, y1)) 
			{
				ok = false;
				break;
			}		
		}
		if (ok) rec(x, y + 1);
	}

	a[x][y] = 0;
}
void solve(int test)
{
    printf("Case #%d: ", test);

	cin >> R >> C;

	ans.clear();

	rec(0, 0);

    cout << (int)ans.size() << endl; 
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
