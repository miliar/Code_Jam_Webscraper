#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <iomanip>
#include <functional>
#include <cstdlib>
#include <climits>
#include <cctype>
using namespace std;
#define REP(i,x) for(int i = 0; i < (x); i++)
#define DEP(i,x) for(int i = (x) - 1; i >= 0; i--)
#define FOR(i,x) for(__typeof(x.begin())i=x.begin(); i!=x.end(); i++)
#define set(a,x) memset(a, x, sizeof(a))
#define mo(a,b) (((a)%(b)+(b))%(b))
#define ALL(x) (x).begin(), (x).end()
#define SZ(v) ((int)v.size())
#define UNIQUE(v) sort(ALL(v)); v.erase(unique(ALL(v)), v.end())
#define out(x) cout << #x << ": " << x << endl;
#define fastcin ios_base::sync_with_stdio(0);cin.tie(0);
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;
typedef vector<int> VI;
#define inf 0x3f3f3f3f
#define MOD 1000000007
#define eps 1e-8
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define IT iterator
#define X first
#define Y second
// ************************************************************************

ll fa(ll n) {
    ll h = sqrt(n);
    for (ll i = 2; i <= h; i++)
        if (n % i == 0) return i;
    return 0;
}

ll cal(ll n, ll base) {
    ll rt = 0, cnt = 1;
    while (n) {
        rt += (n & 1) * cnt;
        cnt *= base;
        n >>= 1;
    }
    return rt;
}

int main() {
#ifdef MANGOGAO
    freopen("/Users/Lodour/Downloads/C-small-attempt1.in", "r", stdin);
    // freopen("/Users/Lodour/Downloads/C-large.in", "r", stdin);
    // freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
#endif


    int t, cnt = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d:\n", ++cnt);
        int N, J;
        scanf("%d%d", &N, &J);
        ll last = (1LL << (N - 1)) - 1;
        ll base = (1LL << (N - 1)) + 1;
        int cc = 0;
        for (ll i = 0; i <= last; i++) {
            if (cc == J) break;
            ll cur = base + (i << 1);

            // out(cur);

            bool correct = 1;
            ll facts[10];
            for (ll j = 2; correct && j <= 10; j++) {
                // out(j)
                ll tar = cal(cur, j);
                // out(tar)
                ll fact = fa(tar);
                // out(fact)
                if (fact) facts[j - 2] = fact;
                else correct = 0;
            }
            if (correct) {
                cc++;
                char s[32]; int num = 0;
                while (cur) {
                    s[num++] = cur & 1 ? '1' : '0';
                    cur >>= 1;
                }
                for (int j = num - 1; j >= 0; j--)
                    putchar(s[j]);
                for (int j = 0; j <= 8; j++)
                    printf(" %lld", facts[j]);
                puts("");
            }
        }
    }

}
