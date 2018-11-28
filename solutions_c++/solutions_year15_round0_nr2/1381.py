#include<stdio.h>


int max(int a , int b)
{
    return (a>b)?a:b;
}
int min(int a,int b)
{
    return (a<b)?a:b;
}




int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        int n;
        int p[1005];
        scanf("%d",&n);
        int maxP= -1;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&p[i]);
            maxP = max(maxP,p[i]);
        }


        int ans = 999999999;
        for(int h=1;h<=maxP;h++)
        {
            int tm=0;
            for(int i=0;i<n;i++)
            {
                tm+=(p[i]+h-1)/h-1;
            }
            ans = min(ans,tm+h);
        }

        printf("Case #%d: %d\n",t+1,ans);
    }
    return 0;
}
