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
int a,b,i,d[1011000],j,k,n,m,timer=0,l,r,x,y,t;
int c[1011000],cnt=0,fl=0,a2,a3=-1000000,ans=0;
priority_queue<int>q;
main()
{
    sc("%d",&t);
    while(t>0)
    {
        sc("%d",&n);
        for( i=0;i<n;i++ )
        {
            sc("%d",&c[i]);
        }
        cnt=10000;
        for( i=1;i<=1000;i++ )
        {
            ans=0;
            for( j=0;j<n;j++ )
            {
                if( c[j]<=i )continue;
                a=c[j]/i;
                if( (c[j]+a-1)/a>i )a++;
                r=a-1;
                ans+=r;
            }
            //if(i==2)cout<<ans<<endl;
            cnt=min(cnt,i+ans);
        }
        fl++;
        pr("Case #%d: %d\n",fl,cnt);
        t--;
    }
    return 0;
}
