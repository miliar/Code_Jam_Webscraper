#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for( int tt=1; tt<=t; ++tt )
    {
        set<int> p;
        int r1,r2,x,cnt=0,store;
        cin>>r1;
        for( int i=1; i<=4; ++i )
        {
            for( int j=1; j<=4; ++j )
            {
                cin>>x;
                if( i==r1 )
                {
                    p.insert(x);
                }
            }
        }
        cin>>r2;
        for( int i=1; i<=4; ++i )
        {
            for( int j=1; j<=4; ++j )
            {
                cin>>x;
                if( i==r2 )
                {
                    if(p.find(x)!=p.end())
                    {
                        store=x;
                        ++cnt;
                    }
                }
            }
        }
        //cout<<cnt<<endl;
        cout<<"Case #"<<tt<<": ";
        if( cnt ==1 )
            cout<<store<<endl;
        else if ( cnt>1 )
            cout<<"Bad magician!"<<endl;
        else if ( cnt==0 )
            cout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
