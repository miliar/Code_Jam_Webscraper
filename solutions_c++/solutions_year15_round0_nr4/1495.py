#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
using namespace std;

int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("output4.txt","w",stdout);
    int t,q=0;
    cin>>t;
    while(t--)
    {
        q++;
        ll x,r,c;
        cin>>x>>r>>c;
        string ans;
        if((r*c)%x!=0)
        {
            ans="RICHARD";
            goto ab;
        }
        else if(x==1)
        {
            ans="GABRIEL";
            goto ab;
        }
        else if(x==2&&(r*c)%x==0)
        {
            ans="GABRIEL";
            goto ab;
        }

        else if(x==3)
        {
            if(r*c==3)
            {
                ans="RICHARD";
            }
            else
            {
                ans="GABRIEL";
            }
            goto ab;
        }
        else if(x==4)
        {
            if(r*c==12 || r*c==16)
                ans="GABRIEL";
            else
                ans="RICHARD";
            goto ab;
        }
        ab:
        //cout<<"Case #"<<q<<": "<<ans<<"\n";
        cout<<"Case #"<<q<<": "<<ans<<"\n";

    }
    return 0;
}
