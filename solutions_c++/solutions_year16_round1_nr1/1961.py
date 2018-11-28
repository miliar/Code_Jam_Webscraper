#include<bits/stdc++.h>
using namespace std;
int main()
{
     ifstream cin("concom.in");
    ofstream cout("concom.out");
    long long i,t,cont=0;
    string s,ans;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<++cont<<": ";
        cin>>s;
        ans=s[0];
        for(i=1;i<s.length();++i)
        {
            if(s[i]<ans[0])
            {
                ans+=s[i];
            }
            else ans=s[i]+ans;
        }
        cout<<ans<<endl;
    }
}
