#include <cstdio>
#include <algorithm>
#define N 105
#define fi(a, b, c) for(int a = (b); a < (c); a++)
#define fd(a, b, c) for(int a = (b); a > (c); a--)
#define FI(a, b, c) for(int a = (b); a <= (c); a++)
#define FD(a, b, c) for(int a = (b); a >= (c); a--)
#define fe(a, b, c) for(int a = (b); a; a = c[a])
using namespace std;

int t, n, m, map[128], dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1}, ans;
char s[N][N];

bool check(int y, int x, int d){
	if(y < 0 || y >= n || x < 0 || x >= m) return 0;
	if(map[s[y][x]] > -1) return 1;
	return check(y + dy[d], x + dx[d], d);
}

void solve(int tc){
	scanf("%d %d", &n, &m);
	fi(i, 0, n) scanf("%s", s[i]);
	
	ans = 0;
	fi(i, 0, n) fi(j, 0, m) if(map[s[i][j]] > -1){
		int dir = map[s[i][j]];
		if(check(i + dy[dir], j + dx[dir], dir)) continue;
		
		bool ok = 0;
		fi(k, 0, 4) if(check(i + dy[k], j + dx[k], k)){
			ok = 1;
			break;
		}
		
		if(ok) ans++;
		else{
			ans = -1;
			break;
		}
	}
	
	printf("Case #%d: ", tc);
	if(ans < 0) puts("IMPOSSIBLE");
	else printf("%d\n", ans);
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w+", stdout);
	
	fi(i, 0, 128) map[i] = -1;
	map['^'] = 0;
	map['>'] = 1;
	map['v'] = 2;
	map['<'] = 3;
	
	scanf("%d", &t);
	FI(z, 1, t) solve(z);
	scanf("\n");
}
