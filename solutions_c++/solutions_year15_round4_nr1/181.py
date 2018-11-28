#include <cstdio>

using namespace std;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char s[100][101];

int main()
{
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int r, c, f = 0, ans = 0, j, k, l;
        
        scanf("%d %d", &r, &c);
        
        for (j = 0; j < r; j++) scanf("%s", s[j]);
        
        for (j = 0; j < r; j++) {
            for (k = 0; k < c; k++) {
                int p = 0, q = 0, x = j, y = k;
                
                if (s[j][k] == '.') continue;
                
                if (s[j][k] == '^') {
                    p = -1;
                } else if (s[j][k] == '>') {
                    q = 1;
                } else if (s[j][k] == 'v') {
                    p = 1;
                } else {
                    q = -1;
                }
                
                while (1) {
                    x += p;
                    y += q;
                    
                    if (x < 0 || x >= r || y < 0 || y >= c || s[x][y] != '.') break;
                }
                
                if (x < 0 || x >= r || y < 0 || y >= c) {
                    for (l = 0; l < 4; l++) {
                        x = j;
                        y = k;
                        
                        while (1) {
                            x += dx[l];
                            y += dy[l];
                            
                            if (x < 0 || x >= r || y < 0 || y >= c || s[x][y] != '.') break;
                        }
                        
                        if (x < 0 || x >= r || y < 0 || y >= c) continue;
                        
                        ans++;
                        break;
                    }
                    
                    if (l == 4) f = 1;
                }
            }
        }
        
        if (f == 0) {
            printf("Case #%d: %d\n", i + 1, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
        }
    }
    
    return 0;
}
