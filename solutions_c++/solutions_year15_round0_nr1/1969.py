#include<bits/stdc++.h>
#define in freopen("input.txt","r",stdin)
#define out freopen("output.txt","w",stdout)

#define inp freopen(".in","r",stdin)
#define outp freopen(".out","w",stdout)

using namespace std;

#define pb push_back
#define pf push_front
#define p_f pop_front
#define p_b pop_back
#define LL long long int
#define LD long double
#define MP make_pair
#define sqr(x) (x*x)
#define fi first
#define dist(x,y,xx,yy) sqrt( (x-xx)*(x-xx)+(y-yy)*(y-yy) )
#define lenint int intsi(int x){ int cnt=0; while(x>0){cnt++;x/=10;} return (cnt); }
#define se second
#define all(v) v.begin(),v.end()
#define sc scanf
#define DEBUG(a) cout<<#a<<" -> "<<a<<endl;
#define pr printf
#define si size()
#define str strlen
#define time clock()/(double)CLOCKS_PER_SEC
#define gcd LL GCD(LL a,LL b){ if(b==0)return a;else return GCD(b,a%b); }
const int INF=(-1u)/2;
const long long int INF2=(-1ull)/2;
int a,b,i,j,k,n,m,timer=0,l,r,x,y,t;
int cnt=0,fl=0,a2,a3=-1000000,ans=0;
string s;
main()
{
    sc("%d",&t);
    while(t>0)
    {
        cin>>n>>s;
        fl++;
        n++;
        x=0;
        cnt=0;
        for( i=0;i<n;i++ )
        {
            if( s[i]=='0' )continue;
            if( cnt>=i ){ cnt+=(s[i]-48); }
            else
            {
                x+=(i-cnt);
                cnt+=(i-cnt);
                cnt+=(s[i]-48);
            }
        }
        pr("Case #%d: %d\n",fl,x);
        t--;
    }
    return 0;
}
