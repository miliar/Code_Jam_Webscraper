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

using namespace std;

int n, m;
int g[4][4], h[4][4];

int main() {
    freopen("inA.txt", "r", stdin);
    freopen("outA.txt", "w", stdout);
    int T , cas = 1;
    cin >> T;
    while (T--){
        cin >> n;
        n--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j ++)
              cin >> g[i][j];
        cin >> m;
        m--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j ++)
                cin >> h[i][j];
        int ans = -1, cnt = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j ++) {
                if (g[n][i] == h[m][j]) {
                    cnt ++;
                    ans = g[n][i];
                }
            }
        }
        printf("Case #%d: ",cas++);
        if (cnt == 1) printf("%d\n",ans);
        else {if (cnt == 0) printf("Volunteer cheated!\n"); 
            else if (cnt > 1) printf("Bad magician!\n");
        }
    }
    return 0;
}

