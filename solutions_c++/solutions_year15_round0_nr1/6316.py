# include <bits/stdc++.h>
using namespace std;
# define ll long long int
int a[5000];
main()
{
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    int T;
    ll ans,count,S;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>S;
        for(int i=0;i<=S;i++){scanf("%1d",&a[i]);}
        if(a[0]==0)
        {
            ans=1;count=1;
        }

        else
        {
            ans=0;count=a[0];
        }
        for(int i=1;i<=S;i++)
        {
            if(count<i){ans+=(i-count);count+=(i-count);}
            count+=a[i];
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
}
