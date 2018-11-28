#include <algorithm>
#include <vector>
#include <cstdio>
#define b2e(C) C.begin(), C.end()
using namespace std;

struct P { int i, j; };

bool possible(int n, int m, int a[100][100]) {
	int row[100] = {};
	int col[100] = {};
	vector<P> pos;
	auto H = [&](P p) { return a[p.i][p.j]; };
	for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) pos.push_back(P{i,j});
	sort(b2e(pos), [&](P p, P q) { return H(p) > H(q); });
	for(auto p : pos) {
		int h = H(p);
		if(!row[p.i]) row[p.i] = h;
		if(!col[p.j]) col[p.j] = h;
		if(row[p.i] != h && col[p.j] != h) return false;
	}
	return true;
}

int main() {
	int T; scanf("%d", &T);
	int a[100][100];
	for(int t = 1; t <= T; t++) {
		int n, m; scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) scanf("%d", &a[i][j]);
		printf("Case #%d: %s\n", t, possible(n,m,a) ? "YES" : "NO");
	}
}

