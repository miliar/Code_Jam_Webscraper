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
const int N = 1005, lgN = 15, mod = 1000000007;
const double eps = 1e-3, pi = acos(-1.0);
const ll inf = 1e18 + 100;
string f[N], s[N];
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("1.out", "w", stdout);

    int t;
    sd(t);
    for(int tt = 1; tt <= t ; ++tt)
    {
        printf("Case #%d: ", tt);
        int n;
        sd(n);
        for(int i = 0; i < n; ++i)
            cin>>f[i]>>s[i];
        int l = (1 << n) - 1;
        set<string> x, y;
        int ans = 0;
        for(int m = 0; m <= l; ++m)
        {
            bool flag = true;
            x.clear(), y.clear();
            int z = l - m;
            for(int i = 0; i < n; ++i)
            {
                if(z & (1 << i))
                {
                    x.insert(f[i]), y.insert(s[i]);
                }
            }
            for(int i = 0; i < n; ++i)
            {
                if(m & (1 << i))
                {
                    if(x.find(f[i]) == x.end() || y.find(s[i]) == y.end())
                    {
                        flag = false;
                        break;
                    }
                }
            }
            if(flag)
                ans = max(ans, __builtin_popcount(m));
        }
        printf("%d\n", ans);
    }
    return 0;
}



