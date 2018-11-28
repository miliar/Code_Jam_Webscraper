#include <cstdio>
#include <math.h>

int sf[101]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521 };

bool palindrom(int a)
{
    if(a<10)
        return true;
    int og=0,b=a;
    while(b)
    {
        og=og*10+b%10;
        b=b/10;
    }
    if(a==og)
        return true;
    return false;
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,k=0;
    scanf("%d",&T);
    for(int j=1;j<=T;j++)
    {
        int a,b;
        k=0;
        scanf("%d %d",&a,&b);
        for(int i=0;i<19;i++)
            if(sf[i]>=a && sf[i]<=b)
                k++;
       /* a=sqrt(a);
        b=sqrt(b);
        for(int i=a;i<=b;i++)
        {
            if(palindrom(i)==true)
                if(palindrom(i*i)==true)
                    {
                        printf("%d,",i*i);
                        k++;
                    }
        }*/
       printf("Case #%d: %d\n",j,k);
    }
    return 0;
}
