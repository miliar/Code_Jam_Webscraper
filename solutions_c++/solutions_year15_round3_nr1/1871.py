#include <iostream>
#include"cmath"
#include"fstream"
using namespace std;
int l,c,r,t,T,ans;
int main()
{
    ifstream cin("1.in");
    ofstream cout("1.out");
    cin>>T;
    for (t=1;t<=T;t++)
    {
        cin>>c>>r>>l;
        if(c==1)
        {
            int co=0;
            for (int i=1;i<=r;i+=l)
            co++;
            ans=co*c+(l-1);
        }else
        {
           ans=(c/l)*(r/l)*l;
           if(r-2*l>=0)
           ans+=(c%l)*(r-2*l+2);
           else
            ans+=(c%l);
           if(c-2*l>=0)
            ans+=(r%l)*(c-2*l+2);
           else
            ans+=(r%l);
           if(l!=1)
            ans+=l;
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;


    }
    return 0;
}
