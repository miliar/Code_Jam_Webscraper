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
const ll inf = 1e18 + 100;
ll val(string s)
{
    ll v = 0;
    for(int i = 0; i < s.size(); ++i)
    {
        v = v * 10 + s[i] - '0';
    }
    return v;
}
ll lub(ll a, set<ll> b)
{
    auto it = b.lower_bound(a);
    if(it != b.end())
        return *it;
    return inf;
}
ll glb(ll a, set<ll> b)
{
    auto it = b.lower_bound(a);
    if(it != b.begin())
        return *(--it);
    return -inf;
}
string str(ll a, int s)
{
    string ret = "";
    for(int i = 0; i < s; ++i)
        ret += '0';
    for(int i = s - 1; a > 0; --i)
    {
        ret[i] = a % 10 + '0';
        a /= 10;
    }
    return ret;
}
int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("1.out", "w", stdout);

    int t;
    sd(t);
    for(int tt = 1; tt <= t ; ++tt)
    {
        printf("Case #%d: ", tt);
        string c, j;
        cin >> c >> j;
        ll m = 1, n = 1;
        for(int i = 0; i < c.size(); ++i)
        {
            if(c[i] == '?')
                m *= 10;
            if(j[i] == '?')
                n *= 10;
        }
        --m, --n;
        string cur = c;
        set<ll> x, y;
        ll ans = inf, a = 0, b = 0, cc = 0, jj = inf;
        while(a <= m || b <= n)
        {
            for(int p = 0; p < 1000, a <= m; ++a, ++p)
            {
                ll z = a;
                for(int i = 0; i < c.size(); ++i)
                {
                    if(c[i] != '?')
                        cur[i] = c[i];
                    else
                        cur[i] = z % 10 + '0', z /= 10;
                }
                ll v = val(cur);
                x.insert(v);
                if(ans > lub(v, y) - v || (ans == lub(v, y) - v && v < cc) || (ans == lub(v, y) - v && v == cc && lub(v, y) < jj))
                {
                    ans = lub(v, y) - v, cc = v, jj = lub(v, y);
                }
                if(ans > v - glb(v, y) || (ans == v - glb(v, y) && v < cc) || (ans == v - glb(v, y) && v == cc && glb(v, y) < jj))
                {
                    ans = v - glb(v, y), cc = v, jj = glb(v, y);
                }

            }
            for(int p = 0; p < 1000, b <= n; ++b, ++p)
            {
                ll z = b;
                for(int i = 0; i < j.size(); ++i)
                {
                    if(j[i] != '?')
                        cur[i] = j[i];
                    else
                        cur[i] = z % 10 + '0', z /= 10;
                }
                ll v = val(cur);
                y.insert(v);
                if(ans > lub(v, x) - v || (ans == lub(v, x) - v && lub(v, x) < cc) || (ans == lub(v, x) - v && lub(v, x) == cc && v < jj))
                {
                    ans = lub(v, x) - v, jj = v, cc = lub(v, x);
                }
                if(ans > v - glb(v, x) || (ans == v - glb(v, x) && glb(v, x) < cc) || (ans == v - glb(v, x) && glb(v, x) == cc && v < jj))
                {
                    ans = v - glb(v, x), jj = v, cc = glb(v, x);
                }
            }
            if(ans == 0)
                break;
        }
        cout<<str(cc, c.size())<<" "<<str(jj, c.size())<<"\n";
    }
    return 0;
}



