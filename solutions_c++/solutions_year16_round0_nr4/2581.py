#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define sd(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define debug(X) cerr << " --> " << #X << " = " << X << endl
#define rep(i, begin, end) for(__typeof(end) i =(begin)-((begin)>(end));i!=(end)-((begin)>(end));i+=1-2*((begin)>(end)))
#define endl "\n"
typedef long long ll; typedef pair<int, int> pii;
const int N = 1123456, lgN = 15, mod = 1000000007;
const double eps = 1e-3, pi = acos(-1.0);
int d[N];
vector<pair<vector<int>, vector<ll>>> ans;
int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("4.out", "w", stdout);

    int t;
    sd(t);
    for(int tt = 1; tt <= t ; ++tt)
    {
        printf("Case #%d: ", tt);
        ll k, c, s;
        scanf("%lld %lld %lld", &k, &c, &s);
        if(s == k)
        {
            ll p = 1;
            for(int i = 1; i <= c - 1; ++i)
                p *= k;
            for(int i = 1; i <= s; ++i)
            {
                printf("%lld ", i * p);
            }
            printf("\n");
        }
    }
    return 0;
}


