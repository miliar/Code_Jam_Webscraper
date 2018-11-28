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
int a,b,i,d[1011000],j,k,n,m,timer=0,l,r,x,y,t,s;
int c[1011000],cnt=0,fl=0,a2,a3=-1000000,ans=0;
string s2,s1;
char rs[1001];
void rec( int id )
{
    if( id==s )
    {
        cnt=0;
        for( int i=0;i<s;i++ )
        {
            if( !(i+l-1<s) )continue;
            fl=0;
            for( int j=0;j<l;j++ )
            {
                if( s2[j]!=rs[i+j] ){ fl=1;break; }
            }
            if(fl==0)cnt++;
        }
        m=max(m,cnt);
        n+=cnt;
        ans++;
        return;
    }
    for( int i=0;i<k;i++ )
    {
        rs[id]=s1[i];
        rec(id+1);
    }
}
main()
{
    cin>>t;
    x=1;
    while( t>0 )
    {
        cin>>k>>l>>s;
        cin>>s1;
        cin>>s2;
        n=m=0;
        ans=0;
        rec(0);
        pr("Case #%d: ",x);
        x++;
        pr("%.7lf\n",(m*1.0)-((n*1.0)/(ans*1.0)));
        t--;
    }
    return 0;
}
