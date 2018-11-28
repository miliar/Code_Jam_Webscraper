#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
#define FOR(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALL(c) (c).begin(), (c).end()

#define pr(x) do{cout << (#x) << " = " << (x) << endl;}while(0)
#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
const int INF = 1001001001;
const llint INFll = 9008007006005004003ll;

typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

int st[128][128];

int main() {
	int T = in();
	for (int t = 1; t <= T; t++) {
		rep(i,128)rep(k,128)st[i][k] = 0;
		int R = in();
		int C = in();
		
		for (int r = 1; r <= R; r++) {
			for (int c = 1; c <= C; c++) {
				char inc;
				scanf(" %c", &inc);
				st[r][c] = inc;
			}
		}
		
		int ans = 0;
		for (int r = 1; r <= R; r++) {
			for (int c = 1; c <= C; c++) {
				char inc = st[r][c];
				if (inc == 0) assert(0);
				if (inc == '.') continue;
				
				int dx = 0, dy = 0;
				if (inc == '^') dy = -1;
				else if (inc == 'v') dy = 1;
				else if (inc == '>') dx = 1;
				else if (inc == '<') dx = -1;
				else assert(0);
				
				bool danger = false;
				for (int y = r + dy, x = c + dx; ; y += dy, x += dx) {
					if (st[y][x] == 0) {
						danger = true;
						goto END;
					}
					else if (st[y][x] != '.') {
						goto END;
					}
				}
				
				END:;
				if (danger) ans++;
				int dxs[] = {0, 1, 0, -1};
				int dys[] = {1, 0, -1, 0};
				bool ok = false;
				for (int dir = 0; dir < 4; dir++) {
					int dx = dxs[dir];
					int dy = dys[dir];
					for (int y = r + dy, x = c + dx; ; y += dy, x += dx) {
						if (st[y][x] == 0) {
							goto NEXTDIR;
						}
						else if (st[y][x] != '.') {
							ok = true;
							goto END2;
						}
					}
					NEXTDIR:;
				}
				END2:;
				if (! ok) {
					ans = -1;
					goto OUTPUT;
				}
			}
		}
		OUTPUT:;
		printf("Case #%d: ", t);
		if (ans >= 0) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
