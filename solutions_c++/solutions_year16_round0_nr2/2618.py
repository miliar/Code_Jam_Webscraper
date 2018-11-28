#include<iostream>
#include<string>
using namespace std;
string s;
int main()
{
    int i,t,ca=1;
    cin>>t;
    while(t--)
    {
        cin>>s;
        int ans=1;
        for(i=1;i<s.size();i++)
        {
            if(s[i]!=s[i-1])ans++;
        }
        if(s[i-1]=='+')ans--;
        cout<<"Case #"<<ca<<": "<<ans<<endl;
        ca++;
    }
}
