#include <cassert>
#include <cstdlib>
#include <cstdio>

#include <functional>
#include <iostream>
#include <algorithm>
#include <valarray>
#include <iterator>
#include <complex>
#include <numeric>
#include <utility>
#include <bitset>
#include <limits>
#include <memory>
#include <random>
#include <string>
#include <tuple>
#include <new>

#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <deque>
#include <array>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>

#define DEBUG(...) fprintf(stderr, __VA_ARGS__)
#define ALL(c) begin(c), end(c)
#define SIZE(c) (int)(c).size()

using namespace std;

std::random_device rd;
std::mt19937 gen(rd());

const int maxn = 123;
unsigned char b[maxn][maxn];
int v[maxn][maxn];
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};
unsigned char dv[] = {'^', 'v', '<', '>'};
int di[256];
int R, C;

int check(int r, int c) {
	return r >= 0 && c >= 0 && r < R && c < C;
}

int go(int r, int c, int k) {
	if (!check(r, c)) return 0;
	if (b[r][c] == '.') return go(r + dr[k], c + dc[k], k);
	if (v[r][c]) return 1;
	v[r][c] = 1;
	k = di[b[r][c]];
	return go(r + dr[k], c + dc[k], k);
}

void solve(int test) {
	scanf("%d%d\n", &R, &C);
	for (int i = 0; i < R; i++) {
		scanf("%s", b[i]);
	}
	int cnt = 0;
	int fail = 0;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (b[i][j] == '.') continue;
			int good = 0;
			int nice = 0;
			for (int k = 0; k < 4; k++) {
				int r = i;
				int c = j;
				r += dr[k];
				c += dc[k];
				while (check(r, c)) {
					if (b[r][c] != '.') {
						good = 1;
						if (b[i][j] == dv[k]) nice = 1;
						break;
					}
					r += dr[k];
					c += dc[k];
				}
			}
			if(!good) {
				fail = 1;
			} 
			cnt += !nice;
		}
	}
	printf("Case #%d: ", test);
	if (fail) {
		printf("IMPOSSIBLE\n");
	} else {
		printf("%d\n", cnt);
	}
}

int main () {
	for (int i = 0; i < 4; i++) di[dv[i]] = i;
 	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) solve(test);
}
