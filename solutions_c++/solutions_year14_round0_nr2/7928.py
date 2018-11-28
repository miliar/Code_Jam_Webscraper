#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
int Tcase,t;
double c,f,x;
const double eps=1e-10;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>Tcase;
    for(t=1;t<=Tcase;t++)
    {
        cin>>c>>f>>x;
        //cout<<c<<" "<<f<<" "<<x<<endl;
        double ans=0.0;
        double rate=2.0;
        if(x<=c)
        {
            cout<<"Case #"<<t<<": "<<fixed<<setprecision(10)<<x/rate<<endl;
            continue;
        }
        while(c*rate/f<=x-c)
        {
            //cout<<c*rate/f<<"---"<<x-c<<endl;
            //cout<<"timeadd:"<<c/rate<<"  rate:"<<rate<<endl;
            ans+=c/rate;
            rate+=f;
        }
        ans+=x/rate;
        cout<<"Case #"<<t<<": "<<fixed<<setprecision(10)<<ans<<endl;

    }
    return 0;
}
