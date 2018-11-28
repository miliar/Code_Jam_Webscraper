#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define forn(a,n) for(int a = 0; a<(n); ++a)
#define contains(mask, bit) ((mask & (1<<(bit))) != 0)

int T, r, c, m, mapa[8][8], vist[8][8];

const int DX[8] = {0,0,1,1,1,-1,-1,-1};
const int DY[8] = {1,-1,0,1,-1,0,1,-1};

int valor(int sx, int sy) {
	int ret = 0;
	forn(k,8) {
		int x = sx+DX[k], y = sy+DY[k];
		if(min(x,y) < 0 || x >= r || y >= c) continue;
		ret += mapa[x][y] != 0;
	}
	return ret;
}

void dfs(int sx, int sy) {
	if(vist[sx][sy]) return;
	vist[sx][sy] = 1;
	//cout << sx << " " << sy << endl;

	if(valor(sx,sy) == 0) {
		forn(k,8) {
			int x = sx+DX[k], y = sy+DY[k];
			if(min(x,y) < 0 || x >= r || y >= c) continue;
			dfs(x,y);
		}
	}
}

bool simul(int sx, int sy) {
	memset(vist,0,sizeof(vist));
	dfs(sx, sy);
	forn(i,r) forn(j,c) {
		if(mapa[i][j] == 0 && !vist[i][j])
			return false;
	}
	return true;
}

void imprimirMapa() {
	forn(i,r) {
		forn(j,c) {
			if(mapa[i][j] == 0) 
				printf(".");
			else if(mapa[i][j] == 1)
				printf("*");
			else
				printf("c");
		}
		printf("\n");
	}
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	cin >> T;
	forn(t,T) {
		cin >> r >> c >> m;
		bool ret = false;
		forn(mask, (1<<(r*c))) {
			if(__builtin_popcount(mask) != m) continue;
			forn(i,r) forn(j,c)
				mapa[i][j] = contains(mask, i*c+j);

			forn(i,r) {
				forn(j,c) {
					if(mapa[i][j] == 0 && simul(i,j)) {
						ret = true;
						mapa[i][j] = 2;
						break;
					}
				}
				if(ret) break;
			}
			if(ret) break;
		}

		printf("Case #%i:\n", t+1);
		if(ret) imprimirMapa();
		else printf("Impossible\n");
	}
}