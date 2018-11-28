#include<iostream>
#include<iomanip>

using namespace std;

int main()
{
    int t,k;
    long double c,f,x,ti,r,m,t1,t2;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        ti=0;
        r=2;
        cin>>c>>f>>x;
        a:
        m=c/r+x/(r+f);
        t1=x/r;
        t2=c/r;
        if(t1<m)
            ti+=t1;
        else
            {ti+=t2;
            r+=f;
            goto a;}
        cout.setf(ios::fixed);
        cout<<"Case #"<<k<<": "<<setprecision(7)<<ti<<endl;
    }
    return 0;
}
