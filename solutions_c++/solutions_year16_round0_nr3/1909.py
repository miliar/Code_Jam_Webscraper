# include <bits/stdc++.h>
# define ll long long
# define x first
# define y second
using namespace std;
ifstream fi("c.in");
ofstream fo("c.out");
const int lim = 1e3;
ll get_mod(ll mask,ll bs,ll mod,int to)
{
    ll t = 1;
    int ans = 0;
    for (int i = 0;i < to;++i,t = (t * bs) % mod)
        if ((mask >> i)&1) ans = (ans + t) % mod;
    return ans;
}
ll prim(ll mask,ll bs,int to)
{
    for (int i = 2;i <= lim;++i)
        if (!get_mod(mask,bs,i,to)) return i;
    return 1;
}
int main(void)
{
    int n = 32;
    int k = 500;
    vector < pair < ll , vector < ll > > > ans;
    for (ll i = 1ll << (n-1);k && i < (1ll << (n));++i)
    if (i&1)
    {
        cerr << i << '\n';
        vector < ll > w;
        bool Ok = 1;
        for (int t = 2;t <= 10;++t)
        {
            ll G = prim(i,t,n);
            if (G == 1) Ok = 0;
            w.push_back(G);
        }
        if (Ok) ans.push_back({i,w}),--k;
    }
    fo << "Case #1:\n";
    for (auto it : ans)
    {
        for (int cnt = n-1;cnt>=0;--cnt) if ((1ll << cnt) & it.x) fo << 1;
        else fo << 0;
        fo << ' ';
        for (auto j : it.y) fo << j << ' ';
        fo << '\n';
    }
    return 0;
}

