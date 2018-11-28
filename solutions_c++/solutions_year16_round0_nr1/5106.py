#include <bits/stdc++.h>
using namespace std;
map<int,int>m;
int main()
{
    long long int a,b,c,d,T,sweep,i,j,p,q;
    scanf("%lld",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%lld",&sweep);
        m.clear();
        j=1;
        if(sweep==0)
        {
            printf("Case #%lld: insomnia\n",i);

        }
        else
        {d=sweep;

        b=0;
        while(1)
        {   a=d;
            while(a>0)
            {
                c=a%10;
                if(m[c]==0)
                {
                    b++;
                    m[c]=1;
                }
                a=a/10;
            }
            if(b>=10)
              break;
            j++;
            d=sweep*j;


        }
        printf("Case #%lld: %lld\n",i,d);

    }
    }
    return 0;
}


