//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>   //我是沙茶....今天又写搓了。。
#include <fstream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <climits>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <utility>
#include <cctype>
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define abs(x) ((x)>0?(x):(-(x)))
#define FOR(i,a,b) for(int i = (a);i<=(b);i++)
#define FORD(i,a,b) for(int i = (a);i>=(b);i--)
#define REP(i,n) for(int i = 0;i<(n);i++)
#define rst(x,k) memset(x,k,sizeof(x))
#define lowbit(x) ((x)&(-(x)))
#define h(x) (1<<(x))
#define lson (ind<<1)
#define rson (ind<<1|1)
#define eps 1e-9
#define INF 15000000
#define maxn 2000000
#define mod  1000000007LL
#define HASHMOD 3894229
#define Pi acos(-1.0)
#define link fjksldfjaslkdfjas
#define y1 fksjdlf
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

int iCase;
int n;
double v, x;
double r[110], c[110];
int zero(double fuck) {
    if(abs(fuck) < eps) return 0;
    if(fuck > 0) return 1;
    else return -1;
}
void solve(void) {
    iCase ++;
    scanf("%d%lf%lf", &n, &v, &x);
    for(int i = 0;i < n;i ++) scanf("%lf%lf", r + i, c + i);
    if(n == 1) {
        if(zero(c[0] - x) == 0) {
            printf("Case #%d: %.9lf\n", iCase, v / r[0]);
        }else {
            printf("Case #%d: IMPOSSIBLE\n", iCase);
        }
    }else if(n == 2) {
        double t0, t1;
        if(zero(c[0] - c[1]) == 0) {
            if(zero(c[0] - x) == 0) {
                printf("Case #%d: %.9lf\n", iCase, v / (r[0] + r[1]));
            }else {
                printf("Case #%d: IMPOSSIBLE\n", iCase);
            }
        }else {
            t0 = v * (x - c[1]) / r[0] / (c[0] - c[1]);
            t1 = (v - r[0] * t0) / r[1];
            if(zero(t0) < 0 || zero(t1) < 0) {
                printf("Case #%d: IMPOSSIBLE\n", iCase);
            }else {
                printf("Case #%d: %.9lf\n",iCase,  max(t0, t1));
            }
        }
    }
}

int main(void) {
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    iCase = 0;
    int casenum; scanf("%d", &casenum);
    while(casenum --) solve();
    return 0;
}
