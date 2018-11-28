#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <random>
#include <set>
using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define PB push_back
typedef long long int64;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, -1, 0, 1};

int a[7][7], r, c;
set<int64> drum;

inline int64 hashvalue(int ofs) {
	int64 res = 0;
	REP(i, r)
	REP(j, c) res = res * 3 + a[i][(ofs+j)%c];
	return res;
}

inline void addSol() {
	REP(o, c) if (drum.count(hashvalue(o))) return;
	/*
	REP(i, r) {
		REP(j, c) printf("%d ", a[i][j]+1);
		puts("");
	}
	puts("");
	*/
	drum.insert(hashvalue(0));
}

inline bool check(int x, int y) {
	int num = a[x][y], cnt = 0;
	// printf("check, a[%d][%d] = %d\n", x, y, num);
	REP(d, 4) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		if (ny < 0) ny = c-1;
		if (ny == c) ny = 0;
		if (nx < 0 || nx >= r) continue;
		if (a[nx][ny] == num) ++cnt;
	}
	// printf("a[%d][%d], num = %d, cnt = %d\n", x, y, num, cnt);
	return (num+1 == cnt);
}

void dfs(int x, int y) {
	REP(i, 3) {
		a[x][y] = i;
		// printf("a[%d][%d] = %d\n", x, y, i);
		if (x > 0) if (!check(x-1, y)) continue;
		if (x == r-1 && y == c-1) {
			bool ok = 1;
			REP(j, c) if (!check(r-1, j)) {ok = 0; break;}
			if (ok) addSol();
		} else {
			int nx = x, ny = y;
			if (ny < c-1) ++ny;
			else {++nx; ny = 0;}
			dfs(nx, ny);
		}
	}
}

int main() {
	int nT;
	scanf("%d", &nT);
	FOR(cN, 1, nT) {
		scanf("%d%d", &r, &c);
		drum.clear();
		memset(a, -1, sizeof(a));
		dfs(0, 0);
		int ans = drum.size();
		printf("Case #%d: %d\n", cN, ans);
	}
}
