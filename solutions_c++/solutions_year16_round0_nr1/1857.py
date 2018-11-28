#include <iostream>
#include <cstdio>
using namespace std;
int T,co;
long long N,N2,N3;
bool dig[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%i",&T);
    for (int t=1;t<=T;t++)
    {
        printf("Case #%i: ",t);
        scanf("%lli",&N);
        co=10;
        for (int i=0;i<10;i++)dig[i]=0;
        for (int i=1;i<=100000000 && co;i++)
        {
            N2=N3=N*i;
            while (N2)
            {
                if (!dig[N2%10])
                {
                    co--;
                    dig[N2%10]=1;
                }
                N2/=10;
            }
        }
        if (co)puts("INSOMNIA");
        else printf("%lli\n",N3);
    }
}
