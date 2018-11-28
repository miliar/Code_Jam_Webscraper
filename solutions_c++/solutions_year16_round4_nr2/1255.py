#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
using namespace std;
const int maxn = 17;
int n, k;
long double p[maxn];
vector <int> bit[maxn];
long double ans;
void _main()
{
    cin >> n >> k;
    for(int i = 0; i < maxn; i++)bit[i].clear();
    for(int i = 0; i < 1 << (n); i++)bit[__builtin_popcount(i)].pb(i);
    for(int i = 0; i < n; i++)cin >> p[i];
    for(int i : bit[k])
    {
        long double tmp = 0;
        for(int j : bit[k/2])
        {
            if((i | j) == i)
            {
                long double cur = 1;
                for(int l = 0; l < n; l++)if((1 << l) & i)
                {
                    if((1 << l) & j)cur *= p[l];
                    else cur *= (1-p[l]);
                }
                tmp += cur;
            }
        }
        ans = max(ans, tmp);
    }
}
int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("B-small-attempt0(3).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt; cin >> tt;
    for(int i = 1; i <= tt; i++)
    {
        ans = 0;
        _main();
        cout << fixed << setprecision(12);
        cout << "Case #" << i << ": " << ans << "\n";
    }
    return 0;
}
