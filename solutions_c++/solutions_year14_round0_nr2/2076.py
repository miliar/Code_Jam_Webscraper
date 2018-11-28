#include <stdio.h>
#include <iostream>

using namespace std;

long double x,c,f,r,ans,a,b;

int main()
{
    int i,j,k,t,T;

    freopen("B-large(1).in","r",stdin);
    freopen("b-large.txt","w",stdout);

    std::cout.precision(7);
    std::cout <<  std::fixed;

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        cin>>c>>f>>x;

        ans=0.0;

        for(r=2.00; ; r+=f)
        {
            a=x/r;

            b=c/r+x/(r+f);

            if(a<b)
            {
                ans+=a;
                break;
            }

            ans+=c/r;

        }

        printf("Case #%d: ",t);
        cout<<ans<<endl;
    }

    return 0;
}
