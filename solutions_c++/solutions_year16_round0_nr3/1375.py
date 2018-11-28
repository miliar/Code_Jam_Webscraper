/***************************************
    codeforces = topcoder = sahedsohel
    IIT,Jahangirnagar University(42)
****************************************/
#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ull unsigned long long int
#define inf (INT_MAX/10)
#define linf (LLONG_MAX/10LL)
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sc4(a,b,c,d) scanf("%d%d%d%d",&a,&b,&c,&d)
#define fl(c,i,n) for(i=c;i<n;i++)
#define f(i,n) for(i=0;i<n;i++)
#define mem(a) memset(a,0,sizeof(a))
#define memn(a) memset(a,-1,sizeof(a))
#define pb push_back
#define pp pop_back()
#define aov(a) a.begin(),a.end()
#define mpr make_pair
#define PI (2.0*acos(0.0)) //#define PI acos(-1.0)
#define xx first
#define yy second
#define mxv(a) *max_element(aov(a))
#define mnv(a) *min_element(aov(a))
#define LB(a,x) (lower_bound(aov(a),x)-a.begin())
#define UB(a,x) (upper_bound(aov(a),x)-a.begin())
#define to_c_string(a) a.c_str()
#define strtoint(c) atoi(&c[0])
#define pii pair< int , int >
#define pll pair< ll , ll >
#define pcs(a) printf("Case %d: ", a)
#define nl puts("")
#define endl '\n'
#define dbg(x) cout<<#x<<" : "<<x<<endl

template <class T> inline T bigmod(T p,T e,T M){ll ret = 1;for(; e > 0; e >>= 1){if(e & 1) ret = (ret * p) % M;p = (p * p) % M;}return (T)ret;}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}   // M is prime}
template <class T> inline T bpow(T p,T e){ll ret = 1;for(; e > 0; e >>= 1){if(e & 1) ret = (ret * p);p = (p * p);}return (T)ret;}

int toInt(string s){int sm;stringstream ss(s);ss>>sm;return sm;}
int toLlint(string s){long long int sm;stringstream ss(s);ss>>sm;return sm;}


///int mnth[]={-1,31,28,31,30,31,30,31,31,30,31,30,31};  //Not Leap Year
///int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int kdx[]={2,1,-1,-2,-2,-1,1,2};int kdy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int dx[]={-1,+1,0,1,0,-1}; // Hexagonal Direction   **
///int dy[]={-1,+1,1,0,-1,0}; //                       *#*
///                                                     **
const double eps=1e-9;

/*****************************************************************/
/// ////////////////////   GET SET GO    ////////////////////// ///
/*****************************************************************/

#define intx(i,j,k,l) ((a[i]*b[j]-b[i]*a[j])*(a[k]-a[l])-(a[i]-a[j])*(a[k]*b[l]-b[k]*a[l]))/((a[i]-a[j])*(b[k]-b[l])-(b[i]-b[j])*(a[k]-a[l]))
#define inty(i,j,k,l) ((a[i]*b[j]-b[i]*a[j])*(b[k]-b[l])-(b[i]-b[j])*(a[k]*b[l]-b[k]*a[l]))/((a[i]-a[j])*(b[k]-b[l])-(b[i]-b[j])*(a[k]-a[l]))
#define dst(u,v,x,y) sqrt((x*1.0-u*1.0)*(x*1.0-u*1.0)+(y*1.0-v*1.0)*(y*1.0-v*1.0))
#define area(i,j,k) ((ll)x[i]*y[j]+(ll)x[j]*y[k]+(ll)x[k]*y[i]-(ll)y[i]*x[j]-(ll)y[j]*x[k]-(ll)y[k]*x[i])

int ts,kk=1;

#define M 1000005
#define MD 1000000007LL
#define MX 10005

int n,m;
int sz,qz;
ll rs[5005][12],qs[12];
int qmx;

void chk(ll msk)
{
    ll i,j;

    f(i,11)rs[sz][i]=0;

    for(j=0;j<15;j++)
    {
        if( (msk&(1LL<<j))!=0 )
        {
            for(i=2;i<=10;i++)
            {
                rs[sz][i]=rs[sz][i]+bpow((ll)i,(ll)j);
            }
        }
    }
    rs[sz][0]=rs[sz][10];
    for(i=2;i<=10;i++)
    {
        if( (rs[sz][i]+bigmod((ll)i,(ll)n-1,2LL))%2LL==0 )rs[sz][i]=2;
        else
        {
            bool g=0;
            for(j=3;j<1001;j+=2)
            {
                if( (rs[sz][i]+bigmod((ll)i,(ll)n-1,(ll)j))%(ll)j==0 )
                {
                    g=1;
                    rs[sz][i]=j;
                    qmx=max((ll)qmx,j);
                    break;
                }
            }
            if(!g)return ;
        }
    }
    qz++;
    sz++;
//    cout<<sz<<" "<<msk<<endl;
    return ;
}

char s[35];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    ll t,i,j,k;

    sc(ts);
    while(ts--)
    {
        sz=0;
        sc2(n,m);
        qmx=2;
        for(i=0;i<(1LL<<14);i++)
        {
            ll msk=(ll)i*2LL+1;
//            cout<<msk<<endl;
            chk( msk );
            if(sz==m)break;
        }

        printf("Case #%d:\n",kk++);
        s[n]='\0';
        f(i,sz)
        {
            for(j=0;j<n;j++)
            {
                s[n-j-1]='0'+rs[i][0]%10LL;
                rs[i][0]/=10LL;
            }
            s[0]='1';
            printf("%s",s);
//            cerr<<s<<endl;
            fl(2,j,11)printf(" %lld",rs[i][j]);
            nl;
        }
//        cerr<<sz<<endl;
//        cout<<sz<<" "<<qz<<" "<<qmx<<endl;
    }

    return 0;
}
