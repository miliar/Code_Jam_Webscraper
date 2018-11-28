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
const int N = 105;
int T, cas = 0;
int n, m, a[N][N];
vector<int> R[N],C[N];
int main() {
    cin >> T;
    while (T--) {
        scanf("%d %d", &n, &m);
        rep(i, n) R[i].clear();
        rep(i, m) C[i].clear();
        rep(i, n) rep(j, m) {
            scanf("%d", &a[i][j]);
            R[i].pb(a[i][j]);
            C[j].pb(a[i][j]);
        }
        rep(i, n) sort(R[i].begin(), R[i].end(), greater<int>());
        rep(i, m) sort(C[i].begin(), C[i].end(), greater<int>());
        int ans = 1;
        rep(i, n) rep(j, m) {
            if (a[i][j] != R[i][0] && a[i][j] != C[j][0]) {
                ans = 0;
            }
        }
        cas++;
        printf("Case #%d: ", cas);
        if (ans) puts("YES"); else puts("NO");
    }
	return 0;
}



