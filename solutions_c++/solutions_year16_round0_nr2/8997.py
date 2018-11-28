#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int r=t;
    while(t--)
    {

        string s;
        cin>>s;
        cout<<"Case #"<<r-t<<": ";
        int ans=0;
        if(s[s.length()-1]=='-')ans++;
        for(int i=1;i<s.length();i++)if(s[i]!=s[i-1])ans++;
        cout<<ans<<endl;
    }
    return 0;
}
