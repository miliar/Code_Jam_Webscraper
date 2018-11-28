#define TASKNAME "text"

#include <bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define sz(a) (int)a.size()
#define fst first
#define snd second
#define y1 osrughosduvgarligybakrybrogvba
#define y0 aosfigdalrowgyalsouvgrlvygalri                               
#define mp make_pair
#define pb push_back
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
 
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <bool> vb;
typedef vector <ll> vll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <int, ll> pil;
typedef vector <pii> vpii;

template <typename T>
T sqr(T x) {
    return x * x;
}

template <typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

const double EPS = 1e-12;
const int INF = 1e9;
const ll INFLONG = (ll)1e18;

bool check(double v, double x, vector<double> &r, vector<double> &c, double M) {
    double maxV = 0;
    for (int i = 0; i < sz(r); i++) {
        maxV += M * r[i];
    }
    //std::cerr << M << " " << v << " " << maxV << '\n';
    if (maxV < v - EPS) {
        return 0;
    }

    vector<pair<double, double>> p;
    for (int i = 0; i < sz(r); i++) {
        p.pb(mp(c[i], r[i]));
    }
    sort(all(p));

    double nowt = p[0].fst;
    double nowv = min(v, p[0].snd * M);
    for (int i = 1; i < sz(p); i++) {
        double add = min(v - nowv, p[i].snd * M);
        if (add <= EPS) {
            break;
        }
        nowt = (nowv * nowt + p[i].fst * add) / (nowv + add);
        nowv += add;
    }
    if (nowt >= x + EPS) {
        return 0;
    }

    reverse(all(p));
    
    nowt = p[0].fst;
    nowv = min(v, p[0].snd * M);
    for (int i = 1; i < sz(p); i++) {
        double add = min(v - nowv, p[i].snd * M);
        if (add <= EPS) {
            break;
        }
        nowt = (nowv * nowt + p[i].fst * add) / (nowv + add);
        nowv += add;
    }
    return (nowt >= x - EPS);
}

int main()
{
    freopen(TASKNAME".in", "r", stdin);
    freopen(TASKNAME".out", "w", stdout);
    int testsCount;
    scanf("%d", &testsCount);
    for (int testNumber = 1; testNumber <= testsCount; ++testNumber) {
        printf("Case #%d: ", testNumber);
        int n;
        double v, x;
        scanf("%d%lf%lf", &n, &v, &x);
        vector<double> r(n), c(n);
        for (int i = 0; i < n; i++) {
            scanf("%lf%lf", &r[i], &c[i]);
        }
        if (testNumber == 65) {
            fprintf(stderr, "%.20f %.20f\n", v, x);
        }
        double L = EPS, R = 1e30;
        for (int it = 0; it < 1000; it++) {
            double M = (L + R) / 2;
            int status = check(v, x, r, c, M);
            if (status == 0) {
                L = M;
            } else {
                R = M;
            }
        }
        if (!check(v, x, r, c, R)) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%.20f\n", R);
        }
    }
    return 0;
}