# include <iostream>
# include <cstdio>
# include <cstring>

using namespace std;

const int MAXN = 120;
char a[MAXN][MAXN];

const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};
const char* val=">v<^";
int n, m;

int find(char c) {
    for(int i = 0; i < 4; ++i) if(val[i] == c) return i;
    return -1;
}

bool out_range(int i,int j) {
    int dir = find(a[i][j]);
    while(true) {
        i += dx[dir];
        j += dy[dir];
        if(i >= n || i < 0 || j >= m || j < 0) return true;
        if(a[i][j] != '.') return false;
    }
    return false;
}

bool changeable(int i,int j) {
    for(int k = 0; k < 4; ++k) {
        a[i][j] = val[k];
        if(!out_range(i, j)) return true;
    }
    return false;
}

int main() {
    int T, cas = 0; scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++cas);
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; ++i) scanf("%s", a[i]);
        int ans = 0;
        bool flag = true;
        for(int i = 0; i < n; ++i) 
            for(int j = 0; j < m; ++j) if(a[i][j] != '.') 
                if(out_range(i, j)) {
                    if(!changeable(i, j)) {flag = false; break;}
                    ans += 1;
                }
        if(flag) printf("%d\n", ans);
        else puts("IMPOSSIBLE");
    }
    return 0;
}

