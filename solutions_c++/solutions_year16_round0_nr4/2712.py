#include <bits/stdc++.h>
#include <windows.h>

#define f first
#define s second
#define ll long long
#define ld long double
#define pb push_back
#define files1 freopen("input.txt","r",stdin)
#define files2 freopen("output.txt","w",stdout)
#define mp make_pair
#define fast_io ios_base::sync_with_stdio(0);
#define forn() for(int i=0;i<n;i++)
#define vi vector<int>

using namespace std;

const int inf=2e9;
const double eps=1e-9;
const int maxn = 1e6;

void solve()
{
    int k, c, s;
    scanf("%d %d %d", &k, &c, &s);
    vector<ll> ans;
    ll x = 1;
    for (int i=1;i<c;i++)
        x *= k;
    for (int i=0;i<s;i++){
        ans.pb(x * i + 1LL);
    }
    for (int i=0;i<ans.size();i++){
        printf("%I64d", ans[i]);
        if (i + 1 != ans.size()){
            printf(" ");
        }
    }
    puts("");
}
int main()
{
    srand(time(0));
    files1;
    files2;
    int t;
    //fast_io;
    //cin.tie(0);
    scanf("%d", &t);
    for (int i=1;i<=t;i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
