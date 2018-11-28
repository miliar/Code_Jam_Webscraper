#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int n, m, k;
char a[55][55];
int bad[55][55];
int ok;

bool check() {
	for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (a[i][j] == '.') {
		bad[i][j] = 0;
		for (int dx = -1; dx < 2; dx++) for (int dy = - 1; dy < 2; dy++ ) {
			if (dx == 0 && dy == 0) continue;
			int x = i + dx;
			int y = j + dy;
			if (x < 0 || x >= n || y < 0 || y >= m) continue;
			if (a[x][y] == '*') bad[i][j] = 1;
		}
	}
	for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (a[i][j] == '.') {
		int ok = 0;
		for (int dx = -1; dx < 2; dx++) for (int dy = - 1; dy < 2; dy++ ) {
			if (dx == 0 && dy == 0) continue;
			int x = i + dx;
			int y = j + dy;
			if (x < 0 || x >= n || y < 0 || y >= m) continue;
			if (a[x][y] == '.' && !bad[x][y]) ok = 1;
		}
		if (i == 0 && j == 0) continue;
		if (!ok) return 0;
	}
	return 1;
}

void rec(int x, int p, int s) {
	if (x == n) {
		if (s != k || ok) return;
		if (check()) {
			ok = 1;
				a[0][0] = 'c';
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < m; j++) putchar(a[i][j]);
					puts("");
				}

		}
		return;
	}
	for (int q = 0; q <= p; q++) {
		for (int i = 0; i < q; i++) a[x][i] = '.';
		rec(x + 1, q, s + q);
		for (int i = 0; i < q; i++) a[x][i] = '*';
	}
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> m >> k;
		k = n * m - k;
		cout << "Case #" << tt << ":" << endl;
		for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) a[i][j] = '*';
		ok = 0;
		rec(0, m, 0);
		if (!ok) puts("Impossible");

	}
	return 0;
}