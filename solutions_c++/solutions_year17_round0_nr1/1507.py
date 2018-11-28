#include <bits/stdc++.h>

#define rep(i, j, k) for(int i = (int) j; i < (int) k; ++i)
#define sz(x) ((int) (x).size())
#define ll long long
#define mp make_pair
#define pii pair<int, int >
#define fi first
#define se second
#define pb push_back
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f
#define zero(x) memset((x), (0), sizeof (x))
#define zerox(x, y) memset((x), (y), sizeof (x))

using namespace std;
const int N = 1010;

int k;
char s[N];

int main()
{
#ifdef PIT
freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);
#endif // PIT

    int T, ic = 1;
    for(scanf("%d", &T); T--; ic++){
        scanf("%s", s);
        scanf("%d", &k);
        int n = strlen(s);
        int step = 0;
        for(int i = 0; i <= n-k; ++i) if(s[i] == '-') {
            for(int j = 0; j < k; ++j) {
                if(s[i+j] == '+') s[i+j] = '-';
                else s[i+j] = '+';
            }
            ++step;
        }
        int flag = 1;
        for(int i = 0; i < n; ++i) if(s[i] == '-') {
            flag = 0;
            break;
        }
        if(flag) printf("Case #%d: %d\n", ic, step);
        else printf("Case #%d: IMPOSSIBLE\n", ic);
    }
    return 0;
}
