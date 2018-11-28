#include <iostream>
using namespace std;
#define ll long long
int main()
{   ll t,i;
    cin>>t;
    for(i=0;i<t;++i)
    {   ll a,b,c,j;
        cin>>a>>b>>c;
        cout<<"Case #"<<i+1<<": ";
        for(j=1;j<=c;++j)
            cout<<j<<" ";
        cout<<"\n";
    }
    return 0;
}
