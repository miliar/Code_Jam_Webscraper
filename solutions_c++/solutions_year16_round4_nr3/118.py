#include <cstdio>
#include <algorithm>

using namespace std;

int a[34];
int b[16][16];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int r, c, j, k, l;
        
        scanf("%d %d", &r, &c);
        
        for (j = 0; j < (r + c) * 2; j++) scanf("%d", &a[j]);
        
        printf("Case #%d:\n", i + 1);
        
        for (j = 0; j < (1 << (r * c)); j++) {
            for (k = 0; k < r + c; k++) {
                int x, y, z;
                
                if (a[k * 2] <= c) {
                    x = 0;
                    y = a[k * 2] - 1;
                    z = 0;
                } else if (a[k * 2] <= r + c) {
                    x = a[k * 2] - c - 1;
                    y = c - 1;
                    z = 1;
                } else if (a[k * 2] <= r + c * 2) {
                    x = r - 1;
                    y = c - (a[k * 2] - r - c);
                    z = 2;
                } else {
                    x = r - (a[k * 2] - r - c * 2);
                    y = 0;
                    z = 3;
                }
                
                while (1) {
                    if (x < 0 || x >= r || y < 0 || y >= c) break;
                    
                    if ((j >> (x * c + y)) & 1) {
                        if (z == 0) {
                            y--;
                            z = 1;
                        } else if (z == 1) {
                            x++;
                            z = 0;
                        } else if (z == 2) {
                            y++;
                            z = 3;
                        } else {
                            x--;
                            z = 2;
                        }
                    } else {
                        if (z == 0) {
                            y++;
                            z = 3;
                        } else if (z == 1) {
                            x--;
                            z = 2;
                        } else if (z == 2) {
                            y--;
                            z = 1;
                        } else {
                            x++;
                            z = 0;
                        }
                    }
                }
                
                if (x < 0) {
                    if (a[k * 2 + 1] != y + 1) break;
                } else if (x >= r) {
                    if (a[k * 2 + 1] != r + c + c - y) break;
                } else if (y < 0) {
                    if (a[k * 2 + 1] != r + c * 2 + r - x) break;
                } else {
                    if (a[k * 2 + 1] != c + x + 1) break;
                }
            }
            
            if (k == r + c) {
                int x = 0;
                
                for (k = 0; k < r; k++) {
                    for (l = 0; l < c; l++) {
                        if ((j >> x) & 1) {
                            putchar('/');
                        } else {
                            putchar('\\');
                        }
                        x++;
                    }
                    puts("");
                }
                
                break;
            }
        }
        
        if (j == (1 << (r * c))) puts("IMPOSSIBLE");
    }
    
    return 0;
}
