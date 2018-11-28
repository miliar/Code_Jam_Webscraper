#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("2.out","w",stdout);
	freopen("2.in","r",stdin);
	int t;
	cin>>t;
    for(int _=0;_<t;_++)
    {
        int ans=0;
        string s;
        cin>>s;
        reverse(s.begin(),s.end());
        char c='-';
        for(int i=0;i<s.size();i++)
            if(s[i]==c)
                ans++,
                c=(c=='+'?'-':'+');
        cout<<"Case #"<<_+1<<": "<<ans<<"\n";
    }
    return 0;
}
