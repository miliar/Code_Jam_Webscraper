#include <bits/stdc++.h>
using namespace std;
long long nrt,i,nr,a,aux,c,t,ok,v[15],j;
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%lld",&nrt);

    for(i=1;i<=nrt;i++)
    {
        scanf("%lld",&a);
     // a=i;
        if(a==0)nr=-1;
        else
        {
            t=0;
            for(j=0;j<=9;j++)
                v[j]=0;
            while(1)
            {
                t++;
                ok=0;
                aux=a*t;
                while(aux>0)
                {
                    c=aux%10;
                    aux=aux/10;
                    v[c]=1;
                }
                for(j=0;j<=9;j++)
                    if(v[j]==0)ok=1;
                if(ok==0)
                {
                    nr=t*a;
                    break;
                }
            }
        }
        printf("Case #%lld: ",i);
        if(nr==-1)printf("INSOMNIA\n");
        else printf("%lld\n",nr);
    }
    return 0;
}
