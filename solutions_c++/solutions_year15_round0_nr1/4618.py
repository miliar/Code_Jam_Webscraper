#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    long int i,j,t,sm,ans,cnt;
    string s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>sm>>s;
        ans=0;
        cnt=0;
        //cout<<s<<endl;
        for(j=0;j<=sm;j++)
        {
            if(j>cnt && s[j]!='0')
            {
                ans+=j-cnt;
                cnt+=j-cnt;
            }
            cnt+=s[j]-'0';
            //cout<<j<<" "<<cnt<<" "<<ans<<endl;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
