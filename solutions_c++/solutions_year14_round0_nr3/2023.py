#pragma comment(linker, "/STACK:256000000")

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const double PI = acos(-1.0);
const int INF = 1000000000;
const int MOD = 1000000007;

bool was[5][5];
bool bad[5][5];
int opened;


int r, c;
int need;

void dfs(int x, int y) {
	was[x][y] = 1;
	++opened;

	bool can = 1;
	for (int dx = -1; dx <= 1; ++dx) {
		for (int dy = -1; dy <= 1; ++dy) {
			int nx = x + dx, ny = y + dy;
			if (nx != x || ny != y) {
				if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
					if (bad[nx][ny]) {
						can = 0;
					}
				}
			}
		}
	}

	if (can) {
		for (int dx = -1; dx <= 1; ++dx) {
			for (int dy = -1; dy <= 1; ++dy) {
				int nx = x + dx, ny = y + dy;
				if (nx != x || ny != y) {
					if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
						if (was[nx][ny] == 0) {
							dfs(nx, ny);
						}
					}
				}
			}
		}
	}
}


string res;

vector<int> current;
void binomial(int n, int k, int down = -1) {

	if (!res.empty()) {
		return;
	}

	if (k == 0) {
		memset(was, 0, sizeof(was));		
		int at = 0;
		int id = 0;
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {

				if (at < current.size() && current[at] == id) {
					bad[i][j] = 1;
					++at;
				} else {
					bad[i][j] = 0;
				}
				++id;
			}
		}

		if (bad[0][0] == 0) {
			opened = 0;
			dfs(0, 0);

			if (opened == need) {
				res.clear();
				for (int i = 0; i < r; ++i) {
					for (int j = 0; j < c; ++j) {
						if (bad[i][j]) res += '*';
						else res += '.';
					}
					res += "\n";
				}
				res[0] = 'c';
				return;
			}
		}

		memset(was, 0, sizeof(was));
		if (bad[1][1] == 0 && r >= 2 && c >= 2) {
			opened = 0;
			dfs(1, 1);

			if (opened == need) {
				res.clear();
				for (int i = 0; i < r; ++i) {
					for (int j = 0; j < c; ++j) {
						if (i == 1 && j == 1) {
							res += 'c';
							continue;
						}
						if (bad[i][j]) res += '*';
						else res += '.';
					}
					res += "\n";
				}
				//res[0] = 'c';
				return;
			}
		}

		return;
	}

	for (int i = down + 1; i < n; ++i) {
		if (!res.empty()) {
			return;
		}

		current.push_back(i);
		binomial(n, k - 1, i);
		current.pop_back();
	}
}


int main() {
	int _start = clock();

#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
#define taskname "cutting"
	//freopen(taskname".in","r",stdin);
    //freopen(taskname".out","w",stdout);
#endif
	
	int T;
	cin >> T;

	for (int test = 1; test <= T; ++test) {
		cerr << test << endl;
		int m;
		cin >> r >> c >> m;
		need = r * c - m;

		res.clear();
		binomial(r * c, m);
		if (res.empty()) {
			res = "Impossible\n";
		}
		printf("Case #%d:\n%s", test, res);
	}




	cerr << endl << endl << "Time: " << (double)(clock() - _start) / CLOCKS_PER_SEC << endl;
	return 0;
}