#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int T;
string s;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Bans.out","w",stdout);
    cin>>T;
    for (int _=1;_<=T;_++)
    {
        cin>>s;
        cout<<"Case #"<<_<<": ";
        reverse(s.begin(),s.end());
        char c='+';
        int ans=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]!=c)
            {
                ans++;
                c=s[i];
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
