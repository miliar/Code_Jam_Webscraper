#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for( int tt=1; tt<=t; ++tt )
    {
        double c,f,x,minmtime=INT_MAX,currtime=0,currrate=2;
        int cookies=0;
        cin>>c>>f>>x;
        while( currtime<minmtime )
        {
            //#1
            minmtime=min(minmtime,currtime+((x-cookies)/currrate));
            //#2
            currtime+=(c-cookies)/currrate;
            cookies=0;
            currrate+=f;
        }
        printf("Case #%d: %.7lf\n",tt,minmtime);
    }
    return 0;
}
