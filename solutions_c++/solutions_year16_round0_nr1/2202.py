#include <bits/stdc++.h>
using namespace std;
/* macros */
// memory
#define zeroset(A) memset((A), 0, sizeof((A)))
#define negset(A) memset((A), -1, sizeof((A)))
#define all(c) (c).begin(), (c).end()
#define pb push_back
// input & output
#define inpt(a) freopen(a,"r",stdin)
#define otpt(a) freopen(a,"w",stdout)
#define eol "\n"
// types
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<ll,ll> pll;
#define ff first
#define ss second
// constants
#define EPS 1e-9
#define MAXN 300005
#define INF INT_MAX
#define MOD 1000000007

int sum[MAXN];

int get_msk(int x){
    int ret = 0;
    while(x){
        ret |= (1 << (x%10));
        x/=10;
    }
    return ret;
}

int main()
{
    //ios::sync_with_stdio(false);
    //inpt("sample.in");
    inpt("A-large.in");
    otpt("A_large.out");
    int T;
    scanf("%d", &T);
    for(int ts = 1; ts<=T; ++ts){
        int n = ts;
        scanf("%d", &n);
        if(!n){
            printf("Case #%d: INSOMNIA\n", ts);
            continue;
        }
        int msk = get_msk(n), tmp = n;
        while(msk != (1 << 10)-1){
            tmp += n;
            msk |= get_msk(tmp);
        }
        printf("Case #%d: %d\n", ts, tmp);
    }
    return 0;
}
