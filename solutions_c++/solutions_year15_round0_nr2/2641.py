#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define PB push_back
#define MP make_pair
#define REP(X,N) for(int X=0;X<N;X++)
#define REP2(X,L,R) for(int X=L;X<=R;X++)
#define DEP(X,R,L) for(int X=R;X>=L;X--)
#define CLR(A,X) memset(A,X,sizeof(A))
#define IT iterator
#define X first
#define Y second
#define lson l,m,o<<1
#define rson m+1,r,o<<1|1
using namespace std;
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;
const int MAXN = 1010;
int n;
int s[MAXN];

bool cmp(int a, int b) {
    return a > b;
}

int main() {
    ios::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cas = 1;
    cin >> t;
    while (t--) {
        cin >> n;
        int ans = INF;
        REP(i, n) cin >> s[i];
        sort(s, s+n, cmp);
        for (int i = 1; i <= 1010; i++) {
            int ret = 0;
            REP(j, n) {
                ret += (s[j]+i-1)/i - 1;
            }
            ans = min(ans, ret+i);
        }
        cout << "Case #" << cas ++ << ": ";
        cout << ans << endl;
    }
    return 0;
}
