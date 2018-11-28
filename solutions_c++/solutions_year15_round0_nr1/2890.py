#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,ii,n,stood,invite,i;
    string str;
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
        cin>>n>>str;
        stood=0;
        invite=0;
        for(i=0;i<=n;i++)
        {
            if(stood<i)
            {
                invite+=i-stood;
                stood=i;
            }
            stood+=str[i]-'0';
        }
        cout<<"Case #"<<ii<<": "<<invite<<"\n";
    }
}
