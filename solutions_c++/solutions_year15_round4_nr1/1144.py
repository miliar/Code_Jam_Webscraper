#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;

const int N = 100+5;
int dir[4][2] = {1,0,-1,0,0,1,0,-1};
char s[N][N];
int n, m;

int get(char ch) {
    if(ch == 'v') return 0;
    if(ch == '^') return 1;
    if(ch == '>') return 2;
    return 3;
}

bool check(int x, int y) {
    if(x<0 || y<0 || x>=n || y>=m) return false;
    return true;
}

int solve() {
    int ret = 0;
    for(int i = 0;i < n; i++) {
        for(int j = 0;j < m; j++) if(s[i][j] != '.'){
            bool flag = false;
            for(int k = 0;k < n; k++) if(k != i && s[k][j] != '.') {
                flag = true;
            }
            for(int k = 0;k < m; k++) if(k != j && s[i][k] != '.') {
                flag = true;
            }
            if(!flag) return -1;
            int d = get(s[i][j]);
            int x = i, y = j;
            flag = false;
            x += dir[d][0]; y += dir[d][1];
            while(check(x, y)) {
                if(s[x][y] != '.') flag = true;
                x += dir[d][0]; y += dir[d][1];
            }
            if(!flag)   ret++;
        }
    }
    return ret;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 1;
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d", &n, &m);
        for(int i = 0;i < n; i++) scanf("%s", s[i]);
        int ans = solve();
        printf("Case #%d: ", cas++);
        if(ans == -1) puts("IMPOSSIBLE");
        else    printf("%d\n", ans);
    }
    return 0;
}
