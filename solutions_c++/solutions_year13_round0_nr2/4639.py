#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>

using namespace std;
typedef long long LL;

int n,m;
int a[105][105];
int maxr[105],maxc[105];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("lww2_out.txt","w",stdout);
    int T,ta=1;
    scanf("%d",&T);
    while(T--)
    {
        int i,j;
        scanf("%d%d",&n,&m);
        for(i=0; i<n; i++)
            for(j=0; j<m; j++)
               scanf("%d",&a[i][j]);
        //========================================
        for(i=0; i<n; i++)
        {
            maxr[i] = a[i][0];
            for(j=0; j<m; j++)
                maxr[i] = max(maxr[i],a[i][j]);
        }
        for(i=0; i<m; i++)
        {
            maxc[i] = a[0][i];
            for(j=0; j<n; j++)
                maxc[i] = max(maxc[i],a[j][i]);
        }
        //========================================
        for(i=0; i<n; i++)
        {
            for(j=0; j<m; j++)
               if(a[i][j]<maxr[i] && a[i][j]<maxc[j])
               {
                    break;
               }
            if(j < m) break;
        }

        printf("Case #%d: ",ta++);
        if(i >= n) puts("YES");
        else puts("NO");
    }
    return 0;
}
