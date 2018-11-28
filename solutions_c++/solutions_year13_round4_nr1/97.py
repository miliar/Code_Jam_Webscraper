#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
typedef double du;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)
const int MAXN = 1004;
const int MOD = 1000002013;

int n;

int f(int k, int p){
    return ((ll)n-k+1+n)*k/2%MOD*p%MOD;
}

pair<int, int> q[MAXN*2];
pair<int, int> s[MAXN*2];

int main()
{
    #ifdef __FIO
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    int T, i0;
    scanf("%d", &T);
    for(i0 = 1; i0 <= T; i0++){
        printf("Case #%d: ", i0);
        int m;
        int i, j, k;
        int ans = 0;
        scanf("%d%d", &n, &m);
        for(i = 0; i < m; i++){
            int o, e, p;
            scanf("%d%d%d", &o, &e, &p);
            s[i] = mp(o, -p);
            s[i+m] = mp(e, p);
            ans = (ans+f(e-o, p))%MOD;
        }
        sort(s, s+2*m);
        k = 0;
        for(i = 0; i < 2*m; i++){
            s[i].se *= -1;
            if(s[i].se > 0){
                q[k++] = s[i];
            }
            else{
                s[i].se = -s[i].se;
                while(k > 0 && q[k-1].se <= s[i].se){
                    ans = (ans-f(s[i].fi-q[k-1].fi, q[k-1].se))%MOD;
                    s[i].se -= q[k-1].se;
                    k--;
                }
                if(s[i].se > 0){
                    ans = (ans-f(s[i].fi-q[k-1].fi, s[i].se))%MOD;
                    q[k-1].se -= s[i].se;
                }
            }
        }
        ans = (ans+MOD)%MOD;
        printf("%d\n", ans);
    }
    return 0;
}
