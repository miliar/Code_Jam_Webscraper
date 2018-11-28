#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <algorithm>
using namespace std;

const int N = 15, M = 5000;

int a[3][N][M];
string st[3][N];
int cnt[3][N][3];
int p2[N];
char c[3];

void work()
{
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	int w = -1;
	for(int i = 0; i <= 2; ++i) {
		if(p == cnt[i][n][0] && r == cnt[i][n][1] && s == cnt[i][n][2]) {
			w = i;
			break;
		}
	}
	if(w == -1) {
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		cout << st[w][n] << endl;
	}
}

void pre()
{
	c[0] = 'P';
	c[1] = 'R';
	c[2] = 'S';
	p2[0] = 1;
	for(int i = 1; i <= 12; ++i) {
		p2[i] = p2[i-1]*2;
	}
	for(int i = 0; i <= 2; ++i) {
		a[i][0][1] = i;
		for(int j = 1; j <= 12; ++j) {
			for(int k = 1; k <= p2[j-1]; ++k) {
				if(a[i][j-1][k] == 0) {
					a[i][j][k*2-1] = 0;
					a[i][j][k*2] = 1;
				}
				else if(a[i][j-1][k] == 1) {
					a[i][j][k*2-1] = 1;
					a[i][j][k*2] = 2;
				}
				else {
					a[i][j][k*2-1] = 0;
					a[i][j][k*2] = 2;
				}
			}
			for(int k = 1; k <= p2[j]; ++k) {
				++cnt[i][j][a[i][j][k]];
			}
		}
	}
	st[0][0] = 'P';
	st[1][0] = 'R';
	st[2][0] = 'S';
	for(int j = 1; j <= 12; ++j) {
		string s0 = st[0][j-1];
		string s1 = st[1][j-1];
		string s2 = st[2][j-1];
		if(s0 < s1) {
			st[0][j] = s0 + s1;
		}
		else {
			st[0][j] = s1 + s0;
		}
		if(s1 < s2) {
			st[1][j] = s1 + s2;
		}
		else {
			st[1][j] = s2 + s1;
		}
		if(s0 < s2) {
			st[2][j] = s0 + s2;
		}
		else {
			st[2][j] = s2 + s0;
		}
	}
}

int main()
{
	#define LOCAL_
	#ifdef LOCAL

	freopen("0.in", "r", stdin);
	freopen("0.out", "w", stdout);

	#endif // LOCAL

	int n;
	cin >> n;
	pre();
	for(int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";
		work();
	}
	return 0;
}
