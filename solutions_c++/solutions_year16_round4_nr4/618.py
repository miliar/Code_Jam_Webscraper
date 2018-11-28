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

#define REP(i,n) for(int i=0;i<(n);i++)
#define TR(i,x) for(__typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))
#define SIZE(x) (int)(x).size()

#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int N;

bool Go(int dep, int a[], int g, int done) {
    if (dep == N) {
        return true;
    }
    int u = a[dep];
    vector<int> can;
    REP(i, N) {
        if (g >> (u * N + i) & 1) {
            if (!(done >> i & 1)) {
                can.PB(i);
            }
        }
    }
    if (SIZE(can) == 0) {
        return false;
    } else if (SIZE(can) == 1) {
        return Go(dep + 1, a, g, done | 1 << can[0]);
    } else {
        TR(it, can) {
            if (!Go(dep + 1, a, g, done | 1 << *it)) {
                return false;
            }
        }
        return true;
    }
}

bool Check(int g) {
    int a[4];
    REP(i, N) a[i] = i;
    do {
        if (!Go(0, a, g, 0)) {
            return false;
        }
    } while (next_permutation(a, a + N));
    return true;
}

bool out;

void Solve() {
    cin >> N;
    if (out)
        cerr << N << endl;
    int all = (1 << (N * N)) - 1, had = 0;
    REP(i, N) {
        char s[10];
        scanf("%s", s);
        if (out)
            cerr << s << endl;
        REP(j, N) {
            if (s[j] == '1') {
                had |= 1 << (i * N + j);
            }
        }
    }
    all ^= had;
    int ans = __builtin_popcount(all);
    if (all) {
        if (Check(had)) {
            ans = 0;
        } else {
            for (int i = (all - 1) & all; i; i = (i - 1) & all) {
                if (Check(i | had)) {
                    if (out) {
                        cerr << __builtin_popcount(i) << endl;
                    }
                    ans = min(ans, __builtin_popcount(i));
                }
            }
        }
    }
    cout << ans << endl;
}

int main() {
    //	freopen("D.in","r",stdin);
    //  freopen("D-small-attempt0.in","r",stdin);freopen("D-small-attempt0.out","w",stdout);
     	freopen("D-small-attempt1.in","r",stdin);freopen("D-small-attempt1.out","w",stdout);
    // 	freopen("D-small-attempt2.in","r",stdin);freopen("D-small-attempt2.out","w",stdout);
    //	freopen("D-large.in","r",stdin);freopen("D-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
        cerr << "Case #" << T << ": done!" << endl;
    }
    return 0;
}


