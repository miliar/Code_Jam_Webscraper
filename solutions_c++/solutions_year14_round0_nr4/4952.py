#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <cctype>
#include <map>
#include <iomanip>
                   
using namespace std;
                   
#define eps 1e-8
#define pi acos(-1.0)
#define inf 1<<30
#define linf 1LL<<60
#define pb push_back
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define fi first
#define se second

double a[1111], b[1111];
int vis[1111];
int n;

int main() {
    freopen("inD.txt","r",stdin);
    freopen("outD.txt","w",stdout);
    int T , cas = 1;
    cin >> T;
    while (T--) {
        cin >> n;
        for (int i = 0 ; i < n; i++) cin >> a[i];
        for (int i = 0 ; i < n; i++) cin >> b[i];
        sort(a , a + n);
        sort(b , b + n);
        int ans1 = 0, ans2 = 0;
        //
        int idx = n - 1 , le = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (a[idx] > b[i]) ans2++ , idx--;
            else le++;
            if (le > idx) break;
        }

        //not
        memset(vis , 0, sizeof(vis));
        for (int i = 0; i <= n - 1; i++) {
            idx = -1;
            for (int j = 0; j <= n - 1; j++) {
                if (!vis[j]) {
                    if (b[j] > a[i]) {
                        idx = j;
                        break;
                    }
                }
            }
            if (idx == -1) ans1++;
            vis[idx] = 1;
        }
        
        printf("Case #%d: %d %d\n", cas++ , ans2 , ans1);
    }
    return 0;
}
