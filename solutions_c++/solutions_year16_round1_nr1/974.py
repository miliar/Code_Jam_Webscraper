#include <iostream>
using namespace std;
int main()
{
    int t,tt,i;
    string s,ans;
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>s;
        ans=" ";
        ans[0]=s[0];
        for (i=1;i<s.size();i++)
            if (s[i]>=ans[0]) ans=s[i]+ans;
            else ans+=s[i];
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
