#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 105;
const int INF = 1 << 29;
const long long MOD = 55566677ll;
const int dx[] = {-1, 0, 0, 1, 1, 1, -1, -1};
const int dy[] = {0, -1, 1, 0, 1, -1, -1, 1};

int n, m;
int h[MAXN][MAXN];
int a[MAXN][MAXN];

void prep(){
}

void init(){
    if (scanf("%d%d", &n, &m) == EOF) exit(0);
    for (int i = 0;i < n;i++){
        for (int j = 0;j < m;j++){
            scanf("%d", &h[i][j]);
            a[i][j] = h[i][j];
        }
    }
}

int mx[MAXN];
bool gao(){
    for (int i = 0;i < n;i++){
        mx[i] = 0;
        for (int j = 0;j < m;j++){
            mx[i] = max(mx[i], a[i][j]);
        }
        for (int j = 0;j < m;j++){
            a[i][j] = mx[i];
        }
    }
//    for (int i = 0;i < n;i++){
//        for (int j = 0;j < m;j++){
//            printf("%d ", a[i][j]);
//        }
//        printf("\n");
//    }
    for (int j = 0;j < m;j++){
        bool f = true;
        for (int i = 0;i < n;i++){
            if (a[i][j] != h[i][j]){
                f = false;
                break;
            }
        }
        if (f) continue;
        int mn = 101;
        for (int i = 0;i < n;i++){
            mn = min(mn, h[i][j]);
        }
        f = true;
//        printf("mn = %d\n", mn);
        for (int i = 0;i < n;i++){
            if (h[i][j] > mn){
//                printf("%d %d %d\n", i, j, h[i][j]);
                f = false;
                break;
            }
        }
        if (f) continue;
        return false;
    }
    return true;
}

void work(){
    bool ans = gao();
    printf("%s\n", ans ? "YES" : "NO");
}

int main(){
#ifdef LATTE
//    freopen("b.in", "r", stdin);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
#endif
    int T, t = 0;
    prep();
    scanf("%d", &T);
    while (T--){
        init();
        printf("Case #%d: ", ++t);
        work();
    }
    return 0;
}
