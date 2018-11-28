#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <climits>
#include <cstring>
#include <complex>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
typedef vector<int> vi;


#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define x first
#define y second
#define y1 y1_gdssdfjsdgf
#define y0 y0_fsdjfsdogfs
#define ws ws_fdfsdfsdgfs
#define image(a) {sort(all(a)),a.resize(unique(all(a))-a.begin());}
#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
#define problem_name "a"
int dstx(int a, int b, int c, int d) {
    if (b < c) {
        return max(0, c - b);
    } else {
        return max(0, a - d);
    }
}
bool inters(int a, int b, int c, int d) {
    return !(b < c || a > d);
}
int w, h, n;
int x1[10000];
int x2[10000];
int y1[10000];
int y2[10000];
int ds[10000];
int was[10000];

int d[2000][2000];
const int inf = (int)1e9;
int main(){
    #ifdef home
    assert(freopen(problem_name"2.out","wt",stdout));
    assert(freopen(problem_name".in","rt",stdin));
    #endif
    int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ti++) {
        printf("Case #%d: ", ti);
        scanf("%d %d %d", &w, &h, &n);
        for (int i = 1; i <= n; i++) {
            scanf("%d %d %d %d", &x1[i], &y1[i], &x2[i], &y2[i]);
            x2[i]++;
            y2[i]++;
        }
        x1[0] = 0;
        x2[0] = 0;
        y1[0] = 0;
        y2[0] = h;
        x1[n + 1] = w;
        x2[n + 1] = w;
        y1[n + 1] = 0;
        y2[n + 1] = h;
        for (int i = 0; i <= n + 1; i++) {
            for (int j = 0; j <= n + 1; j++) {
                d[i][j] = max(dstx(x1[i], x2[i], x1[j], x2[j]), dstx(y1[i], y2[i], y1[j], y2[j]));
            }
        }
        int ans = 0;
        for (int i = 0; i <= n + 1; i++) {
            ds[i] = inf;
            was[i] = 0;
        }
        ds[0] = 0;
        for (int it = 0; it <= n + 1; it++) {
            int mn = -1;
            for (int i = 0; i <= n + 1; i++) {
                if (was[i] == 0) {
                    if (mn == -1 || ds[mn] > ds[i]) {
                        mn = i;
                    }
                }
            }
            assert(mn != -1);            
            was[mn] = 1;
            if (mn == n + 1) {
                break;
            }
            for (int i = 0; i <= n + 1; i++) {
                ds[i] = min(ds[i], ds[mn] + d[mn][i]);
            }             
        }
        ans = ds[n + 1];
        printf("%d\n", ans);
    }
    return 0;
}
