#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
using namespace std;
int d[10];
int m()
{
    int ret = d[0];
    for(int i = 1; i < 10; i++)ret = min(ret, d[i]);
    return ret;
}
void upd(ll x)
{
    while(x != 0)
    {
        d[x%10]++;
        x/=10;
    }
}
int _main()
{
    ll n;
    cin >> n;
    ll x = n;
    if(n == 0)return -1;
    for(int i = 1; i <= 5e5; i++)
    {
        upd(x);
        if(m() >= 1)return x;
        x += n;
    }
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt;
    cin >> tt;
    for(int i = 1; i <= tt; i++)
    {
        memset(d, 0, sizeof(d));
        int x = _main();
        if(x != -1)cout << "Case #" << i << ": " << x << "\n";
        else cout << "Case #" << i << ": " << "INSOMNIA\n";
    }
    return 0;
}
