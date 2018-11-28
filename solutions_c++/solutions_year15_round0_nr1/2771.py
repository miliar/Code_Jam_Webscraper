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
const int MAXN = 1000010;

int sum[MAXN];

int main() {
    ios::sync_with_stdio(false);
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    int t;
    int cas = 1;
    cin >> t;
    while (t--) {
        cout << "Case #" << cas++ << ": ";
        int n, ans = 0;
        cin >> n;
        string s;
        cin >> s;
        int len = s.length();
        sum[0] = s[0] - '0';
        REP2(i, 1, len) {
            if (s[i] == '0')
                sum[i] = sum[i-1];
            else {
                if (sum[i-1] >= i) {
                    sum[i] = sum[i-1] + s[i] - '0';
                } else {
                    ans += i - sum[i-1];
                    sum[i] = sum[i-1] + s[i] - '0' + ans;
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}
