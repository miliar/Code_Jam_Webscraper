#include <bits/stdc++.h>

using namespace std;

int i,j,x,y,t,n,m,tes;
char s[1007][1007];
bool valid;
int a[1007];

int convert(int x, int y) {
	if (x == 0) return y;
	if (y > m) return m + x;
	if (x > n) return m + n + (m + 1) - y;
	return m + n + m + (n + 1) - x;
}

// 0 : ATAS
// 1 : KANAN
// 2 : BAWAH
// 3 : KIRI
int nyan(int x, int y, int arah) {
	if (x < 1 || y < 1 || x > n || y > m) return convert(x,y);
	if (arah == 0) {
		if (s[x][y] == '/') return nyan(x,y-1,1); else return nyan(x,y+1,3);
	}
	if (arah == 1) {
		if (s[x][y] == '/') return nyan(x+1,y,0); else return nyan(x-1,y,2);
	}
	if (arah == 2) {
		if (s[x][y] == '/') return nyan(x,y+1,3); else return nyan(x,y-1,1);
	}
	if (arah == 3) {
		if (s[x][y] == '/') return nyan(x-1,y,2); else return nyan(x+1,y,0);
	}
}

void DFS(int x, int y) {
	if (!valid) {
		if (y > m) {
			if (x == n) {
				bool done = true;
				int i,j;
				
				for (i=1 ; i<=n ; i++) {
					for (j=1 ; j<=m ; j++) {
						if (i == 1) {
							if (a[convert(0,j)] != nyan(i,j,0)) done = false;
						}
						if (i == n) {
							if (a[convert(n+1,j)] != nyan(i,j,2)) done = false;
						}
						if (j == 1) {
							if (a[convert(i,0)] != nyan(i,j,3)) done = false;
						}
						if (j == m) {
							if (a[convert(i,m+1)] != nyan(i,j,1)) done = false;
						}
					}
				}
				
				if (done) {
					for (i=1 ; i<=n ; i++) {
						for (j=1 ; j<=m ; j++) printf("%c",s[i][j]);
						printf("\n");
					}
					valid = true;
				}
			} else {
				DFS(x+1,1);
			}
		} else {
			s[x][y] = '/';
			DFS(x,y+1);
			s[x][y] = '\\';
			DFS(x,y+1);
		}
	}
}

int main() {
	scanf("%d",&t);
	for (tes=1 ; tes<=t ; tes++) {
		scanf("%d%d",&n,&m);
		for (i=1 ; i<=n+m ; i++) {
			scanf("%d%d",&x,&y);
			a[x] = y;
			a[y] = x;
		}
		
		valid = false;
		printf("Case #%d:\n",tes);
		DFS(1,1);
		if (!valid) printf("IMPOSSIBLE\n");
	}
}