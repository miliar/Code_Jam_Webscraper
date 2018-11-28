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
    freopen("input.txt", "r", stdin);
    freopen("3.out", "w", stdout);

    int t;
    sd(t);
    for(int tt = 1; tt <= t ; ++tt)
    {
        printf("Case #%d:\n", tt);
        ll n, j;
        sl(n), sl(j);
        for(ll mask = 0; mask < (1LL << (n - 2)); ++mask)
        {
            vector<int> s = {1};
            for(int i = 0; i < n - 2; ++i)
            {
                ll z = 0;
                if(mask & (1LL << i))
                    z = 1;
                s.pb(z);
            }
            s.pb(1);
            bool add = true;
            vector<ll> v;
            for(int base = 2; base <= 10; ++base)
            {
                ll cur = 0;
                for(int i = 0; i < n; ++i)
                {
                    cur = (cur * base + s[i]);
                }
                bool prime = true;
                for(ll i = 2; i <= 100; ++i)
                {
                    if(cur % i == 0)
                    {
                        prime = false;
                        v.pb(i);
                        break;
                    }
                }
                if(prime)
                {
                    add = false;
                    break;
                }
            }
            if(add)
            {
                ans.push_back(make_pair(s, v));
            }
            if(ans.size() == j)
                break;
        }
        for(int i = 0; i < j; ++i)
        {
            for(int p : ans[i].F)
                printf("%d", p);
            printf(" ");
            for(int k = 0; k < 9; ++k)
                printf("%lld ", ans[i].S[k]);
            printf("\n");
        }
    }
    return 0;
}


