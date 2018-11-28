#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
#define mp make_pair
#define N 123

int t, r, c, rc[N], cc[N], ans;
int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};
char gr[N][N];
bool ins(int y, int x) {
	return y < r && x < c && y >= 0 && x >= 0;
}
int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	fo(tc,1,t+1){
		printf("Case #%d: ", tc);
		ans = 0;
		fo(i,0,N) rc[i] = cc[i] = 0;
		scanf("%d %d", &r, &c);
		fo(i,0,r) scanf("%s", gr[i]);
		fo(i,0,r) fo(j,0,c) if (gr[i][j] != '.') rc[i]++, cc[j]++;
		fo(i,0,r) fo(j,0,c) {
			int cy = i, cx = j, dir;
			if (gr[i][j] == '.') continue;
			if (gr[i][j] == '>') dir = 0;
			else if (gr[i][j] == '<') dir = 1;
			else if (gr[i][j] == 'v') dir = 2;
			else dir = 3;
			do {
				if ((cy != i || cx != j) && gr[cy][cx] != '.') break;
				cy += dy[dir];
				cx += dx[dir];
			} while (ins(cy,cx));
			//printf("%d %d %d %d %c\n", i, j, cy, cx);
			if (!ins(cy,cx)) {
			//	printf("%d %d\n", i, j);
				if (rc[i]==1 && cc[j]==1) {
					puts("IMPOSSIBLE");
					goto end;
				}
				ans++;
			}
		}
		printf("%d\n", ans);
		end:;
	}

	return 0;
}