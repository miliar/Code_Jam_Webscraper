#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

struct M {
    int s, t, p;
    void input() {
        if (scanf("%d%d%d", &s, &t, &p) == EOF)
            while (1);
    }
};

bool operator<(const M &m1, const M &m2) {
    return m1.s < m2.s;
}

const long long mod = 1000002013;

int n, m, t;
M p[1024];
long long num[2048];

long long get(long long s, long long t) {
    long long len = t - s;
    return ((long long)n + (n - len + 1)) * len / 2 % mod;
}

void solve() {
    scanf("%d%d", &n, &m);
    long long ori = 0;
    vector<int> vec;
    for (int i = 0; i < m; ++i) {
        p[i].input();
        ori += get(p[i].s, p[i].t) * p[i].p;
        ori %= mod;
        vec.push_back(p[i].s);
        vec.push_back(p[i].t);
    }
    sort(vec.begin(), vec.end());
    vec.resize(unique(vec.begin(), vec.end()) - vec.begin());
    for (int i = 0; i + 1 < vec.size(); ++i) {
        for (int j = 0; j < m; ++j) {
            if (p[j].s <= vec[i] && p[j].t >= vec[i + 1]) {
                num[i] += p[j].p;
            }
        }
    }
    long long ans = 0;
    while (true) {
        long long min_num = -1;
        long long len = 0;
        bool f = true;
        int last = -1;
        for (int i = 0; i < vec.size(); ++i) {
            if (num[i] == 0 || i + 1 == vec.size()) {
                if (len != 0) {
                    ans += get(0, len) * (min_num % mod);
                    ans %= mod;
                    for (int j = last; j < i; ++j)
                        num[j] -= min_num;
                }
                len = 0;
                min_num = -1;
                last = -1;
            } else {
                f = false;
                len += vec[i + 1] - vec[i];
                if (min_num == -1 || num[i] < min_num)
                    min_num = num[i];
                if (last == -1)
                    last = i;
            }
        }
        if (f)
            break;
    }
    printf("Case #%d: %d\n", ++t, (int)((ori - ans + mod) % mod));
}

int main() {
    freopen("A.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
