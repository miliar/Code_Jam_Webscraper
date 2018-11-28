#include <iostream>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <vector>
#include <cstring>
#include <cstdlib>

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define X first
#define Y second
#define next next_

using namespace std;

int n, m, b;
int A[511][511];
int e[511][511];
int pr[1000000];
int X[1000000];
int Y[1000000];
int next[1000000];
int Z[1000000];
int O[1000000];
int M;
int u[1000000];
int it;
int f[1000000];
int fl[1000000];
int rib[1000000];

void add_edge(int x, int y){
	M++;
	X[M] = x;
	Y[M] = y;
	next[M] = pr[x];
	pr[x] = M;
	Z[M] = 1;
	O[M] = 0;

	M++;
	X[M] = y;
	Y[M] = x;
	next[M] = pr[y];
	pr[y] = M;
	Z[M] = 0;
	O[M] = 0;
}

int main(){
	freopen("inputc1.in","r",stdin);
	freopen("outputc1.out","w",stdout);
	int T;
	cin >> T;
	for (int TT = 1; TT <= T; TT++){
		printf("Case #%d: ", TT);
		cin >> n >> m >> b;
		int E = 0;
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				E++;
				e[i][j] = E;
			}
		}
		memset(A, 0, sizeof(A));
		for (int i = 0; i < b; i++){
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int x = x1; x <= x2; x++){
				for (int y = y1; y <= y2; y++){
					A[x][y] = 1;
				}
			}
		}

		M = 1;
		memset(pr, 0, sizeof(pr));
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				if (A[i][j] == 0){
					add_edge(e[i][j] * 2, e[i][j] * 2 + 1);
				}
			}
		}

		for (int i = 0; i < n; i++){
			add_edge(0, e[i][0] * 2);
			add_edge(e[i][m - 1] * 2 + 1, 200000);
		}
		
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				for (int dx = -1; dx <= 1; dx++){
					for (int dy = -1; dy <= 1; dy++){
						if ((dx == 0) ^ (dy == 0)){
							if (i + dx < 0) continue;
							if (i + dx == n) continue;
							if (j + dy < 0) continue;
							if (j + dy == m) continue;
							add_edge(e[i][j] * 2 + 1, e[i + dx][j + dy] * 2);
						}
					}
				}
			}
		}

		int ans = 0;
		while (1){
			it++;
			int sz = 1;
			int i = 1;
			f[1] = 0;
			fl[1] = 0;
			while (i <= sz){
				if (f[i] == 200000){
					ans++;
					int j = i;
					while (fl[j] > 0){
						O[rib[j]]++;
						O[rib[j] ^ 1]--;
						j = fl[j];
					}
					break;
				}
				int j = pr[f[i]];
				while (j){
					if (Z[j] - O[j] > 0){
						if (u[Y[j]] != it){
							u[Y[j]] = it;
							sz++;
							f[sz] = Y[j];
							fl[sz] = i;
							rib[sz] = j;
						}
					}
					j = next[j];
				}
				i++;
			}
			if (i > sz) break;
		}
		cout << ans << endl;
	}
    return 0;
}
