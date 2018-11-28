#include <bits/stdc++.h>
#include <sys/time.h>

using namespace std;

#define FI first
#define SE second
#define X first
#define Y second
#define ST first
#define ND second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef vector<int> VI;
typedef long double LD;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

double getTime() {
	timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec * 1e-6;
}

char t[105][105];
int h, w;

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};
const char dir[] = {'^', '>', 'v', '<'};

bool is_first(int y, int x, int d) {
    y += dy[d];
    x += dx[d];
    while (y >= 0 && y < h && x >= 0 && x < w) {
        if (t[y][x] != '.') {
            return false;
        }
        y += dy[d];
        x += dx[d];
    }
    return true;
}

void alg() {
    cin >> h >> w;
    REP (i, h) {
        REP (j, w) {
            cin >> t[i][j];
        }
    }
    int res = 0;
    REP (i, h) {
        REP (j, w) {
            if (t[i][j] == '.') {
                continue;
            }
            char lst = '.';
            int cnt = 0;
            REP (d, 4) {
                if (is_first(i, j, d)) {
                    if (lst != t[i][j]) {
                        lst = dir[d];
                    }
                    ++cnt;
                }
            }
            if (lst == t[i][j]) {
                if (cnt == 4) {
                    cout << "IMPOSSIBLE" << endl;
                    return;
                }
                ++res;
            }
        }
    }
    cout << res << endl;
}

int main() {
    int d;
    cin >> d;
    FOR (i, 1, d + 1) {
        cout << "Case #" << i << ": ";
        alg();
    }
}
