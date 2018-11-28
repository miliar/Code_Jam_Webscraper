#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int map[100][100], tmp[100][100];
int n, m;

void input() {
	scanf("%d%d", &n, &m);
	for(int i = 0;i < n;i ++) for(int j = 0;j < m;j ++) scanf("%s", &map[i][j]);
}

void solve() {
	vector<pair<int, int> > vp;
	vp.reserve(n*m);

	for(int i = 0;i < n;i ++) for(int j = 0;j < m;j ++) vp.push_back(make_pair(map[i][j], i*100+j));

	sort(vp.begin(), vp.end());

	//printf("%d %d\n", vp[0].first, vp[n*m-1].first);

	for(int i = 0;i < n;i ++) for(int j = 0;j < m;j ++) tmp[i][j] = 100;

	for(int i = 0;i < n*m;i ++) {
		int a = vp[i].second/100, b = vp[i].second%100;
		if(tmp[a][b] == vp[i].first) continue;

		int ok = 1;
		for(int j = 0;j < m;j ++) if(map[a][j] > map[a][b]) { ok = 0; break; }
		if(ok) {
			for(int j = 0;j < m;j ++) if(map[a][b] < tmp[a][j]) tmp[a][j] = map[a][b];
			continue;
		}

		ok = 1;
		for(int j = 0;j < n;j ++) if(map[j][b] > map[a][b]) { ok = 0; break; }
		if(ok) {
			for(int j = 0;j < n;j ++) if(map[a][b] < tmp[j][b]) tmp[j][b] = map[a][b];
		}
		else {
			printf("NO\n");
			return ;
		}
	}

	printf("YES\n");
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}