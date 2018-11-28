#include<bits/stdc++.h>

using namespace std;

typedef long long LL;

#define REP(i,n) FOR(i,0,n)
#define REPR(i,n) FORR(i,n,0)
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORR(i,a,b) for(int i=a;i>=0;i--)
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define inf mod

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("a.in","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    ios_base::sync_with_stdio(false);
    int t;
    double ans,c,f,x,r=2.0,minn;
    cin>>t;
    REP(i,t)
    {
        r=2.0;
        cout<<"Case #"<<i+1<<": ";
        cin>>c>>f>>x;
        //cout<<c<<' '<<f<<' '<<x<<endl;
        minn=(x/r);
        ans=(x/r);
        //cout<<r<<' '<<ans<<endl;
        r+=f;
        int cou=0;
        while(1)
        {
            //cout<<ans<<' '<<(x/r)<<' '<<(x/(r-f))<<' '<<(c/(r-f))<<' ';
            ans+=((x/r)-(x/(r-f))+(c/(r-f)));
            //cout<<ans<<endl;
            r+=f;
            if(ans < minn)
            {
                minn=ans; cou=0;
            }
            else
                cou++;
            if(cou>2)
                break;
        }
        cout<<fixed<<setprecision(7)<<minn<<endl;
    }
    return 0;
}
