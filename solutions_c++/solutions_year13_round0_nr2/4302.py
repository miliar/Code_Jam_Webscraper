#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int Map[111][111];
int now[111][111];

void work(int no)
{
     int n,m;
     scanf("%d%d",&n,&m);
     for (int i = 0;i < n;++i)
         for (int j = 0;j < m;++j)
         {
             scanf("%d",&Map[i][j]);
             now[i][j] = 100;
             }
     for (int i = 0;i < n;++i)
     {
         int maxd = 0;
         for (int j = 0;j < m;++j)
             maxd = max(maxd,Map[i][j]);
         for (int j = 0;j < m;++j)
             now[i][j] = min(now[i][j],maxd);
     }
     for (int j = 0;j < m;++j)
     {
         int maxd = 0;
         for (int i = 0;i < n;++i)
             maxd = max(maxd,Map[i][j]);
         for (int i = 0;i < n;++i)
             now[i][j] = min(now[i][j],maxd);
             }
     for (int i = 0;i < n;++i)
         for (int j = 0;j < m;++j)
             if (now[i][j] != Map[i][j])
             {
                printf("Case #%d: NO\n",no);
                return;
                }
     printf("Case #%d: YES\n",no);
}
             

int main()
{
    int times;
    scanf("%d",&times);
    for (int i = 1;i <= times;++i)
        work(i);
    return 0;
}
    
