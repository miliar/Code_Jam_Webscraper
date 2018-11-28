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

int DW(int n, double a[], double b[]) {
    int pa = 0, pb = 0;
    while (pa < n) {
        if (a[pa] > b[pb]) {
            pa++;
            pb++;
        } else {
            pb++;
            n--;
        }
    }
    return pa;
}

int W(int n, double a[], double b[]) {
    int pa = n - 1, pb = n - 1;
    while (pb >= 0) {
        if (a[pa] < b[pb]) {
            pa--;
        }
        pb--;
    }
    return pa + 1;
}

void Solve() {
    int n;
    double a[1010], b[1010];
    cin >> n;
    REP(i, n) cin >> a[i];
    REP(i, n) cin >> b[i];
    sort(a, a + n, greater<double>());
    sort(b, b + n, greater<double>());
    printf("%d %d\n", DW(n, a, b), W(n, a, b));
}

int main() {
//	freopen("D-small-attempt0.in","r",stdin);freopen("D-small-attempt0.out","w",stdout);
//	freopen("D-small-attempt1.in","r",stdin);freopen("D-small-attempt1.out","w",stdout);
//	freopen("D-small-attempt2.in","r",stdin);freopen("D-small-attempt2.out","w",stdout);
	freopen("D-large.in","r",stdin);freopen("D-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
    }
    return 0;
}

