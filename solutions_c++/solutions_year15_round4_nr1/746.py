#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

const int MAXN = 110;

int T;
int n, m;
char a[MAXN][MAXN];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; ++i)
            scanf("%s", a[i]);
        
        bool ok = true;
        int cnt = 0;
        
        for (int i = 0; i < n && ok; ++i) {
            for (int j = 0; j < m && ok; ++j) {
                if (a[i][j] == '.')
                    continue;
                bool up = true;
                for (int k = i - 1; k >= 0 && up; --k)
                    if (a[k][j] != '.')
                        up = false;
                
                bool down = true;
                for (int k = i + 1; k < n && down; ++k)
                    if (a[k][j] != '.')
                        down = false;
                
                bool left = true;
                for (int k = j - 1; k >= 0 && left; --k)
                    if (a[i][k] != '.')
                        left = false;
                
                bool right = true;
                for (int k = j + 1; k < m && right; ++k)
                    if (a[i][k] != '.')
                        right = false;
                
                if ((a[i][j] == '^' && up) || (a[i][j] == 'v' && down) || (a[i][j] == '<' && left) || (a[i][j] == '>' && right)) {
                    ++cnt;
                    if ((int)up + (int)down + (int)left + (int)right == 4)
                        ok = false;
                }
            }
        }
        
        printf("Case #%d: ", t);
        if (ok)
            printf("%d\n", cnt);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
