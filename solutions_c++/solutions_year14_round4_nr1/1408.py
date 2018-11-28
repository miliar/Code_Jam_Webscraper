#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cassert>
#include <ctime>
#include <queue>
#include <map>
#include <set>
#include <climits>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef pair<int, int> PII;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define FILLCHAR(a, x) memset(a, x, sizeof(a))
#define SZ(x) ((int) (x).size())
#define ALL(x) (x).begin(), (x).end()

int T;
int X;
int N;
const int MAXN = 1e4 + 10;
int S[MAXN];
int taken[MAXN];

int run() {
    scanf("%d%d", &N, &X);
    REP(i,N) scanf("%d", &S[i]);
    memset(taken, 0, sizeof(taken));
    map<int,int> bags;
    int ret = 0;
    sort(S, S + N);
    reverse(S, S + N);
    REP(i,N) {
        if (i <= (N - 1) / 2) {
            bags[X - S[i]]++;
        } else {
            auto pos = bags.lower_bound(S[i]);
            if (pos == bags.end()) {
                bags[X - S[i]]++;
            } else {
                ret++;
                pos->second--;
                if (pos->second == 0) bags.erase(pos);
            }
        }
    }

    FOREACH(it,bags) {
        ret += it->second;
    }

    return ret;
}
int main() {
    int T;
    scanf("%d", &T);

    REP(t,T) {
        printf("Case #%d: %d\n", t + 1, run());
    }
}

