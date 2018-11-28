#include "iostream"
#include "algorithm"
#include "vector"
#include "set"
#include "map"
#include "cstring"
#include "string"
#include "vector"
#include "cassert"
#include "queue"
#include "cstdio"
#include "cstdlib"
#include "ctime"
#include "cmath"
#include "bitset"

using namespace std;

typedef long long ll;
typedef pair < int, int > ii;

const int N = 16;

int n;
char s[N][N];
int id[4];
int a[N], b[N], dp[4][N];

int f(int x, int mask) {
    if(x == n)
        return 0;
    int &r = dp[x][mask];
    if(r != -1) return r;
    r = 0;
    bool flag = 0;
    for(int i = 0; i < n; i++) {
        if(b[id[x] * n + i] and !(mask & (1 << i)))
            flag = 1;
    }
    if(!flag) {
        return r = 1;
    }
    for(int i = 0; i < n; i++) {
        if(b[id[x] * n + i] and !(mask & (1 << i)))
            r |= f(x + 1, mask | (1 << i));
    }
    return r;
}

bool check() {
    for(int i = 0; i < n; i++)
        id[i] = i;
    do{
        memset(dp, -1, sizeof(dp));
        if(f(0, 0))
            return 0;
    }while(next_permutation(id, id + n));
    return 1;
}

void solve() {
    scanf("%d", &n);
    for(int i = 1; i <= n; i++)
        scanf("%s", s[i] + 1);
    for(int i = 0; i < n * n; i++)
        a[i] = s[i / n + 1][i % n + 1] - '0';
    int ans = 30;
    for(int mask = 0; mask < (1 << (n * n)); mask++) {
        int bp = __builtin_popcount(mask);
        if(bp >= ans)
            continue;
        bool flag = 0;
        for(int i = 0; i < n * n; i++) {
            if((mask & (1 << i)) and a[i]) {
                flag = 1;
                break;
            }
            b[i] = a[i] | ((mask >> i) & 1);
        }
        if(flag)
            continue;
        if(check()) {
            ans = min(ans, bp);
        }
    }
    printf("%d\n", ans);
}

/*
 
1 3
000
110
000
 
*/

int main () {
    
    freopen("D-small-attempt0.in.txt", "r", stdin);
    freopen("smallD.txt", "w", stdout);
    
    int tt;
    
    scanf("%d", &tt);
    
    for(int it = 1; it <= tt; it++) {
        printf("Case #%d: ", it);
        solve();
    }
    
    return 0;
    
}