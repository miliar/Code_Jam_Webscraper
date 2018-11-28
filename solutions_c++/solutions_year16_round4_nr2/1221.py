#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

double p[20];
double dp[20][20];

double check(vector<int> tmp) {
    int limit = tmp.size() / 2;
    int i, j, k;
    memset(dp, 0, sizeof(dp));
    dp[0][1] = p[tmp[0]];
    dp[0][0] = 1.0 - p[tmp[0]];
    xrep(i, 1, tmp.size()) {
        double pi = p[tmp[i]];
        xrep(j, 1, limit + 1) {
            dp[i][j] = dp[i-1][j-1] * pi + dp[i-1][j] * (1.0 - pi);
        }
        dp[i][0] = dp[i-1][0] * (1-pi);
    }
    double ans = dp[tmp.size()-1][limit];
    return ans;
}

int main() {
    int t, tt, i, j, jj;
    int n, k, x2;
    double ans;

    cin >> tt;
    xrep(t, 1, tt+1) {
        ans = -1;
        cin >> n >> k;
        rep(i, n) { cin >> p[i]; }
        x2 = Lshift(i, n);
        rep(i, x2) {
            vector<int> tmp;
            for (j = 0, jj = 1; j < n; j++, jj<<=1) {
                if (jj & i) { tmp.push_back(j); }
            }
            if (tmp.size() == k) {
                ans = max(ans, check(tmp));
            }
        }
        printf("Case #%d: %.10lf\n", t, ans);
    }
}
