#include<stdio.h>
#include<math.h>
int check(int *f)
{
    int i;
    for(i=0;i<10;i++)
        if(f[i]==0)return 0;
    return 1;
}
void updatef(int n,int *f)
{
    while(n>0)
    {
        f[n%10]++;
        n=n/10;
    }
}
int main()
{
    int t,n,test,cnt;
    scanf("%d",&t);
    for(test=1;test<=t;test++)
    {
        int f[10]={0};
        cnt=1;
        scanf("%d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",test);
            continue;
        }
        while(1)
        {
            updatef(cnt*n,f);
            if(check(f))
            {
                printf("Case #%d: %d\n",test,cnt*n);
                break;
            }
            cnt++;
        }
    }
}
