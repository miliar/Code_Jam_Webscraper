#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
#define x first
#define y second

const int N = 5;

int n;
bool know[N][N];
bool worker[N];
bool repaired[N];

bool verify(int level) {
    bool ret = true;
    if (level == n) return ret;

    FOR(w, 0, n) if (!worker[w]) {
        if (!ret) break;

        worker[w] = true;
        bool any = false;
        FOR(i, 0, n) {
            if (!repaired[i] && know[w][i]) {
                any = true;
                repaired[i] = true;
                ret &= verify(level + 1);
                repaired[i] = false;
            }
        }
        if (!any) ret = false;

        worker[w] = false;
    }
    return ret;
}

int main() {
    char s[N][N];
    int T; scanf("%d", &T); FOE(ca, 1, T) {
        scanf("%d", &n); FOR(i, 0, n) scanf("%s", s[i]);

        int ans = n * n;

        FOR(b, 0, 1<<(n*n)) {
            bool skip = false;
            int cost = 0;
            CLR(know);
            FOR(i, 0, n) FOR(j, 0, n) {
                bool buy = b & (1<<(i * n + j));
                if (buy && s[i][j] == '1') {
                    skip = true;
                }
                cost += int(buy);

                know[i][j] = buy || s[i][j] == '1';
            }
            if (skip) continue;

            CLR(worker);
            CLR(repaired);
            bool ok = verify(0);
            if (ok) {
                //printf("Cost: %d\n", cost);
                //FOR(i,0,n) { FOR(j,0,n) printf("%d",int(know[i][j])); puts(""); }
                ans = min(ans, cost);
            }
        }

        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
