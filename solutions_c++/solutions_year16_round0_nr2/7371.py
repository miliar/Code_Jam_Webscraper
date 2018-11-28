#include<bits/stdc++.h>
using namespace std;
#define ll long long
string s;
int main()
{
    ll t,cnt,i,slen,z=0LL;
    freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        z++;
        cnt=0LL;
        cin>>s;
        slen=s.length();
        for(i=0;i<slen-1;i++)
        {
            if(s[i]!=s[i+1])
            {
                cnt++;
            }
        }
        if(s[i]=='-')
        {
            cnt++;
        }
        cout<<"Case #"<<z<<": "<<cnt<<"\n";
        s.clear();
    }
    return 0;
}