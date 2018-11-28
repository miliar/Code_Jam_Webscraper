 #include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <utility>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define INF 2e9
#define pb push_back
#define mp make_pair
#define forn(i,n) for (int i = 0; i < n; i++)

using namespace std;

typedef long long ll;

ll n, m, t;
ll from, to, p;

struct event
{
    ll x, type, p;
    event() {}
    event (ll _x, ll _type, ll _p) {
        x = _x;
        type = _type;
        p = _p;
    }
};

ll f(ll l, ll r) {
    ll z = (r - l + 1);
    ll ans = z * n - ((z - 1) * z / 2);
    return ans;
}

bool operator < (const event & a, const event & b) {
    if (a.x != b.x) {
        return a.x < b.x;
    } else {
        return a.type > b.type;
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;

    forn (it, t) {
        vector <event> d;
        cin >> n >> m;
        ll ans = 0;
        forn (i, m) {
            cin >> from >> to >> p;
            d.pb(event(from, 1, p));
            d.pb(event(to, 0, p));
            ans += f(from, to) * p;
        }
        //cout << ">>" << ans << endl;
        sort(d.begin(), d.end());
        stack <event> s;
        ll res = 0;
        for (int i = 0; i < d.size(); i++) {
            if (d[i].type) {
                s.push(d[i]);
                //printf(">push ");
                //cout << d[i].type << " " << d[i].x << " " << d[i].p << endl;
            }
            else {
                //printf(">pop ");
                //cout << d[i].type << " " << d[i].x << " " << d[i].p << endl;
                while (d[i].p) {
                    event k = s.top();
                    if (d[i].p >= k.p) {
                        d[i].p -= k.p;
                        res += f(k.x, d[i].x) * k.p;
                        //cout << "add " << f(k.x, d[i].x) * k.p << endl;
                        s.pop();
                    } else {

                        k.p -= d[i].p;
                        res += f(k.x, d[i].x) * d[i].p;
                        d[i].p = 0;
                        //cout << "add " << f(k.x, d[i].x) * d[i].p << endl;

                        s.pop();
                        s.push(k);
                    }
                }
            }

        }
        //cout << res << " " << ans << endl;
        cout << "Case #" << it + 1 << ": " << ans - res << endl;
    }

    return 0;
}
