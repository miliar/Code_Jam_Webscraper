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
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
#endif
    ios_base::sync_with_stdio(0);
    int a[4][4],b[4][4],a1,a2,ans,ac,t;
    cin>>t;
    FORE(tt,1,t)
    {
        cout<<"Case #"<<tt<<": ";
        ac=0;
        cin>>a1;--a1;
        REP(i,4) REP(j,4) cin>>a[i][j];
        cin>>a2;--a2;
        REP(i,4) REP(j,4) cin>>b[i][j];
        REP(i,4) REP(j,4) if(a[a1][i]==b[a2][j]) {ac++;ans=a[a1][i];}
        if(ac==0) cout<<"Volunteer cheated!\n";
        else if(ac==1) cout<<ans<<endl;
        else cout<<"Bad magician!\n";
    }
    return 0;
}
