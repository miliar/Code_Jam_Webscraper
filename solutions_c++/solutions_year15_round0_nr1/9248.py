#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{

    //freopen("i.txt","r",stdin);
    //freopen("o.txt","w",stdout);
    int t;
    cin>>t;
    for(int u=1;u<=t;u++)
    {
        long long  n,pre=0,ans=0;
        string st;
        cin>>n;
        cin>>st;
        pre+=st[0]-'0';
       // cout<<pre<<":D"<<endl;
        for(int i=1;i<=n;i++)
        {
            if(i>pre && st[i]!='0')
            {
                ans+=(i-pre);
                pre+=(i-pre);
                //cout<<i<<" "<<ans<<":P"<<endl;
                pre+=st[i]-'0';

            }
            else
            {
                pre+=st[i]-'0';
            }

        }
        cout<<"Case #"<<u<<": "<<ans<<endl;

    }
       return 0;
}
