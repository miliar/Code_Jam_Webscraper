#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,ii;
    scanf("%lld",&t);
    for(ii=1;ii<=t;ii++)
    {
        long double c,f,x,tim,co,ttim;
        cin>>c>>f>>x;
        tim=x/2;
        co=c/2;
        ttim=co+(x/(2+f));
        int i=1;
        while(ttim<tim)
        {
            tim=ttim;
            co+=c/(2+i*f);
            i++;
            ttim=co+(x/(2+i*f));
        }
        cout.precision(11);
        cout<<"Case #"<<ii<<": "<<tim<<"\n";
    }
    return 0;
}
