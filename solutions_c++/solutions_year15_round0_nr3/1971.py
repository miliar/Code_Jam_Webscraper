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
string s,ss,o,tw,sd[100010],sd2[100010];
string solve( string a,string b )
{
    x=0;
    if( a[0]=='-' ){x++;a=a[1];}
    if( b[0]=='-' ){x++;b=b[1];}
    if( a=="1" && b=="1" )return "1";
    else if( a=="1" && b=="i" )return "i";
    else if( a=="1" && b=="j" )return "j";
    else if( a=="1" && b=="k" )return "k";

    if( a=="i" && b=="1" )return "i";
    else if( a=="i" && b=="i" )return "-1";
    else if( a=="i" && b=="j" )return "k";
    else if( a=="i" && b=="k" )return "-j";

    else if( a=="j" && b=="1" )return "j";
    else if( a=="j" && b=="i" )return "-k";
    else if( a=="j" && b=="j" )return "-1";
    else if( a=="j" && b=="k" )return "i";

    else if( a=="k" && b=="1" )return "k";
    else if( a=="k" && b=="i" )return "j";
    else if( a=="k" && b=="j" )return "-i";
    else if( a=="k" && b=="k" )return "-1";
}
int solve2( string a,string b )
{
    x=0;
    if( a[0]=='-' ){x++;a=a[1];}
    if( b[0]=='-' ){x++;b=b[1];}
    if( x%2!=0 )return 0;
    if( a=="1" && b=="j" )return 1;

    else if( a=="i" && b=="k" )return 1;

    else if( a=="j" && b=="-1" )return 1;
    else if( a=="k" && b=="-i" )return 1;
    return 0;
}
string take( string a,string b )
{
    a=solve(a,b);
    x%=2;
    if( x==1 )
    {
        if( a[0]=='-' ){a=a[1];return a;}
        else return ("-"+a);
    }
    return a;
}
main()
{
    sc("%d",&t);
    while(t>0)
    {
        fl++;
        sc("%d%d",&n,&m);
        cin>>ss;
        s="";
        for( i=0;i<m;i++ )s+=ss;
        n*=m;
        sd2[0]=s[0];
        if( 1<n )
        {
            o=s[0];
            tw=s[1];
            sd2[1]=take(o,tw);
        }
        for( i=0;i<n;i++ )
        {
            c[i]=0;
            d[i]=0;
            if( 1>=i )o=sd2[i];
            else { tw=s[i];sd2[i]=take(o,tw);o=sd2[i]; }
            if( o=="i" )c[i]=1;
        }
        sd[n-1]=s[n-1];
        if(n-2>=0)
        {
            o=s[n-2];
            tw=s[n-1];
            sd[n-2]=take( o,tw );
        }
        for( i=n-1;i>=0;i-- )
        {
            if( i>=(n-2) )o=sd[i];
            else { o=s[i];tw=s[i+1];o=take(o,tw);o=take(o,sd[i+2]);sd[i]=o;}
            if( o=="k" )d[i]=1;
        }
        d[n]=c[n]=0;
        for( i=0;i<n;i++ )
        {
            if( c[i]==1 )
            {
                for( j=i+1;j<n;j++ )
                {
                    if( d[j+1]==1 && solve2( sd2[i],sd2[j] ) )
                    {
                        pr("Case #%d: YES\n",fl);
                        goto rtt;
                    }
                }
            }
        }
        pr("Case #%d: NO\n",fl);
        rtt:;
        t--;
    }
    return 0;
}
