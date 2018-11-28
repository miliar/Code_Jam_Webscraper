#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    short T,tc=0;
    cin>>T;
    while(tc++<T)
    {
        double c,x,f,t=0,r=2;
        short flag=0;
        cin>>c>>f>>x;
        while((x/r)>((c/r)+x/(r+f)))
        {
            t+=c/r;
            r+=f;            
        }
        t+=x/r;
        cout<<"Case #"<<tc<<": "<<setprecision(7)<<fixed<<t<<endl;
    }    
    return 0;
}
