#include <iostream>
#include <cstdio>
#include <iomanip>
#include <string>
#include <queue>
#include <list>
#include <map>
using namespace std;
typedef long long ll;
typedef long double ld;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    cout<<fixed<<setprecision(7);
    for(int q=0;q<t;++q)
    {
        double x,c,f;
        cin>>c>>f>>x;
        cout<<"Case #"<<q+1<<": ";
        if (x<c)
        {
            cout<<x/2<<"\n";
            continue;
        }
        double ans=c/2,t=2;
        for(;;)
            if ((x-c)/t<x/(t+f))
            {
                ans+=(x-c)/t;
                break;
            } else
            {
                t+=f;
                ans+=c/t;
            }
        cout<<ans<<"\n";
    }
    return 0;
}
