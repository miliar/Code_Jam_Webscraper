#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>

#define REP(i,n) for (int i=0; i<(n); ++i)
#define TR(i,x) for(typeof(x.begin()) i=x.begin(); i!=x.end(); ++i)
#define ALL(x) x.begin(), x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x, 0, sizeof(x))
#define FIIL(x,c) memset(x, c, sizeof(x))

#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int n, m;
int a[110][110];
vector<PII> v[110];

bool check(PII x) {
    bool ok = true;
    REP(i,m) if (a[x.first][i]>a[x.first][x.second]) {
        ok=false;
        break;
    }
    if (ok) return true;
    REP(i,n) if (a[i][x.second]>a[x.first][x.second]) {
        return false;
    }
    return true;
}

int main() {
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small-attempt2.in", "r", stdin);
    //freopen("B-small-attempt3.in", "r", stdin);
    //freopen("B-small.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cas;
    cin>>cas;
    for (int T=1; T<=cas; ++T) {
        cin>>n>>m;
        REP(i,100) v[i].clear();
        REP(i,n) REP(j,m) {
            scanf("%d", &a[i][j]);
            v[a[i][j]-1].PB(MP(i,j));
        }
        bool ans=true;
        REP(i,100) {
            REP(j,v[i].size()) {
                if (!check(v[i][j])) {
                    ans=false;
                    break;
                }
            }
            if (!ans) break;
        }
        printf("Case #%d: ", T);
        puts(ans?"YES":"NO");
    }
    return 0;
}
