#include <cstdio>
#include <algorithm>

using namespace std;

int a[4][4];
int b[4][4];
int f[4];
int par[4];

void init(int n) {
    int i;
    
    for (i = 0; i < n; i++) f[i] = 0;
    for (i = 0; i < n; i++) par[i] = i;
}

int find(int x) {
    if (par[x] == x) return x;
    return par[x] = find(par[x]);
}

void unite(int x, int y) {
    x = find(x);
    y = find(y);
    
    if (x == y) return;
    
    par[x] = y;
}

int check(int n) {
    int i, j, k;
    
    init(n);
    
    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            for (k = 0; k < n; k++) {
                if (b[i][k] == 1 && b[j][k] == 1) unite(i, j);
            }
        }
    }
    
    for (i = 0; i < n; i++) {
        int c1 = 0, c2 = 0;
        
        if (f[i] == 1) continue;
        
        for (j = 0; j < n; j++) {
            if (find(i) == find(j)) {
                for (k = 0; k < n; k++) {
                    if (b[i][k] + b[j][k] == 1) return 0;
                }
                
                f[j] = 1;
                c1++;
            }
        }
        
        for (j = 0; j < n; j++) {
            if (b[i][j] == 1) c2++;
        }
        
        if (c1 != c2) return 0;
    }
    
    return 1;
}

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, ans = 1e9, j, k, l;
        
        scanf("%d", &n);
        
        for (j = 0; j < n; j++) {
            for (k = 0; k < n; k++) {
                scanf("%1d", &a[j][k]);
            }
        }
        
        for (j = 0; j < (1 << (n * n)); j++) {
            int f = 0, sum = 0;
            
            for (k = 0; k < n; k++) {
                for (l = 0; l < n; l++) {
                    if ((j >> (k * n + l)) & 1) {
                        if (a[k][l] == 0) sum++;
                        
                        b[k][l] = 1;
                    } else {
                        if (a[k][l] == 1) f = 1;
                        
                        b[k][l] = 0;
                    }
                }
            }
            
            if (f == 1) continue;
            
            if (check(n) == 1) ans = min(ans, sum);
        }
        
        printf("Case #%d: %d\n", i + 1, ans);
    }
    
    return 0;
}
