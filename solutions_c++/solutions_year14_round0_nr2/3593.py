#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    double c,f,x,time,rt;
    int k,t;
    cin>>t;
    t++;
    cout<<fixed<<setprecision(7);
    for(k=1;k<t;k++)
    {
        time=0;
        rt=2;
        cin>>c>>f>>x;
        while(x/rt>(x/(rt+f)+c/rt))
        {
            time+=c/rt;
            rt+=f;
        }
        time+=x/rt;
        cout<<"Case #"<<k<<": "<<time<<"\n";
    }
    return 0;
}
