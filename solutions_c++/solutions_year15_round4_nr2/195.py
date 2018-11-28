#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<bitset>
using namespace std;

const int N = 103;
const double eps = 0.00000000000000001;

int n, p[N];
double f[N], t[N], r, tr;

bool cmp(int a, int b) {
    return t[a] < t[b];
}

double tmin(double timp) {
    int i;

    double vc = 0, tc = 0;

    for(i = 1; i <= n; ++i) {

        double vad = f[p[i]] * timp;

        if(vc + vad >= r) {
            double ned = r - vc;

            double newtc = (vc * tc + ned * t[p[i]]) / (vc + ned);
            tc = newtc;
            vc += ned;
            break;
        }
        else {
            double newtc = (vc * tc + vad * t[p[i]]) / (vc + vad);
            tc = newtc;
            vc += vad;
        }
    }

    return tc;
}

double tmax(double timp) {
    int i;

    double vc = 0, tc = 0, rez = 10000000000.0;

    for(i = n; i; --i) {

        double vad = f[p[i]] * timp;

        if(vc + vad >= r) {
            double ned = r - vc;

            double newtc = (vc * tc + ned * t[p[i]]) / (vc + ned);
            tc = newtc;
            vc += ned;
            break;
        }
        else {
            double newtc = (vc * tc + vad * t[p[i]]) / (vc + vad);
            tc = newtc;
            vc += vad;
        }
    }

    return tc;
}

bool ver(double timp) {

    double v = 0;
    for(int i = 1; i <= n; ++i)
        v += (f[i] * timp);

    return v >= r;
}

void sol() {
    int i, j;

    double cs = 0, cd = 1.0 * (1LL<<50);

    cin >> n >> r >> tr;

    double tmmin = 100000.0, tmmax=  0;

    for(i = 1; i <= n; ++i) {
        cin >> f[i] >> t[i];
        p[i] = i;

        tmmin = min(tmmin, t[i]);
        tmmax = max(tmmax, t[i]);
    }

    if(tmmin > tr || tmmax < tr) {
        cout << "IMPOSSIBLE";
        return;
    }

    sort(p + 1, p + n + 1, cmp);

    for(int w = 1; w <= 2000; ++w) {
        double mid = (cs + cd) / 2;

        if(cd == 4)
            cd = 4;

        if(!ver(mid)) {
            cs = mid;
            continue;
        }

        if(tmin(mid) > tr + eps || tmax(mid) + eps < tr) {
            cs = mid;
        }
        else {
            cd = mid;
        }
    }

    cout << fixed << setprecision(13) << fixed << cs;
}

int main() {
    freopen("ttt", "r", stdin);
    freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        cout << "Case #" << a << ": ";
        sol();
        cout << "\n";
    }

    return 0;
}
