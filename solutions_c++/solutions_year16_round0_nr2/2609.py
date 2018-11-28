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
int solve(string s)
{
    if(s.size()==1)return s[0]=='-';
    int k=-1,t=-1,t1=-1;
    if(s[0]=='-')
    {
        PER(i,s.size()-1,0)if(s[i]=='-'){k=i;break;}
        REP(i,0,s.size()-1)if(s[i]=='+'){t=i;break;}
        if(t==-1)return 1;
        string s1=s.substr(0,k+1);
        reverse(ALL(s1));
        REP(i,0,s1.size()-1){if(s1[i]=='+')s1[i]='-';else s1[i]='+';}
        return 1+solve(s1);
    }
    else
    {
        PER(i,s.size()-1,0)if(s[i]=='-'){k=i;break;}
        REP(i,0,s.size()-1)if(s[i]=='-'){t=i;break;}
        if(k==-1) return 0;
        PER(i,k,0)if(s[i]=='+'){t1=i;break;}
        string s1=s.substr(0,t1+1);
        reverse(ALL(s1));
        return 2+solve(s1);
    }
}
int main()
{
    ifstream infile ("B-large.in");
    ofstream outfile ("B-large.out");
    int t=0,T;
    string s;
    infile>>T;
    while(++t<=T)
    {
        infile>>s;
        outfile<<"Case #"<<t<<": "<<solve(s)<<'\n';
    }
    return 0;
}
