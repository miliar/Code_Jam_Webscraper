#include <bits/stdc++.h>

#define rep(i,n) for(int i=0; i<n; i++)
#define repa(i,a,b,d) for(int i=a; i<=b; i+=d)
#define repd(i,a,b,d) for(int i=a; i>=b; i-=d)
#define repi(it,stl) for(auto it = (stl).begin(); (it)!=stl.end(); ++(it))
#define sz(a) ((int)(a).size())
#define mem(a,n) memset((a), (n), sizeof(a))
#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mp(a,b) make_pair((a),(b))
#define pii pair<int,int>
#define vi vector<int>
#define vs vector<string>
#define sstr stringstream
#define myfind(v,x) (find(all((v)),(x))-(v).begin())

typedef long long ll;
using namespace std;

ll c, f, x;
const double mul = 1e10;
int main()
{

#ifndef ONLINE_JUDGE
    freopen("code.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
#endif

    int tst;
    scanf("%d", &tst);
    repa(tt, 1, tst, 1) {
        double cc, ff, xx;
        scanf("%lf%lf%lf", &cc, &ff, &xx);
        c = (ll)(cc * mul);
        f = (ll)(ff * mul);
        x = (ll)(xx * mul);

        //t, n, r
        pair<ll, pair<ll, ll> > tmp = mp(0, mp(0, 0));
        priority_queue<pair<ll, pair<ll, ll> >, vector<pair<ll, pair<ll, ll> > >, greater<pair<ll, pair<ll, ll> > > > q;
        q.push(mp(0, mp(0, 2 * mul)));
        ll t, n, r;
        while(q.size()) {
            t = q.top().first;
            n = q.top().second.first;
            r = q.top().second.second;
            q.pop();
            if(n == x)
                break;

            //s1: finish
            ll nt = (ll)(((x - n + 0.0) / r) * mul);
            q.push(mp(t + nt, mp(x, r)));

            //s2: buy farm
            nt = (ll)(((c - n + 0.0) / r) * mul);
            q.push(mp(t + nt, mp(0, r + f)));
        }
        printf("Case #%d: %.7lf\n", tt, t / mul);

    }
    return 0;
}