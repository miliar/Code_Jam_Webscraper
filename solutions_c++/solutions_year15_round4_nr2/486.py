#include <algorithm>
#include <array>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define rep(i,b) for(auto i=(0);i<(b);++i)
#define fo(i,a,b) for(auto i=(a);i<=(b);++i)
#define ford(i,a,b) for(auto i=(a);i>=(b);--i)
#define fore(a,b) for(auto a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

vector<pair<ld, ld> > data;

int N;
ld V, X;

bool can(ld t) {
    ld sum = 0;
    ld temp = 0;
    rep (i, N) sum += t * data[i].second;
    rep (i, N) temp += t * data[i].second * data[i].first;
    if (sum < V) return false;
    if (temp / sum < X) {

    }
    else {
        reverse(all(data));
    }
    db(temp<<" "<<sum<<" "<<temp/sum);
    rep (i, N) {
        db(data[i].first<<" "<<data[i].second);
        ld mian = - data[i].first * data[i].second + data[i].second * X;
        ld licz = X * sum - temp;
        if (abs(mian) < 1e-18) continue;
        ld tim = licz / mian;
        tim = max(tim, (ld)0);
        tim = min(tim, t);
        db(t<<" "<<tim);
        sum -= tim * data[i].second;
        temp -= tim * data[i].second * data[i].first;

        db(temp<<" "<<sum<<" "<<temp/sum<<" "<<V<<" "<<X);
    }
    if (sum < V) return false;
    return abs(temp / sum - X) < (ld)1e-9;
}

void solve() {
    scanf("%d", &N);
    scanf("%Lf%Lf", &V, &X);
    data.clear();

    rep (i, N) {
        ld r, c;
        scanf("%Lf%Lf", &r, &c);
        db(r<<" "<<c);
        data.push_back(make_pair(c, r));
    }
    sort(all(data));

    ld a = 0;
    ld b = 1000 + V / 0.0001;
    ld mid;
    ld good = -1;
    rep (i, 100) {
        mid = (a + b) / 2;
        bool c = can(mid);
        db(c<<" "<<mid);
        if (c) {
            good = mid;
            b = mid;
        }
        else
            a = mid;
    }
    if (good >= 0 or can(good + 1e-9))
        printf("%.9Lf\n", good);
    else
        printf("IMPOSSIBLE\n");
}

int main(int argc, char ** argv) {
    ios::sync_with_stdio(false);

    //  freopen("../1.in","r",stdin);
    //  freopen("../2.in","r",stdin);
    //  freopen("../3.in","r",stdin);
    //  freopen("../A-small.in","r",stdin); freopen("../A-small.out","w",stdout);
    //  freopen("../A-small-attempt0.in","r",stdin);freopen("../A-small-attempt0.out","w",stdout);
    //  freopen("../A-small-attempt1.in","r",stdin);freopen("../A-small-attempt1.out","w",stdout);
    //  freopen("../A-small-attempt2.in","r",stdin);freopen("../A-small-attempt2.out","w",stdout);
    //  freopen("../A-large.in","r",stdin); freopen("../A-large.out","w",stdout);

    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
        printf("Case #%d: ", i);
        solve();
        fflush(stdout);
        cerr.flush();
    }
	return 0;
}
