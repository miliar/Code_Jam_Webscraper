#include<cstdio>
#include<cstring>
typedef long long LL;
double dp[1<<20];
double ddp[1<<20];
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ti;
    scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        char tmp[30];
        scanf("%s",tmp);
        int n=0,smask=0;
        for(;tmp[n];n++)
        {
            if(tmp[n]=='X')smask|=1<<n;
        }
        memset(dp,0,sizeof(dp));
        memset(ddp,0,sizeof(ddp));
        ddp[smask]=1;
        for(int mask=smask;mask<(1<<n)-1;mask=(mask+1)|smask)
        {
            for(int i=0;i<n;i++)
            {
                int w=i,t=n;
                while(mask&(1<<w))
                {
                    w=(w+1)%n;
                    t--;
                }
                dp[mask|(1<<w)]+=dp[mask]+t*ddp[mask];
                ddp[mask|(1<<w)]+=ddp[mask];
            }
        }
        printf("Case #%d: %.10f\n",ca,1.*dp[(1<<n)-1]/ddp[(1<<n)-1]);
    }
}
