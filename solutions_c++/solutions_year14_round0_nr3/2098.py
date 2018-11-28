#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)

int T, n, m, k;
char a[55][55];
bool b[55][55];
int c[55][55], q[101010][2], f, r;

const int dx[] = {0, 0, 1,-1,-1, 1,-1, 1};
const int dy[] = {1,-1, 0, 0, 1, 1,-1,-1};

bool check(int r1, int c1, int r2, int c2) {
	//if (n-r1==1 && c1 > 1) return false;
	//if (m-c2==1 && r2 > 1) return false;
	rep(i, n+2) rep(j, m+2) {
	    a[i][j] = '.'; b[i][j] =false; c[i][j] = 0;
	}
	kep(i, n) kep(j, m) a[i][j] = '*';
	kep(i, r1) kep(j, c1) a[i][j] = '.';
	kep(i, r2) kep(j, c2) a[i][j] = '.';
	kep(i, n) kep(j, m) {
		b[i][j] = true;
		rep(k, 8) c[i][j] += a[i+dx[k]][j+dy[k]] == '*';
	}
	q[1][0] = q[1][1] = 1; f=(r=1)-1;
	int x, y; b[1][1] = false;
	while (++f<=r) {
		x = q[f][0]; y = q[f][1];
		if (c[x][y]) continue;
		rep(k, 8) if (a[x+dx[k]][y+dy[k]] == '.' && b[x+dx[k]][y+dy[k]]) {
			b[x+dx[k]][y+dy[k]] = false;
			q[++r][0] = x+dx[k];
			q[r][1] = y+dy[k];
		}
	}
	return (r == k);
}

void solve() {
	scanf("%d%d%d", &n, &m, &k);
	if (k == 0) {
		//rep(i, n-1) { rep(i, m) putchar('.'); puts(""); }
		//rep(i, m-1) putchar('.'); puts("c");
		puts("Yes");
		return;
	}
	k = n*m-k;
	for (int r1 = 1; r1 <= n && r1 <= k; r1++)
		for(int c1 = 1; c1 <= m && r1 * c1 <= k; c1++)
			for (int r2 = 1; r2 <= r1 && r2 <= k; r2++) {
				int c2=(k+r2*c1-r1*c1)/r2;
                if (c2 <= m && r1*c1+r2*(c2-c1)== k && check(r1,c1,r2,c2)) {
                    a[1][1] = 'c';
                    /*kep(i, n) {
                        kep(j, m) putchar(a[n+1-i][m+1-j]);
                        putchar('\n');
                    }*/
                    puts("Yes");
                    return;
                }
			}
	puts("Impossible");
}

int main() {
	freopen("C-small-attempt3.in", "r", stdin);
    freopen("C-small-attempt3.ou", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d:\n", _);
		solve();
	}
}
