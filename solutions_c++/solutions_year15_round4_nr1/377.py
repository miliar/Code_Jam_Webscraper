#pragma comment(linker, "/STACK:512000000")
#include <iostream>
#include <vector>
#include <iomanip>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <cstring>
#include <ctime>
#include <string>
#include <sstream>
#include <math.h>
#include <stack>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

char dirs[] = {'^', 'v', '<', '>'};
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int get_dir_id(char c) {
	for (int i = 0; i < 4; ++i) {
		if (dirs[i] == c) {
			return i;
		}
	}

	return -1;
}

const int N = 105;

pair<int, int> next_cell[N][N][4];

const pair<int, int> UNDEF = make_pair(-1, -1);
const pair<int, int> OUT = make_pair(-321, -123);

pair<int, int> get(int x, int y, int dir, const vector<string>& field) {
	if (x < 0 || x >= field.size() || y < 0 || y >= field[0].size()) {
		return OUT;
	}
	
	if (next_cell[x][y][dir] != UNDEF) {
		return next_cell[x][y][dir];
	}
	int nx = x + dx[dir];
	int ny = y + dy[dir];

	if (nx < 0 || nx >= field.size() || ny < 0 || ny >= field[0].size()) {
		next_cell[x][y][dir] = OUT;
	} else {
		if (field[nx][ny] != '.') {
			next_cell[x][y][dir] = make_pair(nx, ny);
		} else {
			next_cell[x][y][dir] = get(nx, ny, dir, field);
		}
	}

	return next_cell[x][y][dir];
}

int is_safe[N][N];


int solve(vector<string> field) {
	int n = field.size();
	int m = field[0].size();

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			for (int z = 0; z < 4; ++z) {
				next_cell[i][j][z] = UNDEF;
				is_safe[i][j] = 0;
			}
		}
	}

	int ans = 0;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (field[i][j] != '.') {
				int cdir = get_dir_id(field[i][j]);

				pair<int, int> to = get(i, j, cdir, field);

				if (to != OUT) {
					is_safe[i][j] = true;
				} else {

					for (int ndir = 0; ndir < 4; ++ndir) {
						pair<int, int> nto = get(i, j, ndir, field);

						if (nto != OUT) {
							++ans;
							is_safe[i][j] = true;
							goto end;
						}
					}

					return -1;

					end:;
				}
			}
		}
	}

	return ans;
}

int main() {

	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
	    freopen("output.txt","w",stdout);
	#else
	#define taskname "cutting"
		//freopen(taskname".in","r",stdin);
		//freopen(taskname".out","w",stdout);
	#endif



	int tests_; cin >> tests_;
	for (int test_ = 1; test_ <= tests_; ++test_) {
		
		int r, c;
		cin >> r >> c;
		vector<string> f(r);
		for (int i = 0; i < r; ++i) {
			cin >> f[i];
		}
		
		int ans = solve(f);

		if (ans >= 0) {
			cout << "Case #" << test_ << ": " << ans << endl;		
			cerr << "Case #" << test_ << ": " << ans << endl;
		} else {
			cout << "Case #" << test_ << ": " << "IMPOSSIBLE" << endl;		
			cerr << "Case #" << test_ << ": " << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}