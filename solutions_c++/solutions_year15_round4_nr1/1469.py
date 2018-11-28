#include <iostream>
#include <algorithm>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <ctime>
using namespace std;

#define rep(i, n) for (int i=0; i<(n); ++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define repd(i, a, b) for (int i=(a); i>=(b); --i)
#define clr(a, b) memset(a, b, sizeof(a))
#define sz(a) ((int)(a).size())

#define N 100

const char dir[] = ".^>v<";

int d[5][2] = {0,0,-1,0, 0,1, 1,0, 0,-1};
int a[N+10][N+10];
int n, m;

void test(int i, int j, bool ok[], int &cnt){
	repf(k, 1, 4){
		int x = i + d[k][0];
		int y = j + d[k][1];
		while (x >=1 && x<=n && y>=1 && y<=m){
			if (a[x][y] != 0){
				ok[k] = true;
				cnt ++;
				break;
			}
			x += d[k][0];
			y += d[k][1];
		}
	}	
}

int solve(){
	int ret = 0;
	bool ok[5];
	int cnt;
	repf(i, 1, n) 
		repf(j, 1, m) if (a[i][j]!=0){
			cnt = 0;		
			memset(ok, 0, sizeof(ok));

			test(i, j, ok, cnt);
			if (cnt == 0) return -1;
			if (!ok[a[i][j]]) ret++;
		}
	return ret;
}

int main(){
	int ts;
	scanf("%d", &ts);
	repf(te, 1, ts){
		scanf("%d%d", &n, &m);
		repf(i, 1, n) 
			repf(j, 1, m){
				char c = getchar();
				while (strchr(dir, c) == NULL)
					c = getchar();
				a[i][j] = strchr(dir, c) - dir;
			}
		int ans = solve();
		printf("Case #%d: ", te);
		if (ans<0)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
	return 0;
}
