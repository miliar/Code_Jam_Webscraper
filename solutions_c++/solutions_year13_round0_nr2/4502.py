#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;

#define maxn 107

int a[maxn][maxn];
int n, m;

bool check()
{
    int i, j, k;
    bool ok1, ok2;
    
    for (i = 0; i < n; ++i)
        for (j = 0; j < m; ++j) {
            ok1 = true; ok2 = true;
            
            for (k = i-1; k >= 0; --k)
                if (a[k][j] > a[i][j]) {
                    ok1 = false;
                    break;
                }
            for (k = i+1; k < n; ++k)
                if (a[k][j] > a[i][j]) {
                    ok1 = false;
                    break;
                }
                
            for (k = j-1; k >= 0; --k)
                if (a[i][k] > a[i][j]) {
                    ok2 = false;
                    break;
                }
            for (k = j+1; k < m; ++k)
                if (a[i][k] > a[i][j]) {
                    ok2 = false;
                    break;
                }
            
            if ((!ok1) && (!ok2)) return false;
        }
    return true;
}
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    
    int k, cases, i, j;
    
    scanf("%d",&cases);
    for (k = 1; k <= cases; ++k) {
        printf("Case #%d: ",k);
        scanf("%d%d",&n,&m);
        for (i = 0; i < n; ++i)
            for (j = 0; j < m; ++j)
                scanf("%d",&a[i][j]);
        if (check()) printf("YES\n");
        else printf("NO\n");
    }
    
    return 0;
}
