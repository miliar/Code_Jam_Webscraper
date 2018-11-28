#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define re(i,j,n) for(int i=j;i<n;i++)
#define down(i,n) for(int i=n;i>=0;i--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define pb push_back

#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
#define LL long long
#define INF (0x3f3f3f3f)
const int N = 10000000;
int T, cas = 0;
LL A,B;
int a[N + 5];
char aa[20], p;
inline bool ck(LL k) {
    p = 0;
    for(; k ; p++) {
        LL t = k / 10;
        aa[p] = k - (t << 3) - (t << 1) + '0';
        k = t;
    }
    rep(i, p) {
        if (aa[i] != aa[p - 1 - i]) return false;
    }
    return true;
}

void gao(int n) {
    memset(a, 0, sizeof  a);
    a[0] = 0;
    a[1] = 1;
    re(i,2,n) {
        if (ck(i) && ck(i*(LL)i)) {
            a[i]++;
        }
    }
    re(i, 1, N + 1) a[i] += a[i - 1];
}
int main() {
    cin >> T;
    gao(N + 1);
    while (T--) {
        cin >> A >> B;
        A = (LL)sqrt(A - 1), B = (LL)sqrt(B);
        int ans = a[B] - a[A];
        cas++;
        printf("Case #%d: %d\n", cas, ans);
    }
	return 0;
}



