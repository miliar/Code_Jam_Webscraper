#include <bits/stdc++.h>
using namespace std;

#define inf (1<<30)-1
#define INF (1LL<<62)-1
#define MOD 1000000007LL
#define MP make_pair
#define PB push_back
#define ALL(x) x.begin(),x.end()
#define PI acos(-1)
#define MEM(x,y) memset(x,y,sizeof (x))
#define debug cout<<"A"<<'\n'
#define REP(i,a,b) for (int i=(a); i<=(b); i++)
#define PER(i,a,b) for (int i=(a); i>=(b); i--)
#define endl '\n'
#define print(x) cout<<x<<'\n'
#define dprint(a,x) cout<<setprecision(x)<<fixed<<a<<'\n'
#define itrALL(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int,int>PII;
typedef pair<LL,LL>PLL;
typedef set<int> SI;
typedef set<LL> SL;
typedef set<string> SS;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef map<LL,LL> MLL;
typedef queue<int> QI;

/* Direction Array */

// int fx[]={1,-1,0,0};
// int fy[]={0,0,1,-1};
// int fx[]={0,0,1,-1,-1,1,-1,1};
// int fy[]={-1,1,0,0,1,1,-1,-1};

template <class T> inline T bigmod(T p,T e,T M)
{
    T ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}

template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}
template <class T> inline T lcm(T a,T b) {a=abs(a);b=abs(b); return (a/gcd(a,b))*b;}
template <class T, class X> inline bool getbit(T a, X i) { T t=1; return ((a&(t<<i))>0);}
template <class T, class X> inline T setbit(T a, X i) { T t=1;return (a|(t<<i)); }
template <class T, class X> inline T resetbit(T a, X i) { T t=1;return (a&(~(t<<i)));}

inline LL power(LL a, LL b)
{
	LL multiply=1;
	REP(i,0,b)
	{
		multiply*=a;
	}
	return multiply;
}
inline LL ABS(LL a){return (a>=0)?a:-a;}

/*end of header*/
int main()
{
    ifstream infile ("A-large.in");
    ofstream outfile ("A-large.out");
    LL t=0,T,n,n1;
    set<int>s;
    infile>>T;
    while(++t<=T)
    {
        infile>>n;
        if(n==0)
        {
            outfile<<"Case #"<<t<<": INSOMNIA\n";
            continue;
        }
        s.clear();
        for(int i=1;;i++)
        {
            n1=n*i;
            while(n1>0)
            {
                s.insert(n1%10);
                n1/=10;
            }
            if(s.size()==10)
            {
                outfile<<"Case #"<<t<<": "<<n*i<<'\n';
                break;
            }
        }
    }
    return 0;
}

