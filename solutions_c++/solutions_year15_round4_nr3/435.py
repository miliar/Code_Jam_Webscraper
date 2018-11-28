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
#include <cassert>
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

int N;

char buf[333][111111];
vector<int> words[333];
map<string, int> s2i;
int mask[1000000];

void solve() {
    scanf("%d\n", &N);
    s2i.clear();
    db(N);
    rep (i, N) words[i].clear();
    int xx = 0;
    rep (i, N) {
        for (int zn = 0; ; zn++) {
            scanf("%c", &buf[i][zn]);
            if (buf[i][zn] == '\n') {
                buf[i][zn] = 0;
                break;
            }
        }
        stringstream is(buf[i]);
        string x;
        while (is>>x) {
            if (!s2i.count(x)) {
                s2i[x] = s2i.size() - 1;
                xx++;
            }
            words[i].push_back(s2i[x]);
        }
    }
    int w = s2i.size();
    assert(xx == w);
    db("");
    int res = 100000;
    rep (x, 1<<N) {
        if (x & 1) continue;
        if (!(x & 2)) continue;
        rep (i, w)
            mask[i] = 0;
        rep (i, N) {
            fore (it, words[i]) if (x & (1<<i))
                mask[*it] |= 1;
            else
                mask[*it] |= 2;
        }
        int sum = 0;
        rep (i, w)
            if (mask[i] == 3)
                sum += 1;
        if (sum == 3)  {
            db(x<<" "<<sum);
            rep (i, w) db(mask[i]);
        }

        res = min(res, (int)sum);
    }
    printf("%d\n", res);
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
    scanf("%d\n", &t);
    fo (i, 1, t) {
        printf("Case #%d: ", i);
        solve();
        fflush(stdout);
        cerr.flush();
    }
	return 0;
}
