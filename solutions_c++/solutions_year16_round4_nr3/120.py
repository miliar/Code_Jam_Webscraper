#include<cassert>
#include<queue>
#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 105, K = 405;

int n, m, k;

int match[K];

bool used[K];

char map[N][N];

/*
int getSide(int id) {
	if (id < m) {
		return 0;
	} else if (id < n + m) {
		return 1;
	} else if (id < n + 2 * m) {
		return 2;
	} else {
		return 3;
	}
}

char& getPos(int id) {
	if (id < m) {
		return map[0][id];
	} else if (id < n + m) {
		return map[id - m][m - 1];
	} else if (id < n + 2 * m) {
		return map[n - 1][m - (id - n - m + 1)];
	} else {
		return map[n - (id - n - 2 * m + 1)][0];
	}
}

char makeInc(int id) {
	int d = getSide(id);
	return (d == 0 || d == 2) ? '\\' : '/';
}

char makeDec(int id) {
	int d = getSide(id);
	return (d == 0 || d == 2) ? '\\' : '/';
}
*/

int stamp, vis[N][N];

const int dx[4] = {1, 1, -1, -1},
		  dy[4] = {1, -1, -1, 1};

int fa[N][N];

bool ban[N][N];

pair<int, int> getPPos(int id) {
	if (id < m) {
		return make_pair(0, id);
	} else if (id < n + m) {
		return make_pair(id - m, m);
	} else if (id < n + 2 * m) {
		return make_pair(n, m - (id - n - m));
	} else {
		return make_pair(n - (id - n - 2 * m), 0);
	}
}

bool makeMatch(int u, int v) {
	/*
	   if (v == (u + 1) % k) {
	   if (u == m - 1) {
	   map[0][m - 1] = '\\';
	   } else if (u == n + m - 1) {
	   map[n][m - 1] = '/';
	   } else if (u == n + 2 * m - 1) {
	   map[n][0] = '\\';
	   } else if (u == k - 1) {
	   map[0][0] = '/';
	   } else {
	   getPos(u) = makeInc(u);
	   getPos(v) = makeDec(v);
	   }
	   } else {
	 */
	queue<pair<int, int> > q;
	++stamp;
	pair<int, int> start = getPPos(u), end = getPPos(v + 1);
	q.push(start);
	vis[start.first][start.second] = stamp;
	while (q.size()) {
		int x = q.front().first, y = q.front().second;
		q.pop();
		for (int d = 0; d < 4; ++d) {
			int tx = x + dx[d], ty = y + dy[d];
			if (tx < 0 || tx > n || ty < 0 || ty > m) {
				continue;
			}
			char ch = (d == 0 || d == 2) ? '\\' : '/';
			if (map[min(tx, x)][min(ty, y)] != ' ' &&  map[min(tx, x)][min(ty, y)] != ch) {
				continue;
			}
			if (vis[tx][ty] != stamp) {
				vis[tx][ty] = stamp;
				fa[tx][ty] = d;
				q.push(make_pair(tx, ty));
			}
		}
	}
	//cout << start.first << ' ' << start.second << ' ' << end.first << ' ' << end.second << endl;
	if (!(vis[end.first][end.second] == stamp)) {
		return false;
	}
	int cx = end.first, cy = end.second;
	while (cx != start.first || cy != start.second) {
		int d = fa[cx][cy];
		int nx = cx - dx[d], ny = cy - dy[d];
		if (d == 0 || d == 2) {
			map[min(nx, cx)][min(ny, cy)] = '\\';
		} else {
			map[min(nx, cx)][min(ny, cy)] = '/';
		}
		cx = nx, cy = ny;
	}
	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		printf("Case #%d:\n", ++id);
		scanf("%d%d", &n, &m);
		k = (n + m) * 2;
		for (int i = 0; i < k; i += 2) {
			int u, v;
			scanf("%d%d", &u, &v);
			--u, --v;
			match[u] = v;
			match[v] = u;
			used[u] = used[v] = false;
		}	
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				map[i][j] = ' ';
			}
		}
		bool flag = true;	
		for (int i = 0; i < k / 2; ++i) {
			int choice = -1;
			for (int u = 0; u < k; ++u) {
				if (!used[u]) {
					bool find = true;
					int vv = u;
					while (true) {
						vv = (vv + 1) % k;
						if (vv == match[u]) {
							break;
						}
						if (!used[vv]) {
							find = false;
							break;
						}
					}
					if (find) {
						choice = u;
						break;
					}
				}
			}
			if (choice == -1) {
				flag = false;
				break;
			}
			if (!makeMatch(choice, match[choice])) {
				flag = false;
				break;
			}
			used[choice] = true;
			used[match[choice]] = true;
		}
		if (!flag) {
			puts("IMPOSSIBLE");
		} else {
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < m; ++j) {
					if (map[i][j] == ' ') {
						map[i][j] = '/';
					}
				}
				map[i][m] = '\0';
				puts(map[i]);
			}
		}
	}
	return 0;
}
