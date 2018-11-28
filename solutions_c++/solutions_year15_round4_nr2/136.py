#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream ss;

#define sz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define mset(t,v) memset((t),(v),sizeof(t))
#define print(a) cout << #a << ": " << a << endl;
#define print_arr(a,n) rep(_##i, n) cout << #a << "[" << _##i << "]: " << a[_##i] << endl

#define rep(i,n) for(int i=0,_##i=(n);i<_##i;++i)
#define repr(i,n) for(int i=(n);--i>=0;)
#define rep2(i,l,r) for(int i=(l),_##i=(r);i<_##i;++i)
#define repr2(i,l,r) for(int i=(r),_##i=(l);--i>=_##i;)

#define vt(args...) vector<tuple<args>>
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define em emplace

int N;
double V, X;
typedef pair<double, double> pdd;
pdd src[100];

const double EPS = 1e-14;

bool ok(double t) {
    int i;
    double vol = 0;
    double temp = 0;

    if (src[0].first == src[N - 1].first) {
        if (X < src[0].first - EPS || X > src[0].first + EPS) {
            return false;
        }
        rep(j, N) vol += src[j].second;
        vol *= t;
        if (vol < V) return false;
        return true;
    }

    temp = 0;
    vol = V;
    for(i = 0; i < N; ++i) {
        if (t * src[i].second > vol) {
            temp += vol * src[i].first;
            vol = 0;
            break;
        } else {
            temp += t * src[i].second * src[i].first;
            vol -= t * src[i].second;
        }
    }
    if (i == N || temp > V * X + EPS) return false;

    temp = 0;
    vol = V;
    for(i = N - 1; i >= 0; --i) {
        if (t * src[i].second > vol) {
            temp += vol * src[i].first;
            vol = 0;
            break;
        } else {
            temp += t * src[i].second * src[i].first;
            vol -= t * src[i].second;
        }
    }
    if (i == -1 || temp < V * X - EPS) return false;
    return true;
}

void solve_case(int i) {
    cout << "Case #" << i << ": ";
    cin >> N >> V >> X;
    rep(i, N) {
        cin >> src[i].second >> src[i].first;
    }
    sort(src, src + N);

    double lo = 0;
    double hi = 1e10;

    rep(num, 200) {
        double mid = 0.5 * (lo + hi);
        if (ok(mid)) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    
    if (hi > 1e9) {
        cout << "IMPOSSIBLE\n";

    } else {
        cout << (0.5 * (lo + hi)) << "\n";
    }
}

int main(){
    int T;
    cin >> T;
    cout << fixed << setprecision(11);
    rep(i, T) solve_case(i + 1);
    return 0;
}

