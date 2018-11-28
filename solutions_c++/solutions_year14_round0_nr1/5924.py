#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("ttt.in","r",stdin);
    freopen("ttt.out","w",stdout);
    int t,c=1;cin>>t;
    while(t--)
    {
        int a;cin>>a;
        int arr[5],ii=0;
        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                int x;cin>>x;
                if(i==a)arr[ii++]=x;
            }
        }
        int b,match=0,ans;cin>>b;
        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                int y;cin>>y;
                if(i==b)
                {
                    for(int k=0;k<ii;++k)
                    {
                            if(arr[k]==y) match++,ans=y;
                    }
                }
            }
        }
        cout<<"Case #"<<c++<<": ";
        if(match)
        {
            (match==1)?cout<<ans<<endl:cout<<"Bad magician!\n";
        }
        else cout<<"Volunteer cheated!\n";
    }
    return 0;
}


