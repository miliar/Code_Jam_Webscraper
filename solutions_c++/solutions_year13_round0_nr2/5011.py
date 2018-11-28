#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
#include <set>
#include <vector>
#include <string>
#include <queue>
#define INF 2100000000
#define eps 1e-8
#define lld long long

using namespace std;
int n, i, m, j, k;
int a[200][200];
int main()
{
    int T,tot=0;
//            freopen("B.in","r",stdin);
//    freopen("a.out","w",stdout);
   cin>>T;
   while(T--)
   {
       scanf("%d%d", &n, &m);
       for(i = 1; i <= n; i++)
       for(j = 1; j <= m; j++)
       scanf("%d", &a[i][j]);
       int flag = 1;
       for(i = 1; i <= n; i++)
       {
           int p = INF,pj;
           int tt=1;
           for(j = 1; j <= m; j++)
               p = min(p, a[i][j]);
            for(j = 1; j <= m; j++)
            if (a[i][j] != p) tt=0;
            if (tt) continue;
             for(j = 1; j <= m; j++)
             if (a[i][j] == p)
             {
                 for(k = 1; k <= n; k++)
                 if (a[k][j] > p) flag = 0;
             }
       }
       printf("Case #%d: ", ++tot);
       if (flag) puts("YES"); else puts("NO");
   }
}
