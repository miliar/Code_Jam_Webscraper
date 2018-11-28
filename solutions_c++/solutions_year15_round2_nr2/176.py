#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

#define mp make_pair
#define pb push_back
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define all(c) (c).begin(), (c).end()
#define sz(c) (int)(c).size()


using namespace std;

typedef long long ll;

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

void solve(int test) {
	int R, C, N;
	scanf("%d%d%d", &R, &C, &N);
	int _N = N;
	vector<vector<int>> b(R, vector<int>(C, 0));
	int res = 4 * N;
	for (int it = 0; it < 2; it++) {
		int ans = 0;
		N = _N;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				b[r][c] = 0;
				if ((r + c) % 2 == it && N) {
					b[r][c] = 1;
					N--;
				}
			}
		}
		vector<int> q;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (b[r][c]) continue;
				int a = 0;
				for (int k = 0; k < 4; k++) {
					int nr = r + dr[k];
					int nc = c + dc[k];
					if (nr >= R || nr < 0) continue;
					if (nc >= C || nc < 0) continue;
					a += b[nr][nc];
				}
				q.push_back(a);
			}
		}
		sort(q.begin(), q.end());
		for (int i = 0; i < N; i++) ans += q[i];
		res = min(ans, res);
	}
	printf("Case #%d: %d\n", test, res);
}

int main(){
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) solve(test);
}
