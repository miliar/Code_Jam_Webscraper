//Template update date: 20140316
#include <iostream>
#include <sstream>
#include <cstdio>
#include <climits>
#include <ctime>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <queue>
#include <algorithm>
#define  esp 1e-6
#define  pi acos(-1.0)
#define  inf 0x0f0f0f0f
#define  pb push_back
#define  lson l, m, rt<<1
#define  rson m+1, r, rt<<1|1
#define  lowbit(x) (x&(-x))
#define  mp(a, b) make_pair((a), (b))
#define  in  freopen("solve_in.txt", "r", stdin);
#define  out freopen("solve_out.txt", "w", stdout);

#define  bug puts("********))))))");
#define  inout in out

#define  SET(a, v) memset(a, (v), sizeof(a))
#define  READ(a, n) {REP(i, n) cin>>(a)[i];}
#define  REP(i, n) for(int i = 0; i < (n); i++)
#define  Rep(i, base, n) for(int i = base; i < n; i++)
#define  REPS(i, s) for(int i = 0; s[i]; i++)
#define  pf(x) ((x)*(x))
#define  Log(a, b) (log((double)b)/log((double)a))
#define Srand() srand((int)time(0))
#define random(number) (rand()%number)
#define random_range(a, b) (int)(((double)rand()/RAND_MAX)*(b-a) + a)

using namespace std;

typedef long long  LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<PII, int> VIII;
typedef VI:: iterator IT;
typedef map<string, int> Mps;
typedef map<int, int> Mpi;
typedef map<int, PII> Mpii;
typedef map<PII, int> Mpiii;
int dblcmp(double x)
{
    if(fabs(x) < esp)
        return 0;
    return x > 0 ? 1 : -1;
}
int main()
{

    int T;
    double ans, x, f, r, c, temp;
    for(int t = scanf("%d", &T); t <= T; t++) {
        scanf("%lf%lf%lf", &c, &f, &x);
        ans = inf, temp = 0;
        r = 2.0;
        if(dblcmp(c - x) >= 0) {
            printf("Case #%d: %.7f\n", t, x/r);
            continue;
        }
        while(1) {
            ans = min(ans, temp+x/r);
            temp += c/r;
            r += f;
            if(dblcmp(temp-ans) > 0)
                break;
        }
        printf("Case #%d: %.7f\n", t, ans);
    }
    return 0;
}
