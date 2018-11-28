#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<vector>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,z;
    int a=12;
    cout.precision(a);
    double c,f,x,ctime,ntime,rate,ans;
    cin>>t;
    for(z=1;z<=t;z++)
    {
        cin>>c>>f>>x;
        rate=2.0;
        ctime=(x/rate);
        ans=c/rate;
        ntime=ans+(x/(rate+f));
        rate+=f;
        while(ctime>ntime)
        {
            ctime=ntime;
            ans+=c/rate;
            ntime=ans+(x/(rate+f));
            rate+=f;
        }
        cout<<"Case #"<<z<<": "<<ctime<<endl;
    }
}
