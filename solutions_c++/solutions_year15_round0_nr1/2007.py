#include <stdio.h>

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("alarge.in","r",stdin);
    freopen("alargeout.txt","w",stdout);
    #endif
    int t;
    scanf ("%d",&t);
    int j;
    for (j=1;j<=t;++j)
    {
        int smax;
        scanf ("%d",&smax);
        int i;
        char S[10000];
        scanf ("%s",S);
        //printf ("%d %s\n",smax,S);
        int ans=0;
        int count=S[0]-'0';
        for (i=1;i<=smax;++i)
        {
            if (count<i)
            {
                ans+=i-count;
                count+=i-count;
            }
            count=count+S[i]-'0';
        }
        printf("Case #%d: %d\n",j,ans);
    }
    return 0;
}
