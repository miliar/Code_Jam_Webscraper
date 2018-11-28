#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int n;
double dp[1 << 20];

double dfs(int x)
{
    int i, j;
    double sum = 0;
    
    if (dp[x] != -1) return dp[x];
    
    if (x == (1 << n) - 1) return dp[x] = 0;
    
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if ((x >> ((i + j) % n)) & 1) continue;
            
            sum += dfs(x | (1 << (i + j) % n)) + n - j;
            
            break;
        }
    }
    
    return dp[x] = sum / n;
}

int main()
{
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int x = 0, j;
        char s[21];
        
        scanf("%s", s);
        
        n = strlen(s);
        
        for (j = 0; j < (1 << n); j++) dp[j] = -1;
        
        for (j = 0; j < n; j++) {
            if (s[j] == 'X') x |= (1 << j);
        }
        
        printf("Case #%d: %.12lf\n", i + 1, dfs(x));
    }
    
    return 0;
}
