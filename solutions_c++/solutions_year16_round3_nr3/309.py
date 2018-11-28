#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>
#include <ctime>

using namespace std;

vector<int> memo[4][4][4][11];

int used[27 + 13];
int cnt[64];

void go(int x) {
	if (x == 27) {
		memset(cnt, 0, sizeof cnt);
		
		int total = 0;
		
		int A = 0, B = 0, C = 0;
		
		for (int i = 0; i < x; ++i) {
			if (used[i]) {
				int a = i % 3;
				int b = (i / 3) % 3;
				int c = i / 9;
				
				++total;
				A = max(A, a);
				B = max(B, b);
				C = max(C, c);
				++a; ++b; ++c;
				cnt[a + b * 4]++;
				cnt[a + c * 16]++;
				cnt[b * 4 + c * 16]++;
			}
		}
		
		int mx = *max_element(cnt, cnt + 64);
		
		if (mx > 10) return;
		
		if (memo[A][B][C][mx].size() < total) {
			memo[A][B][C][mx].clear();
			for (int i = 0; i < 27; ++i) if (used[i])
				memo[A][B][C][mx].push_back(i);
		}
		
		return;
	}
	
	used[x] = 1;
	go(x + 1);
	used[x] = 0;
	go(x + 1);
}

void gen() {
	go(0);
}

void solve() {
	int a, b, c, k;
	cin >> a >> b >> c >> k;
	int x, y, z, t;
	x = y = z = t = 0;
	for (int i = 0; i < a; ++i) for (int j = 0; j < b; ++j) for (int r = 0; r < c; ++r)
		for (int l = 0; l <= k; ++l) if (memo[i][j][r][l].size() > memo[x][y][z][t].size()) {
			x = i; y = j; z = r;
			t = l;
		}
			
	static int test_id = 0;
	++test_id;
	cout << "Case #" << test_id << ": " << memo[x][y][z][t].size() << endl;
	
	for (int i = 0; i < memo[x][y][z][t].size(); ++i) {
		int code = memo[x][y][z][t][i];
		int a = code % 3;
		int b = (code / 3) % 3;
		int c = code / 9;
		cout << a + 1 << ' ' << b + 1 << ' ' << c + 1 << endl;
	}
}

int main() {
	gen();
	cerr << clock() << endl;
	int t;
	cin >> t;
	while (t --> 0)
		solve();
	return 0;
}