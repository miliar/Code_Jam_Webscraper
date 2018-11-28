// New Ryan
// Create @ 22:10 06-01 2013
// Comment - 

#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <map>
#include <set>

using namespace std;

// Self Template Code BGEIN

#define sz(x) ((int)((x).size()))
#define out(x) printf(#x" %d\n", x)
#define all(x) (x).begin(), (x).end()
#define clz(x) memset (x, 0, sizeof(x))
#define read(x) freopen (x, "r", stdin)
#define wrte(x) freopen (x, "w", stdout)
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define repf(i,a,b) for (int i = (a); i <= (b); ++i)
#define repd(i,a,b) for (int i = (a); i >= (b); --i)
#define repcase int t, Case = 1; for (scanf ("%d", &t); t; --t)
#define repeach(i,x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)

typedef long long int64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef pair<double, double> pdd;

int sgn(double x) { return (x > 1e-8) - (x < -1e-8); }
int count_bit(int x) { return x == 0? 0 : count_bit(x >> 1) + (x & 1); }

template<class T> inline void ckmin(T &a, const T b) { if (b < a) a = b; }
template<class T> inline void ckmax(T &a, const T b) { if (b > a) a = b; }

// Self Template Code END

const int mod = 1000002013;
const int maxm = 1000 + 10;

struct node {
    int o, e, p;
    
    node() {}
    node(int _1, int _2, int _3): o(_1), e(_2), p(_3) {
    }
    
    bool operator<(const node& rhs) const {
        return e == rhs.e? o > rhs.o : e > rhs.e;
    }
};

int n, m, O[maxm], E[maxm], P[maxm];
vector<pair<pii, int> > allp;
pii possible[maxm * 2];

int fix(int x) {
    return (x % mod + mod) % mod;
}

int add(int x, int y) {
    return (x + y) % mod;
}

int mul(int x, int y) {
    return (int64)x * y % mod;
}

int cal(int64 s, int64 t, int num) {
    int64 cnum = t - s;
    int64 res = (n + n - cnum + 1) * cnum / 2;
    return mul(res % mod, num);
}

int main() {
    wrte ("A_1.out");
    
    repcase {
        scanf ("%d%d", &n, &m);
        int ans = 0;
        allp.clear();
        rep (i, m) {
            scanf ("%d%d%d", &O[i], &E[i], &P[i]);
            ans = add(ans, cal(O[i], E[i], P[i]));
            allp.push_back(make_pair(pii(O[i], -1), P[i]));
            allp.push_back(make_pair(pii(E[i], 1), P[i]));
        }
        sort (all(allp));
        int cnt = 0;
        repeach (it, allp) {
            if (it->first.second == -1) {  // in
                possible[cnt++] = pii(it->first.first, it->second);
            } else {  // out
                int left = it->second;
                //out(left);
                for (int j = cnt - 1; j >= 0 && left > 0; --j) {
                    if (possible[j].second < left) {
                        ans = fix(add(ans, -cal(possible[j].first, it->first.first, possible[j].second)));
                        //printf ("go %d %d %d\n", possible[j].first, it->first.first, possible[j].second);
                        left -= possible[j].second;
                    } else {
                        ans = fix(add(ans, -cal(possible[j].first, it->first.first, left)));
                        //printf ("go %d %d %d\n", possible[j].first, it->first.first, possible[j].second);
                        possible[j].second -= left;
                        cnt = (possible[j].second == 0? j : j + 1);
                        
                        break ;
                    }
                }
            }
        }
        printf ("Case #%d: %d\n", Case++, ans);
    }
    return 0;
}

