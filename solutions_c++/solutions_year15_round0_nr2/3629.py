#include <bits/stdc++.h>
#define fr(i,a,b) for(int i = (a), __ = (b); i < __; ++i)
#define frr(i,a,b) for(int i = (a), __ = (b); i >= __; --i)
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define cl(a,b) memset(a, b, sizeof a)
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d %d", &a, &b)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

const int inf = 1000000000;

int main() {
    int T; scanf("%d", &T);
    for(int cases = 1; cases <= T; ++cases) {
        vi vec;
        int mx = 0;
        int D; scanf("%d", &D);
        fr(i,0,D) {
            int a; scanf("%d", &a);
            vec.pb(a);
            mx = max(mx, a);
        }
        int n = (int)vec.size();
        int ret = inf;
        for(int mn = mx; mn >= 1; --mn) {
            int espera = 0;
            fr(i,0,n) 
                if(vec[i] > mn) 
                    espera += ((vec[i]-mn)+(mn-1))/mn;
            ret = min(ret, espera+mn);
        }
        printf("Case #%d: %d\n", cases, ret);
    }
    return 0;
}