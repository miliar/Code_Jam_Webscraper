# include <bits/stdc++.h>
using namespace std;
# define ll long long int
main()
{
    int t,T;
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    cin>>T;
    ll x,r,c;
    int ans;
    for(int t=1;t<=T;t++)
    {
        cin>>x>>r>>c;
//        cout<<x<<r<<c<<endl;
        if(x==1)ans=2;
        else if(x==2){if(((r*c)%2)==0)ans=2;else ans=1;}
        else if(x==3)
        {
            if((r==1 || c==1) || (r==2 && c==2) || (r==2 && c==4) || (r==4 && c==2) || (r==4 && c==4))ans=1;
            else if((r==2 && c==3) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3))ans=2;
        }
        else if(x==4)
        {
            if((r*c)%4!=0 || (r==1 && c==4) || (r==4 && c==1) || (r==2 && c==2) || (r==2 && c==4) || (r==4 && c==2))ans=1;
            else if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4))ans=2;
        }

        if(ans==1)cout<<"Case #"<<t<<": "<<"RICHARD"<<endl;
        else if(ans==2)cout<<"Case #"<<t<<": "<<"GABRIEL"<<endl;
    }
}
