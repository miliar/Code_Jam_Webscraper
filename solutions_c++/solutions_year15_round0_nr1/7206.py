#include<stdio.h>
#include<string.h>
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t,n,i;
    char ar[1005];
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {

        scanf("%d",&n);
        getchar();
        gets(ar);
        long long cnt=0,sum=0;
        int l=strlen(ar);
        sum+=(ar[0]-'0');
        for(i=1;i<l;i++)
        {
            long long nw=ar[i]-'0';
            if(sum<i)
            {
                cnt+=(i-sum);
                sum+=(i-sum);
            }
            sum+=nw;
        }
        printf("Case #%d: %lld\n",cs,cnt);

    }

    return 0;
}
