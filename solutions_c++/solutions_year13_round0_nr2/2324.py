#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

int a[111][111];
int w[111][111];
int n, m;
int cnt;


void Load()
{
	cin >> n >> m;
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			cin >> a[i][j];
			w[i][j] = 0;
		}
	}
	cnt = n*m;
}

void Mark(int bx, int by, int dx, int dy, int l, int h) {
	int i;
	int cur = a[bx][by];
	for (i = 0; i < l; i++) {
	    if (a[bx][by] >= cur) {
	    	w[bx][by] += h;
	    }
	    if (a[bx][by] > cur) 
	    	cur = a[bx][by];
		bx += dx;
		by += dy;
	}
}

void Solve()
{
	int i, j;
	for (i = 0; i < n; i++) {
		Mark(i, 0, 0, 1, m, 1);
		Mark(i, m-1, 0, -1, m, 1);
	}
	for (i = 0; i < m; i++) {
		Mark(0, i, 1, 0, n, 10);
		Mark(n-1, i, -1, 0, n, 10);
	}
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			if (w[i][j] % 10 == 2 || w[i][j] / 10 == 2) cnt--;
		}
	}
	if (cnt > 0) cout << "NO\n";
	else cout << "YES\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
