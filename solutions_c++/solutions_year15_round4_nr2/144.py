#include <bits/stdc++.h>
using namespace std;
#define ulong uint64_t
#define mt make_tuple
#define eb emplace_back
#define all(u) begin(u),end(u)
#define _overload3(_1,_2,_3,name,...) name
#define _rep(i,n) _repi(i,0,n)
#define _repi(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload3(__VA_ARGS__,_repi,_rep,)(__VA_ARGS__)
template<class C>void uniq(C&c){c.erase(unique(all(c)),end(c));}
template<class T>bool chmin(T&a,const T&b){return a>b&&(a=b,1);}
template<class T>bool chmax(T&a,const T&b){return a<b&&(a=b,1);}

int n;
double x, v;
vector<pair<double, double>> vec;

void input()
{
    cin >> n >> v >> x;
    vec.clear();
    rep(i, n) {
        double a, b;
        cin >> b >> a;
        vec.eb(a, b);
    }
    sort(all(vec));
}

const double eps = 1e-8;
const double inf = 1e18;

double lower()
{
    if (vec[0].first > x + eps) return 0.0;
    double sum = 0.0, srate = 0.0;
    rep(i, n) {
        double tem, rate;
        tie(tem, rate) = vec[i];
        if ((sum + tem * rate) / (srate + rate) > x - eps) {
            const double t = (x * srate - sum) / (tem - x) / rate;
            return srate + t * rate;
        }
        sum += tem * rate;
        srate += rate;
    }
    return 0.0;
}

double upper()
{
    if (vec[n-1].first < x - eps) return 0.0;
    double sum = 0.0, srate = 0.0;
    for (int i = n-1; i >= 0; --i) {
        double tem, rate;
        tie(tem, rate) = vec[i];
        if ((sum + tem * rate) / (srate + rate) < x + eps) {
            const double t = (x * srate - sum) / (tem - x) / rate;
            return srate + t * rate;
        }
        sum += tem * rate;
        srate += rate;
    }
    return 0.0;
}

void solve()
{
    double ans = 0.0;
    vector<pair<double, double>> tmp;
    rep(i, n) {
        if (abs(vec[i].first - x) < eps) {
            ans += vec[i].second;
        } else {
            tmp.eb(vec[i]);
        }
    }
    vec = move(tmp);
    n = vec.size();
    if (not vec.empty()) ans += max(lower(), upper());
    if (ans < eps) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << v / ans << endl;
    }
}

int main()
{
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(9);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        input();
        cout << "Case #" << i << ": ";
        solve();
    }
}
