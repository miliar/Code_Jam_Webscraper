#include<iostream>
#include<vector>
#include<cstdio>
#include<iomanip>
using namespace std;
int main()
{
    long long t;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double mini=9999999999.0;
        double crr=0.0;
        double cps=2.0;
        while(1)
        {
            double fin=crr+x/cps;
            if(fin<mini)mini=fin;
            else break;
            double nextfarm=c/cps;
            crr+=nextfarm;
            cps+=f;
        }
        cout<<"Case #"<<i+1<<": ";
        cout<<fixed<<setprecision(7) << mini << '\n';
    }
    return 0;
}
