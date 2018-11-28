# include <iostream>
# include <cstdio>
# include <cstring>

#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;

int val[4][4] = {
    {0x00, 0x01, 0x02, 0x03},
    {0x01, 0x10, 0x03, 0x12},
    {0x02, 0x13, 0x10, 0x01},
    {0x03, 0x02, 0x11, 0x10}
};

int inv[8], c[8][8];

void pre() {
    rep(i, 4) rep(j, 4) {
        c[i][j] = val[i][j];
        c[i|4][j] = (val[i][j] ^ 16);
        c[i][j|4] = (val[i][j] ^ 16);
        c[i|4][j|4] = val[i][j];
    }
    rep(i, 8) rep(j, 8) 
        if(c[i][j] & 0x10) 
            c[i][j] = (c[i][j] ^ 0x10)|4;
    rep(i, 8) rep(j, 8) 
        if(c[i][j] == 1) inv[i] = j;
}

char s[10020];
int a[10020];
int n, m;

int get_val() {
    int t = 0, s = 0;
    for(int i = 0; i < n; ++i) 
        t = c[t][a[i]];
    for(int i = 0; i < m; ++i)
        s = c[s][t];
    return s;
}

bool solve() {
    int t = 0;
    int first_i = -1, last_k = -1;
    int cnt = 0;
    rep(i, m) {
        rep(j, n) {
            t = c[t][a[j]];
            cnt += 1;
            if(t == 1 && first_i == -1) {
                first_i = cnt;
            }
            if(t == 3) {
                last_k = cnt;
            }
        }
    }
    if(first_i == -1 || last_k == -1) 
        return false;
    return (first_i < last_k);
}

int main() {
    pre();
    int T; scanf("%d", &T);
    int cas = 0;
    while(T--) {
        printf("Case #%d: ", ++cas);
        scanf("%d%d", &n, &m);
        scanf("%s", s);
        if(m >= 20) {
            m = m % 20 + 20;
        }
        for(int i = 0; i < n; ++i)
            switch(s[i]) {
                case '1': a[i] = 0; break;
                case 'i': a[i] = 1; break;
                case 'j': a[i] = 2; break;
                case 'k': a[i] = 3; break;
            }
        if(get_val() == 0x04 && solve()) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
}

