#include <cmath>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <cstring>
#include <cstdio>
#include <string>
#include <functional>

#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define tr(cont, it) for (typeof(cont.begin()) it = cont.begin() ; it != cont.end() ; it++)
#define FOR(i, j, k, l) for(int i=(j) ; i<(k) ; i+=(l))
#define rep(i, j) FOR(i, 0, j, 1)
#define rrep(i, j) FOR(i, j, -1, -1)

#define INF 1000000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef long long ll;

int R, C, M, CASE;
char board[5][5];

bool bound(int x, int y) {
	return x >= 0 && x < R &&
				y >= 0 && y < C;
}

int dist[5][5];
int near[5][5];
int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};
int fx, fy;
bool done = false;

void dfs(int x, int y) {
	dist[x][y] = 1;
	rep(d, 8) {
		int nx, ny;
		nx = x + dx[d];
		ny = y + dy[d];
		if (bound(nx, ny) && near[nx][ny] == 0 && dist[nx][ny] == -1) {
			dist[nx][ny] = 1;
			dfs(nx, ny);
		}
	}
}

int components() {
	int ans = 0;
	memset(dist, -1, sizeof dist);
	rep(i, R) {
		rep(j, C) {
			if (near[i][j] == 0 && dist[i][j] == -1) {
				ans++;
				fx = i, fy = j;
				dfs(i, j);
			}
		}
	}
	return ans;
}

int check2() {
	rep(i, R) rep(j, C) {
		if (near[i][j] != -1 && near[i][j] != 0) {
			int zeros = 0;
			rep(d, 8) {
				int nx, ny;
				nx = i + dx[d];
				ny = j + dy[d];
				if (bound(nx, ny) && near[nx][ny] == 0) {
					zeros++;
				}
			}
			if (zeros == 0) {
				return 0;
			}
		}
	}
	return 1;
}

int check() {
	memset(near, 0, sizeof near);

	rep(i, R) {
		rep(j, C) {
			if (board[i][j] != '*') {
				rep(d, 8) {
					int nx, ny;
					nx = i + dx[d];
					ny = j + dy[d];
					if (bound(nx, ny)) {
						near[i][j] += (board[nx][ny] == '*');
					}
				}
			}
			else {
				near[i][j] = -1;
			}
		}
	}

	if (components() == 1 && check2()) {
		done = true;
		return 1;
	}
	return 0;
}

void pboard() {
	rep(i, R) {
		rep(j, C) {
			printf("%c", board[i][j]);
		}
		printf("\n");
	}
}

void solve(int r, int c, int m) {
	if (done) return;
	if (m == 0) {
		if (check()) {
			board[fx][fy] = 'c';
			pboard();
		}
		return;
	}
	if (r != R) {
		if (c == C) {
			solve(r+1, 0, m);
		}
		else {
			board[r][c] = '*';
			solve(r, c+1, m-1);
			if (done) return;
			board[r][c] = '.';
			solve(r, c+1, m);
		}
	}
}

void solve_for_one() {
	if (R == C) {
		printf("c\n");
	}
	else {
		int r = max(R, C) - M;
		while (M--) {
			printf("*");
			if (C == 1) printf("\n");
		}
		while ((--r) >= 1) {
			printf(".");
			if (C == 1) printf("\n");
		}
		printf("c\n");
	}
}

void solve_for_two() {
	if (R == C) {
		if (M == 0) {
			printf("..\n.c\n");
		}
		else {
			printf("Impossible\n");
		}
	}
	else {
		if (M % 2 == 0) {
			int r = max(R, C) - M/2;
			if (C == 2) {
				while (M) {
					printf("**\n");
					M -= 2;
				}
				while ((--r) >= 1) {
					printf("..\n");
				}
				printf(".c\n");
			}
			else {
				rep(i, M/2) printf("*");
				rep(i, r) printf(".");
				printf("\n");
				rep(i, M/2) printf("*");
				rep(i, r-1) printf(".");
				printf("c\n");
			}
		}
		else {
			printf("Impossible\n");
		}
	}
}

int main() {
	scanf("%d", &CASE);
	for (int c=1 ; c<=CASE ; c++) {
		done = false;
		printf("Case #%d:\n", c);
		scanf("%d %d %d", &R, &C, &M);
		if (R == 1 || C == 1) {
			solve_for_one();
			continue;
		}
		else if ((R*C) - M == 1) {
			rep(i, R) rep(j, C) board[i][j] = '*';
			board[R-1][C-1] = 'c';
			pboard();
			continue;
		}
		else if (R*C - M < 4) {
			printf("Impossible\n");
			continue;
		}
		else if (R == 2 || C == 2) {
			solve_for_two();
			continue;
		}
		rep(i, R) rep(j, C) board[i][j] = '.';
		solve(0, 0, M);
		if (!done) {
			printf("Impossible\n");
		}
	}
}