#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forr(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define fornr(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define forrr(i, f, t) for (int i = (int)(t)-1; i >= (int)(f); --i)
#define printvec(v) for (auto e : v) cout << e << ", "; cout << endl;
#define all(x) (x).begin(), (x).end()

using namespace std;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }

typedef long long ll;
ll cmax[20], cmin[20], jmax[20], jmin[20];

string C, J;
int N;
pair<ll, ll> best(int i);
pair<ll, ll> mb(ll cf, ll jf, int i) {
    ll ten = 1; forn(k, N-i-1) ten *= 10;
    if (cf == jf) {
        pair<ll, ll> b = best(i+1);
        b.first += cf * ten;
        b.second += cf * ten;
        return b;
    } else if (cf > jf) {
        return make_pair(cf * ten + cmin[i+1], jf*ten + jmax[i+1]);
    } else {
        return make_pair(cf * ten + cmax[i+1], jf*ten + jmin[i+1]);
    }
}

pair<ll, ll> best(int i) {
    if (i == N) return make_pair(0, 0);
    char Ci = C[i];
    char Ji = J[i];
    vector<pair<ll, ll>> sols;
    if (Ci == '?' && Ji == '?') {
        sols.push_back(best(i+1));
        sols.push_back(mb(0, 1, i));
        sols.push_back(mb(1, 0, i));
    } else if (Ci == Ji) {
        sols.push_back(mb(Ci-'0', Ji-'0', i));
    } else if (Ci == '?') {
        sols.push_back(mb(Ji-'0', Ji-'0', i));
        if (Ji > '0') sols.push_back(mb(Ji-'0'-1, Ji-'0', i));
        if (Ji < '9') sols.push_back(mb(Ji-'0'+1, Ji-'0', i));
    } else if (Ji == '?') {
        sols.push_back(mb(Ci-'0', Ci-'0', i));
        if (Ci > '0') sols.push_back(mb(Ci-'0', Ci-'0'-1, i));
        if (Ci < '9') sols.push_back(mb(Ci-'0', Ci-'0'+1, i));
    } else {
        sols.push_back(mb(Ci-'0', Ji-'0', i));
    }
    pair<ll, ll> b = sols[0];
    for (auto o : sols) {
        if (abs(o.first - o.second) < abs(b.first - b.second)) b = o;
        else if (abs(o.first - o.second) == abs(b.first - b.second)) {
            if (o.first < b.first) b = o;
            else if (o.first == b.first && o.second < b.second) b = o;
        }
    }
    return b;
}

int main()
{
    int T;
    cin >> T;
    cout.precision(8);
    for (int casenum = 1; casenum <= T; ++casenum) {
        cin >> C >> J;
        N = C.size();
        cmax[N] = cmin[N] = jmax[N] = jmin[N] = 0;
        ll ten = 1;
        fornr(i, N) {
            char Ci = C[i];
            char Ji = J[i];
            cmax[i] = cmax[i+1] + (Ci == '?' ? ten * 9 : ten * (Ci - '0'));
            cmin[i] = cmin[i+1] + (Ci == '?' ? 0 : ten * (Ci - '0'));
            jmax[i] = jmax[i+1] + (Ji == '?' ? ten * 9 : ten * (Ji - '0'));
            jmin[i] = jmin[i+1] + (Ji == '?' ? 0 : ten * (Ji - '0'));
            ten *= 10;
        }

        pair<ll, ll> b = best(0);
        ll c = b.first;
        ll j = b.second;
        /* cout << c << ' ' << j << endl; */
        fornr(i, N) {
            C[i] = '0' + c % 10;
            J[i] = '0' + j % 10;
            c /= 10;
            j /= 10;
        }

        cout << "Case #" << casenum << ": " << C << ' ' << J << endl;
    }
    return 0;
}

