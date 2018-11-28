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

const int MOD = 1e9 + 7;

int m, n;
char s[20][20];
int nxt[2000][26];
int cost[2000];
int f[20][2000], ways[20][2000];

int Calc(int st) {
    int tot = 1;
    CLEAR(nxt);
    for (; st; st -= st & -st) {
        int cur = 0, i = __builtin_ctz(st & -st);
        for (int j = 0; s[i][j]; ++j) {
            int ch = s[i][j] - 'A';
            if (nxt[cur][ch] == 0) nxt[cur][ch] = tot++;
            cur = nxt[cur][ch];
        }
    }
    return tot;
}

void Update(int& best, int cur, int& tot, int count) {
    if (best < cur) {
        best = cur;
        tot = count;
    } else if (best == cur) {
        tot += count;
        if (tot >= MOD) tot -= MOD;
    }
}
void Solve() {
    cin >> m >> n;
    REP(i, m) {
        scanf("%s", s[i]);
    }
    REP(i, 1 << m) {
        cost[i] = Calc(i);
    }
    FILL(f, 0xff);
    CLEAR(ways);
    f[0][0] = 0;
    ways[0][0] = 1;
    int all = (1 << m) - 1;
    REP(i, n) REP(j, 1 << m) {
        if (f[i][j] >= 0) {
            for (int st = all ^ j, t = st; t; t = (t - 1) & st) {
                Update(f[i + 1][j | t], f[i][j] + cost[t], ways[i + 1][j | t], ways[i][j]);
            }
        }
    }
    cout << f[n][all] << " " << ways[n][all] << endl;
}

int main() {
	freopen("D-small-attempt0.in","r",stdin);freopen("D-small-attempt0.out","w",stdout);
//	freopen("D-small-attempt1.in","r",stdin);freopen("D-small-attempt1.out","w",stdout);
//	freopen("D-small-attempt2.in","r",stdin);freopen("D-small-attempt2.out","w",stdout);
//	freopen("D-large.in","r",stdin);freopen("D-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
    }
    return 0;
}

