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
#define REPL(i,a,b) for (LL i=(a); i<=(b); i++)
#define PERL(i,a,b) for (LL i=(a); i>=(b); i--)
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
	REP(i,1,b)
	{
		multiply*=a;
	}
	return multiply;
}
inline LL ABS(LL a){return (a>=0)?a:-a;}

/*end of header*/
int main()
{
    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    int cnt[26],digit[10];
    string s;
    int t=0,T;
    cin>>T;
    while(++t<=T)
    {
        cin>>s;
        MEM(cnt,0);
        MEM(digit,0);
        REP(i,0,s.size()-1) cnt[s[i]-'A']++;
        while(cnt['Z'-'A']>0)
        {
            digit[0]++;
            cnt['Z'-'A']--;
            cnt['E'-'A']--;
            cnt['R'-'A']--;
            cnt['O'-'A']--;
        }
        while(cnt['X'-'A']>0)
        {
            digit[6]++;
            cnt['S'-'A']--;
            cnt['I'-'A']--;
            cnt['X'-'A']--;
        }
        while(cnt['U'-'A']>0)
        {
            digit[4]++;
            cnt['F'-'A']--;
            cnt['O'-'A']--;
            cnt['U'-'A']--;
            cnt['R'-'A']--;
        }
        while(cnt['W'-'A']>0)
        {
            digit[2]++;
            cnt['T'-'A']--;
            cnt['W'-'A']--;
            cnt['O'-'A']--;
        }
        while(cnt['G'-'A']>0)
        {
            digit[8]++;
            cnt['E'-'A']--;
            cnt['I'-'A']--;
            cnt['G'-'A']--;
            cnt['H'-'A']--;
            cnt['T'-'A']--;
        }
        while(cnt['F'-'A']>0)
        {
            digit[5]++;
            cnt['F'-'A']--;
            cnt['I'-'A']--;
            cnt['V'-'A']--;
            cnt['E'-'A']--;
        }
        while(cnt['V'-'A']>0)
        {
            digit[7]++;
            cnt['S'-'A']--;
            cnt['E'-'A']--;
            cnt['V'-'A']--;
            cnt['E'-'A']--;
            cnt['N'-'A']--;
        }
        while(cnt['R'-'A']>0)
        {
            digit[3]++;
            cnt['T'-'A']--;
            cnt['H'-'A']--;
            cnt['R'-'A']--;
            cnt['E'-'A']--;
            cnt['E'-'A']--;
        }
        while(cnt['O'-'A']>0)
        {
            digit[1]++;
            cnt['O'-'A']--;
            cnt['N'-'A']--;
            cnt['E'-'A']--;
        }
        digit[9]+=cnt['I'-'A'];
        cout<<"Case #"<<t<<": ";
        REP(i,0,9)
        {
            while(digit[i]>0)
            {
                cout<<i;
                digit[i]--;
            }
        }
        cout<<'\n';
    }
    return 0;
}

