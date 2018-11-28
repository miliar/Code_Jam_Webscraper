#include <cstdio>

using namespace std;

int fr[11], ok;

int cond()
{
    for(int i=0;i<=9;i++)
        if(fr[i]==0)
            return 0;
    return 1;
}

void cifre(int n)
{
    ok=0;
    do
    {
        fr[n%10]++;
        if(cond()==1)
            ok=1;
        n/=10;
    }
    while(n);
}

int main()
{
    freopen("sheep.in","r",stdin);
    freopen("sheep.out","w",stdout);
    int n;
    long int x;
    scanf("%d\n", &n);
    for(int i=1;i<=n;i++)
    {
        scanf("%ld\n",&x);
        ok=0;
        for(int j=0;j<=9;j++)
            fr[j]=0;
        cifre(x);
        if(ok==1)
            printf("CASE #%d: %ld\n", i, x);
        if(x==0)
        {
            ok=1;
            printf("CASE #%d: INSOMNIA\n", i);
        }
        for(int j=2;ok==0;j++)
        {
            cifre(j*x);
            if(ok==1)
                printf("CASE #%d: %ld\n", i,x*j);
        }
    }
    return 0;
}
