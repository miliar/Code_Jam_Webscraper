#include <stdio.h>

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("largeb.in","r",stdin);
        freopen("blargeout.txt","w",stdout);
    #endif
    int t;
    scanf ("%d",&t);
    int j;
    for (j=1;j<=t;++j)
    {
        int d;
        scanf ("%d",&d);
        int A[2000];
        int i;
        int max=-1;
        for (i=0;i<d;++i)
        {
            scanf ("%d",&A[i]);
            if (A[i]>max)
                max=A[i];
        }
        int k;
        int ans=10000000;
        for (i=1;i<=max;++i)
        {
            int t=0;
            for (k=0;k<d;++k)
            {
                if (A[k]%i==0)
                    t+=(A[k]/i)-1;
                else
                    t+=(((double)A[k])/i);
            }
            t+=i;
            if (t<ans)
                ans=t;
        }
        printf("Case #%d: %d\n",j,ans);
    }
    return 0;
}
