#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
const int maxn = 1000 + 10;

double a[maxn], b[maxn],c[maxn];

int main()
{
    freopen("D.in","r",stdin);
   freopen("out.txt","w",stdout);
    int cas,n;
    scanf("%d",&cas);
    for(int t = 1 ;t <= cas; ++ t)
    {
        scanf("%d",&n);
        for(int i = 1 ;i <= n; ++ i)
            cin>>a[i];
        for(int i = 1 ;i <= n; ++i)
            cin>>b[i];
        int ans1 = 0 ,ans2 = n;
        sort(a+ 1, a + n + 1);
        sort(b + 1,b + n + 1);
        for(int i = 1 ; i<= n; ++ i) c[i] = b[i];
        for(int i = 1 ; i <= n; ++ i)
        {
            for(int j = 1 ;j <= n; ++ j)
            {
                if(c[j] > a[i])
                {
                    c[j] = 0;
                    -- ans2;
                    break;
                }
            }

        }
       int l1 = 1, l2 = 1;
       int r1 = n ,r2 = n;
       int cnt =0 ;
       while(l1 <= n && l2 <= r2 )
       {
           if(a[l1] > b[l2])
           {
               ++ l1;
               ++ l2;
               ++ ans1;
           }
           else
           {
               ++ l1;
               -- r2;
           }
           ++ cnt;

        }

        printf("Case #%d: %d %d\n",t,ans1,ans2);
    }
    return 0;
}
