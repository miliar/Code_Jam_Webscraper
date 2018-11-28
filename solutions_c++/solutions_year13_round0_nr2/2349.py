#include <cstdio>
#include <cstdlib>

#define maxn 105

int a[maxn][maxn];
int total, n, m;

bool check(int x, int y) {
    bool flag = true;
    
    for (int i = 0; i < n; i++)
        if (a[i][y] > a[x][y]) {
            flag = false;
            break;
        }
        
    if (flag)
        return true;
        
    flag = true;
    for (int j = 0; j < m; j++)
        if (a[x][j] > a[x][y]) {
            flag = false;
            break;
        }
        
    return flag;
}

bool judge() {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (!check(i, j))
                return false;
                
    return true;
}

int main() {
    
    FILE *fi = fopen("B-large.in", "r");
    FILE *fo = fopen("output.txt", "w");
    
    fscanf(fi, "%d", &total);
    
    for (int t = 0; t < total; t++) {
        fscanf(fi, "%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                fscanf(fi, "%d", &a[i][j]);
                
        if (judge())
            fprintf(fo, "Case #%d: YES\n", t + 1);
        else
            fprintf(fo, "Case #%d: NO\n", t + 1);
            
    }
    
    fclose(fi);
    fclose(fo);
    
    return 0;
}
