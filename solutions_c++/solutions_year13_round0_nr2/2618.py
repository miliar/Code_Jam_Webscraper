#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
#include <complex>
#include <list>

using namespace std;
 
void ASS(bool b)
{
    if (!b)
    {
        ++*(int*)0;
    }
}
 
#define FOR(i, x) for (int i = 0; i < (int)(x); ++i)
#define CL(x) memset(x, 0, sizeof(x))
#define CLX(x, y) memset(x, y, sizeof(x))
 
#pragma comment(linker, "/STACK:106777216")
 
typedef vector<int> vi;

typedef unsigned long long LL;

int n, m;
int a[128][128];

bool Ok(int x, int y, int h) {
	bool ox = 1;
	bool oy = 1;
	FOR(i, n)
		if (a[i][y] > h)
			ox = 0;
	FOR(i, m)
		if (a[x][i] > h)
			oy = 0;
	return ox || oy;
}

void Solve() {
	cin >> n >> m;
	vector< vector< pair<int, int> > > v(101);
	FOR(i, n)
		FOR(j, m) {
			cin >> a[i][j];
			if (a[i][j] > 100) {
				cout << "NO";
				return;
			}
			v[a[i][j]].push_back(make_pair(i, j));
		}
	for (int h = 100; h >= 0; h--) {
		const vector< pair<int, int> >& vv = v[h];
		FOR(i, vv.size())
			if (!Ok(vv[i].first, vv[i].second, h)) {
				cout << "NO";
				return;
			}
	}
	cout << "YES";
}

int main()
{
	freopen("c://my//in.txt", "r", stdin);
	freopen("c://my//out.txt", "w", stdout);

	int T;
	cin >> T;

	FOR(i, T) {
		cout << "Case #" << (i + 1) << ": ";
		Solve();
		cout << "\n";
	}

	return 0;
}
