#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int T;
int m;
int n;
int f[13];

int deal(int i)
{
    while(i)
    {
        if(f[i%10]==0)
        {
            f[i%10]=1;
            f[11]++;
        }
        i/=10;
    }
    if(f[11]==10)
        return 1;
    else
        return 0;
}

int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);
    scanf("%d",&T);
    for(int it=1;it<=T;it++)
    {
        printf("Case #%d: ",it);
        scanf("%d",&m);
        if(m==0)
        {
            printf("INSOMNIA\n"); 
        }
        else
        {
            memset(f,0,sizeof(f));
            n=m;
            for(;;)
            {
                if(deal(n))
                {
                    printf("%d\n",n);
                    break;
                }
                n+=m;
            }
        }
    }
    return 0;
}
