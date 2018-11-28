#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <bitset>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define pb push_back
#define mp make_pair
#define EPS 1.0e-8
#define INF 1000000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef long double ld;

ll b, m[100005];

ll haircuts(ll t) {
    ll ret = 0LL;
    FOR(i,0,b) {
        ret += t/m[i] + 1;
    }
    return ret;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    ll n, time, ans;
    ll lo, hi, mid;
    ll attended, attending, c;

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%lld %lld", &b, &n);
        FOR(i,0,b) scanf("%lld", &m[i]);

        lo = 0LL; hi = m[0]*n;
        while(hi - lo > 1LL){
            mid = (hi + lo) / 2;
            if (haircuts(mid) >= n) hi = mid;
            else lo = mid;
        }
        if (haircuts(lo) >= n) time = lo;
        else time = hi;

        if (time == 0LL) {
            printf("Case #%d: %lld\n", ncase, n);
            continue;
        }

        //printf("%lld\n", haircuts(0));
        attended = haircuts(time - 1);;
        //FOR(i,0,b) if ((time-1) % m[i] != 0) attending++;
        c = attended; //printf("%lld %lld\n", attended, attending);
        FOR(i,0,b) {
            if (time%m[i] == 0) {
                c++;
                if (c == n) {
                    ans = i + 1;
                    break;
                }
            }
        }

        printf("Case #%d: %lld\n", ncase, ans);
    }

    return 0;
}
