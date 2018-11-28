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

#define M 100005
#define MD 1000000000LL
#define MX 10005

char rs[3][13][4100];
int sz[12],q[3][12][256];

char qs[]={"RPS"};
char ls[][5]={"RS","PR","PS"};

void srt(char s[],int l,int r)
{
    if(l==r)return ;
    int md=(l+r)/2;
    int i,j;
    for(i=0;i<(r-l+1)/2;i++)
    {
        if( s[l+i]==s[md+i+1] )continue;
        if(s[l+i]<s[md+i+1])break;
        else{
            for(i=0;i<(r-l+1)/2;i++)swap(s[l+i],s[md+i+1]);
            break;
        }
    }
    srt(s,l,md);
    srt(s,md+1,r);
    return ;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,i,j,k;

    rs[0][0][0]='P';
    rs[1][0][0]='R';
    rs[2][0][0]='S';
    sz[0]=1;
    mem(q);
    q[0][0]['P']++;
    q[1][0]['R']++;
    q[2][0]['S']++;
    f(t,3)
    {
        for(i=1;i<13;i++)
        {
            k=0;
            for(j=0;j<sz[i-1];j++)
            {
                int x;
                f(x,3)if(rs[t][i-1][j]==qs[x])break;
                rs[t][i][k++]=ls[x][0];
                rs[t][i][k++]=ls[x][1];
                q[t][i][ ls[x][0] ]++;
                q[t][i][ ls[x][1] ]++;
            }
            rs[t][i][k]='\0';
            sz[i]=k;

            srt(rs[t][i],0,sz[i]-1);
        }
    }
    int qs[3];
    sc(ts);
    while(ts--)
    {
        int n;
        sc4(n,qs[0],qs[1],qs[2]);
        n++;
        string qrs="IMPOSSIBLE";
        f(t,3)
        {
            //cout<<q[t][n-1]['R']<<" "<<q[t][n-1]['P']<<" "<<q[t][n-1]['S']<<endl;
            if( q[t][n-1]['R']==qs[0]&&q[t][n-1]['P']==qs[1]&&q[t][n-1]['S']==qs[2] )
            {
                if(qrs=="IMPOSSIBLE")qrs=string(rs[t][n-1]);
                else qrs=min(qrs,string(rs[t][n-1]));
            }
        }
        printf("Case #%d: %s\n",kk++,qrs.c_str());
    }

    return 0;
}
