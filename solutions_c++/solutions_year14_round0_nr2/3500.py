#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int>   PI;
typedef vector<int> VI;
typedef long long LL;

#define FOR(i,a,b) for(register int i=a;i<b;i++)
#define FORE(i,a,b) FOR(i,a,b+1)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define mod 1000000007
#define MP make_pair
#define INF mod

int main()
{
#ifndef ONLINE_JUDGE
    freopen("B-large.in","r",stdin);
    freopen("a.out","w",stdout);
#endif
    ios_base::sync_with_stdio(0);
    double ans,temp,c,f,x;
    int t;cin>>t;
    FORE(tt,1,t)
    {
        cout<<"Case #"<<tt<<": ";
        cin>>c>>f>>x;
        ans=x/2;
        temp=c/2;
        for(int i=1;temp+(x/(2+i*f))<ans;i++)
        {
            ans=temp+(x/(2+i*f));
            temp+=(c/(2+i*f));
        }
        cout<<fixed<<setprecision(7)<<ans<<endl;
    }
    return 0;
}
