
#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <string.h>
#include <string>
#include <limits.h>
#include <algorithm>
#include <set>
#include <ctime>
using namespace std;
#define SZ(x) ((int)(x).size())
#define rep(i,a,n) for (int i=a; i<(int)n; i++)
#define per(i,n,a) for (int i=n; i>=a; i--)
#define hk push_back
#define pk pop_back
#define mp make_pair
#define PI 3.141592653589793
#define clr(a) memset(a, 0, sizeof(a))
#define clr1(a) memset(a, -1, sizeof(a))
typedef vector<int> VI;
typedef vector< pair<int, int> > VIP;
typedef vector< pair<int, pair<int, double> > > VIPP;
typedef vector<string> VS;
typedef vector <double> VD;
typedef vector <bool> VB;
typedef long long ll;
#define MAX_V 1000
const ll mod = 1000000007;
ll powmod(ll a, ll b) {
	ll res = 1; a %= mod; for (; b; b >>= 1){ if (b & 1)res = res*a%mod; a = a*a%mod; }return res;
}

int T, R, C;
char board[100][100];
int direction[4][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

int main() {
	cout.precision(12);
	cin >> T;
	int T1 = 0;
	while (T1++ < T) {
		cin >> R >> C;
		rep(i, 0, R) {
			rep(j, 0, C) {
				cin >> board[i][j];
			}
		}


		int ret = 0;
		bool possible = true;
		rep(i, 0, R) {
			rep(j, 0, C) {
				if (board[i][j] != '.') {
					bool empty[4] = { 0, 0, 0, 0 };
					int cnt = 0;
					rep(k, 0, 4) {
						int x = i, y = j;
						bool stop = false;
						while (1) {
							x += direction[k][0]; y += direction[k][1];
							if (x < 0 || x >= R || y < 0 || y >= C) break;
							if (board[x][y] != '.') {
								stop = true; break;
							}
						}
						if (!stop) {
							cnt++; empty[k] = true;
						}
					}
					if (cnt == 4) {
						possible = false; break;
					}
					else {
						if (empty[0] && board[i][j] == '^') ret++;
						if (empty[1] && board[i][j] == 'v') ret++;
						if (empty[2] && board[i][j] == '<') ret++;
						if (empty[3] && board[i][j] == '>') ret++;
					}
				}
			}
			if (!possible) break;
		}

		if (!possible) cout << "Case #" << T1 << ": " << "IMPOSSIBLE" << endl;
		else cout << "Case #" << T1 << ": " << ret << endl;






		/*

		if (R == 1 && C == 1) {
		if (board[0][0] == '.') cout << "Case #" << T1 << ": " << "0" << endl;
		else cout << "Case #" << T1 << ": " << "IMPOSSIBLE" << endl;
		}

		else if (R == 1) {
		int cnt = 0;
		rep(j, 0, C) {
		if (board[0][j] != '.') {
		cnt++;
		}
		}
		if (cnt == 1) cout << "Case #" << T1 << ": " << "IMPOSSIBLE" << endl;

		else {
		int ret = 0;
		rep(j, 0, C) {
		if (j == 0) if (board[0][j] != '.' && board[0][j] != '>') ret++;
		else if (j == C - 1) if (board[0][j] != '.' && board[0][j] != '<') ret++;
		else if (board[0][j] == '^' || board[0][j] == 'v') ret++;
		}
		cout << "Case #" << T1 << ": " << ret << endl;
		}
		}
		else if (C == 1) {
		int cnt = 0;
		rep(i, 0, R) {
		if (board[i][0] != '.') {
		cnt++;
		}
		}
		if (cnt == 1) cout << "Case #" << T1 << ": " << "IMPOSSIBLE" << endl;

		else {
		int ret = 0;
		rep(i, 0, R) {
		if (i == 0) if (board[i][0] != '.' && board[i][0] != 'v') ret++;
		else if (i == R - 1) if (board[i][0] != '.' && board[i][0] != '^') ret++;
		else if (board[i][0] == '>' || board[i][0] == '<') ret++;
		}
		cout << "Case #" << T1 << ": " << ret << endl;
		}
		}
		else {
		int ret1 = 0;
		bool possible = true;
		rep(i, 1, R - 1) {
		rep(j, 1, C - 1) {
		if (board[i][j] != '.') {
		int cnt = 0;
		rep(k, 0, 4) {
		int x = i, y = j;
		bool stop = false;
		while (1) {
		x += direction[k][0]; y += direction[k][1];
		if (x < 0 || x >= R || y < 0 || y >= C) break;
		if (board[x][y] != '.') {
		stop = true; break;
		}
		}
		if (!stop) cnt++;
		}
		if (cnt == 4) {
		possible = false; break;
		}
		}
		}
		if (!possible) break;
		}

		if (!possible) cout << "Case #" << T1 << ": " << "IMPOSSIBLE" << endl;


		else {
		int ret = 0;
		rep(i, 0, R) {
		if (i == 0) if (board[i][0] == '<' || board[i][0] == '^') ret++;
		else if (i == R - 1) if (board[i][0] == '<' || board[i][0] == 'v') ret++;
		else if (board[i][0] == '<') ret++;
		}
		rep(i, 0, R) {
		if (i == 0) if (board[i][C - 1] == '>' || board[i][C - 1] == '^') ret++;
		else if (i == R - 1) if (board[i][C - 1] == '>' || board[i][C - 1] == 'v') ret++;
		else if (board[i][C - 1] == '>') ret++;
		}
		rep(j, 1, C - 1) {
		if (board[0][j] == '^') ret++;
		if (board[R - 1][j] == 'v') ret++;
		}
		cout << "Case #" << T1 << ": " << ret + ret1 << endl;
		}
		}
		*/
	}

	return 0;
}