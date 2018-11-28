/************************************************************
 *                                                          *
 *            ==>>BG_PeaceMind(BISHAL)               @NEPAL *
 *************************************************************/
#include<bits/stdc++.h>
#define MX 502
#define mpr(a,b) make_pair(a,b)
#define pii pair<int,int>
#define X first
#define Y second
#define SZ(x) x.size()
#define all(v) v.begin(),v.end()
#define pb(x) push_back(x)
#define clr(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define fr(i,a,n) for(i=a;i<=n;i++)
#define rf(i,a,n) for(i=a;i>=n;i--)
#define _cin ios_base::sync_with_stdio(0),cin.tie(0)
using namespace std;
typedef long long ll;
typedef double dd;
double C,F,X;
map<dd,dd>dp;
double solve(int pos,double val,double f)
{
    if(pos>=5*X) return val;
    //if(dp.find(val)!=dp.end()) return dp[val];
    //if(val>=X) return val;
    //if(f>=X/2.0) return val;
    //cout<<val<< " : "<<f<<endl;
    //
    dd a=val+(X/f);
    dd b=solve(pos+1,val+(C/f),f+F);
    //cout<<a<< " "<<b<<endl;
    return min(a,b);
}

int main()
{
    //_cin;
    freopen("B-small-attempt3.in","r",stdin);
    freopen("output3.txt","w",stdout);
    int tc,i,j,k,cs=1;
    scanf("%d",&tc);
    while(tc--)
    {
       // dp.clear();
        scanf("%lf%lf%lf",&C,&F,&X);
        double ans=solve(0,0,2);
        printf("Case #%d: %0.10lf\n",cs++,ans);
    }
    return 0;
}
