#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <queue>
using namespace std;

int a[2010], b[2010];
int f[2010][2010];
int in[2010];
int ans[2010];

int main() {
    freopen("/Users/L/Downloads/C-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/L/Downloads/ans.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int kase = 1; kase <= T; kase++) {
        int n;
        scanf("%d", &n);
        
        for (int i = 0; i < n; i++) scanf("%d", &a[i]);
        for (int i = 0; i < n; i++) scanf("%d", &b[i]);
        memset(f, 0, sizeof(f));
        memset(in, 0, sizeof(in));
        
        for (int i = 0; i < n; i++) {
            int flag = 1;
            for (int j = i-1; j >= 0; j--)
                if (a[j] >= a[i]) f[i][j] = 1;
                else if (a[j]+1 == a[i] && flag) {
                    f[j][i] = 1;
                    flag = 0;
                }
        }
        for (int i = n-1; i >= 0; i--) {
            int flag = 1;
            for (int j = i+1; j < n; j++)
                if (b[i] <= b[j]) f[i][j] = 1;
                else if (b[i] == b[j]+1 && flag) {
                    f[j][i] = 1;
                    flag = 0;
                }
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (f[i][j]) in[j]++;
        
        printf("Case #%d:", kase);
        for (int k = 0; k < n; k++) {
            int now;
            for (int i = n-1; i >= 0; i--)
                if (in[i] == 0) now = i;
            
            in[now] = -1;
            ans[now] = k+1;
            
            for (int i = 0; i < n; i++)
                if (f[now][i]) in[i]--;
        }
        for (int i = 0; i < n; i++) printf(" %d", ans[i]);
        printf("\n");
        
    }
    return 0;
}