#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
#define m(x,y) make_pair(x,y)
#define mx 105
int dist[105][105][2] = { 0 };
char ar[mx];

struct state {
	int x, y, z;
	state(int x, int y, int z) {
		this->x = x;
		this->y = y;
		this->z = z;
	}
};
bool operator< (const state & a, const state &b) {
	return a.x < b.x;
}
int n;
void bfs() {
	n= strlen(ar + 1);
	for (int i = 0;i <= n;++i)
		for (int j = 0;j <= n;++j)
			for (int k = 0;k <= 1;++k)
				dist[i][j][k] = (1 << 30);
	priority_queue<pair<int, state> > Q;
	Q.push(m(0, state(0, 0, 0)));
	Q.push(m(0, state(0, 0, 1)));
	while (!Q.empty()) {
		int x = Q.top().second.x;
		int y = Q.top().second.y;
		int z = Q.top().second.z;
		int d = -Q.top().first;
		Q.pop();
		bool Z = (z > 0);
		if (dist[x][y][z] <= d)continue;
		dist[x][y][z] = d;
		Q.push(m(-(d + 1), state(y, x, !Z)));
		int i = x + y + 1;
		if (i <= n) {
			bool type = (ar[i] == '+');
			
			if (Z && type) Q.push(m(-d, state(x + 1, y, z)));
			if(!Z && !type) Q.push(m(-d, state(x, y+1, z)));		
		}
	}
}
int main() {
	int t;
	freopen("B-large.in", "r", stdin);
freopen("out.out", "w", stdout);
	scanf("%d", &t);
	int cas = 1;
	while (t--) {
		printf("Case #%d: ", cas++);
		scanf("%s", ar + 1);
		bfs();
		int ans = min(dist[n][0][0], dist[n][0][1]);
		printf("%d\n", ans);
	}
}