#include<stdio.h>
#include<string.h>
bool ok;
bool vis[10];
int coun;
void fenjie(long long x)
{
    while(x)
    {
        if(!vis[x%10])
        {
            vis[x%10]=true;
            coun++;
        }
        x/=10;
    }
}
int main()
{
    long long n;
    int t;
    scanf("%d",&t);
    int cases=0;
    while(t--)
    {
        cases++;
        printf("Case #%d: ",cases);
        scanf("%lld",&n);
        long long i=1;
        ok=true;
        memset(vis,0,sizeof(vis));
        coun=0;
        while(ok)
        {
            fenjie(n*i);
            //printf("%lld\n",n*i);
            if(coun==10)
            {
                break;
            }
            i++;
            if(i>10000000)
            {
                break;
            }
        }
        if(i>10000000)
        {
            printf("INSOMNIA\n");
        }
        else
        {
            printf("%lld\n",i*n);
        }
    }
    return 0;
}
