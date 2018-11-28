#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll hsh[100000];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t,ti=0;
    cin>>t;
    while(t--)
    {
        ti++;
        string st;
        cin>>st;
        ll k,c=0,ans=0,flg=1;
        cin>>k;
        memset(hsh,0,sizeof(hsh));
        for(int i=0;i<=st.size()-k;i++)
        {
            c+=hsh[i];
            if(c%2==0)
            {
                if(st[i]=='+')
                {

                }
                else
                {
                    c++;
                    hsh[i+k]--;
                    ans++;
                }
            }
            else
            {
                if(st[i]=='-')
                {

                }
                else
                {
                    c++;
                    hsh[i+k]--;
                    ans++;
                }
            }
        }
        for(int i=st.size()-k+1;i<st.size();i++)
        {
           c+=hsh[i];
            if(c%2==0)
            {
                if(st[i]=='+')
                {

                }
                else
                {
                   // cout<<i;
                    flg=0;
                }
            }
            else
            {
                if(st[i]=='-')
                {

                }
                else
                {
                    flg=0;
                }
            }
        }
        cout<<"Case #"<<ti<<": ";
        if(flg==1)
            cout<<ans<<"\n";
        else
        cout<<"IMPOSSIBLE"<<"\n";
    }
}
