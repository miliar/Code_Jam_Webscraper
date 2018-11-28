#include<iostream>
#include<cstdio>
#include<fstream>
#include<iomanip>

using namespace std;

int main()
{
    int t;
    int k;
    ifstream cin("input.in");
    ofstream cout("output.out");
    cin>>t;
    for(k=1;k<=t;k++)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double xrp,crp,crc,xrc;
        xrp=x/2;crp=c/2,crc=0;
        double r=2;
        while(1)
        {
            //cout<<"hewee";
            r+=f;
            xrc=x/r;
            if(xrp<crp+xrc)
            break;
            xrp=xrc;
            crc+=crp;
            crp=c/r;
        }
        double ans= crc+xrp;
        cout << std::fixed;
        cout<<"Case #"<<k<<": ";
        cout<<setprecision(20)<<ans<<"\n";
    }
    return 0;
}
