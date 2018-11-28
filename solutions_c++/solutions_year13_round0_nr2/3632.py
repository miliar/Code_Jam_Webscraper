#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <memory.h>

using namespace std;
class pp{
public:
	pp(){}
	pp(int _v, int _r, int _c) {
		v = _v, r = _r, c = _c;
	}
	int v;
	int r, c;
	bool operator<(const pp& A ) const {
		return v < A.v;
	}
};

int test = 1;
int N, M;
int map[101][101];
vector<pp> G;

bool col(int v, int c) {
	for(int i=0; i<N; i++) if( v < map[i][c] ) return false;
	return true;
}
bool row(int v, int r) {
	for(int i=0; i<M; i++) if( v < map[r][i] ) return false;
	return true;
}

void solve() {
	G.clear();
	memset(map, 0, sizeof map);
	scanf("%d %d", &N, &M);
	for(int i=0; i<N; i++) {
		for(int j=0; j<M; j++) {
			scanf("%d", &map[i][j]);
			G.push_back(pp(map[i][j], i, j));
		}
	}
	sort(G.begin(), G.end());
	for(int i=0; i<G.size(); i++) {
		bool r = row(G[i].v, G[i].r);
		bool c = col(G[i].v, G[i].c);
		if( !r && !c ) {
			printf("Case #%d: NO\n", test++);
			return;
		}
	}
	printf("Case #%d: YES\n", test++);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int TC;
	scanf("%d", &TC);
	while(TC-- > 0) solve();
	return 0;
}