#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("cj41.in","r",stdin);
   //freopen("out41.txt","w",stdout);
    int t,s,c,k;
    cin>>t;
    for(int co=1;co<=t;co++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<co<<": ";
        if(k==1)
            cout<<k<<endl;
        else if((c==1&&s<k)||s<k-1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            if(c==1&&s==k)
        {
            for(int i=1;i<=k;i++)
                cout<<i<<" ";
            cout<<endl;
        }
        else
        {
            for(int i=2;i<=k;i++)
                cout<<i<<" ";
            cout<<endl;
        }

    }
}
