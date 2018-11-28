#include <iostream>
using namespace std;
int main()
{
    int t,c,ans,a,b,k;
    cin>>t;
    c=1;
    while(t--)
    {
        cin>>a>>b>>k;
        ans=0;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                //cout<<(i&j)<<endl;
                if((i&j)<k)
                {
                    ans++;
                    //cout<<i<<"   "<<j<<endl;
                }
            }
        }
        cout<<"Case #"<<c++<<": "<<ans<<endl;
    }
    return 0;
}
