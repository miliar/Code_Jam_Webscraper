#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;

#define FOR(i,a,b) for(register int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define mod 1000000009
#define MP make_pair
#define INF mod


int main()
{
#ifndef ONLINE_JUDGE
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
#endif
    ios_base::sync_with_stdio(0);
    int n,t,j1,j2;
    cin>>t;
    FOR(tt,1,t+1)
    {
        cout<<"Case #"<<tt<<": ";
        cin>>n;
        double a[n],b[n];
        REP(i,n) cin>>a[i];
        REP(i,n) cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        j1=j2=0;
        REP(i,n) if(a[i]>b[j2]) j2++;
        REP(i,n) if(a[j1]<b[i]) j1++;
        cout<<j2<<' '<<n-j1<<endl;
    }
    return 0;
}
