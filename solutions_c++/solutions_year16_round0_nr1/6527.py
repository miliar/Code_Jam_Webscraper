#include <cstdio>
int cnt[20];
int main()
{
    int ans,k,T,n;
    scanf("%d",&T);
    for(int i=1; i<=T; i++)
    {
       scanf("%d",&n);
        if(n==0)
            printf("Case #%d: INSOMNIA\n",i);
        else
        {
            for(int j=0; j<=9; j++)
                cnt[j]=0;
            ans=0;
            for(int j=1; ; j++)
            {
                k=n*j;
                while(k>0)
                {
                    ans+=cnt[k%10]^1;
                    cnt[k%10]=1;
                    k/=10;
                }
                if(ans==10)
                {
                    printf("Case #%d: %d\n",i,n*j);
                    break;
                }
            }
        }
    }
    return 0;
}
