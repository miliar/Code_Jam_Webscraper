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

int vis[20];
VI ans;
int main()
{

    int T;
    for(int t = scanf("%d", &T); t <= T; t++) {
        int n;
        SET(vis, 0);
        ans.clear();
        scanf("%d", &n);
        n--;
        REP(i, 4) REP(j, 4) {
            int u;
            scanf("%d", &u);
            if(i == n)
                vis[u] = 1;
        }
        scanf("%d", &n);
        n--;
        REP(i, 4) REP(j, 4) {
            int u;
            scanf("%d", &u);
            if(i == n && vis[u] == 1)
                ans.pb(u);
        }
        printf("Case #%d: ", t);
        if(ans.size() == 1)
                cout<<ans[0]<<endl;
         else if(ans.size() == 0)
            puts("Volunteer cheated!");
        else puts("Bad magician!");
    }
    return 0;
}
