#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("output.txt","w",stdout);

    int i,t;
    long double c,f,x,cc,tm,r,at,bt,tt;

    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        scanf("%Lf %Lf %Lf",&c,&f,&x);
        cc=tm=0;
        r=2;
        while(cc<x)
        {
            at=(c-cc)/r;
            bt=(x-cc)/r;
            if(at > bt)
            {
                tm+=bt;
                cc=x;
                break;
            }
            else
            {
                tt=at+(x/(r+f));
                if(tt < bt)
                {
                    r=r+f;
                    cc=0;
                    tm+=at;
                }
                else
                {
                    tm+=bt;
                    cc=x;
                    break;
                }
            }
        }
        printf("Case #%d: %.7Lf\n",i,tm);
    }

    return 0;
}
