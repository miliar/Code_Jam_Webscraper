#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    FILE *file;
    long double c,f,x;
    file=fopen("final.o","w");
    long long int t;
    cin>>t;
    for(long long int k=1;k<=t;k++)
    {
        cin>>c>>f>>x;
        long double ans=0.0,a,b,m;
        long double rate=2.0;
        while(true)
        {
            a=(x*(1.0))/rate;
            b=(c*(1.0))/rate;
            m=(x*(1.0))/(rate+f);
            if(a<(b+m))
            {
                ans+=a;
                //cout<<ans<<endl;
                break;
            }
            else
            {
                ans+=b;
                rate+=f;
            }
            //cout<<ans<<endl;
        }
        fprintf(file,"Case #%lld: %.7Lf\n",k,ans);
        printf("%.7Lf\n",ans);

    }

}
