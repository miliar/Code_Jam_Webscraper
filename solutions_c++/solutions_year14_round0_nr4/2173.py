#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
int cmp(const void *a,const void *b)
{
    if( *(double *)a > *(double *)b)
        return 1;
    else
        return -1;
}
int main()
{
     freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,pos = 0,n,i,j,ans,ANS;
    int AA[1900];
    double A[1900],B[1900];
    scanf("%d",&T);
    while(T --)
    {
        scanf("%d",&n);
        for(i = 1;i <= n;i ++)
            scanf("%lf",&A[i]);
        for(i = 1;i <= n;i ++)
            scanf("%lf",&B[i]);
        qsort(A + 1,n,sizeof(A[0]),cmp);
        qsort(B + 1,n,sizeof(B[0]),cmp);
        for(i = 1;i <= n;i ++)
                AA[i] = 0;
          ans = n;
        for(i = 1;i <= n;i ++)
        {
            for(j = 1;j <= n;j ++)
                {
                    if(!AA[j] && B[j] > A[i])
                    {
                        AA[j] = 1;
                        ans --;
                        break;
                    }
                }
           if(j == n + 1)
              for(int k = 1;k <= n;k ++)
              if(!AA[k])
                AA[k] = 1;
        }
         ANS = n;
        for(i = 1;i <= n;i ++)
            AA[i] = 0;
        int L = 1;
        for(i = 1;i <= n;i ++)
        {
            if(A[i] > B[L])
                L ++;
            else
                ANS --;
        }
        printf("Case #%d: %d %d\n",++pos,ANS,ans);
    }
    return 0;
}
