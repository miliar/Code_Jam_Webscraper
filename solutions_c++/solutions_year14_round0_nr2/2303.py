#include <iostream>
#include <iomanip>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);

    int T,t;
    int j,k;

    double i,c,f,x,time;
    int m;

    cin>>t;
    T=t;
    while(t--)
    {
        time=0;
        cin>>c>>f>>x;
        m=x/c-2.0/f;
        for (i=0.0;i<m;i+=1.0)
        {
            time+=c/(2.0+i*f);
        }
        time+=x/(2.0+i*f);
        cout<<"Case #"<<T-t<<": "<<fixed<<setprecision(7)<<time<<endl;
    }
    return 0;
}
