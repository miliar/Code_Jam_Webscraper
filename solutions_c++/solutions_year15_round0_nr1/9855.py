#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("solution.txt","w",stdout);
    string in;
    int t,s,sMax,cnt=0,ans=0;

    cin>>t;
    for(int j=1; j<=t; ++j)
    {
        cin>>sMax>>in;

        cnt+=(in[0]-48);
        for(int i=1; i<in.length(); ++i)
        {
            if(cnt<i && (in[i]-48)>0)
            {
                ans+=(i-cnt);
                cnt+=ans;
            }
            cnt+=(in[i]-48);
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
        ans=0;
        cnt=0;
    }
    return 0;
}
