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

const int MOD = 1e9+7;

int n;
PII s[1010];
int a[1010];
int f[1010][1010], L[1010];

void Solve() {
     cin >> n;
     REP(i, n) {
         cin >> s[i].first;
         s[i].second = i + 1;
     }
     sort(s, s + n);
     REP(i, n) a[s[i].second] = i + 1;
     for (int i = 1; i <= n; ++i) {
         L[i] = 0;
         for (int j = 1; j < i; ++j) {
             if (a[j] > a[i]) ++L[i];
         }
     }
     FILL(f, 0x3f3f);
     f[0][0] = 0;
     REP(i, n) {
         REP(j, n + 1) {
             if (f[i][j] == 0x3f3f3f3f) continue;
             f[i + 1][j + 1] = min(f[i + 1][j + 1], f[i][j] + L[s[i].second]);
             f[i + 1][j] = min(f[i + 1][j], f[i][j] + n - i - L[s[i].second] - 1);
         }
     }
     int ans = 0x3f3f3f3f;
     REP(i, n + 1) {
         ans = min(ans, f[n][i]);
     }
     cout << ans << endl;
}

int main() {
    //	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
    //	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
    //	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
    	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
    }
    return 0;
}


