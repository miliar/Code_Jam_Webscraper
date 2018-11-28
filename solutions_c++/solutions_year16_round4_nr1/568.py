/*
    Rezwan_4029 , AUST
*/

#include <bits/stdc++.h>

#define pb push_back
#define all(x) x.begin(),x.end()
#define ms(a,v) memset(a,v,sizeof a)
#define II ({int a; scanf("%d", &a); a;})
#define LL ({Long a; scanf("%lld", &a); a;})
#define DD ({double a; scanf("%lf", &a); a;})
#define ff first
#define ss second
#define mp make_pair
#define gc getchar
#define EPS 1e-10
#define pi 3.1415926535897932384626433832795
using namespace std;

#define FI freopen ("in.txt", "r", stdin)
#define FO freopen ("out.txt", "w", stdout)

typedef long long Long;
typedef unsigned long long ull;
typedef vector<int> vi ;
typedef set<int> si;
typedef vector<Long>vl;
typedef pair<int,int>pii;
typedef pair<string,int>psi;
typedef pair<Long,Long>pll;
typedef pair<double,double>pdd;
typedef vector<pii> vpii;

#define forab(i, a, b)	for (__typeof (b) i = (a) ; i <= b ; ++i)
#define rep(i, n)		forab (i, 0, (n) - 1)
#define For(i, n)		forab (i, 1, n)
#define rofba(i, a, b)	for (__typeof (b)i = (b) ; i >= a ; --i)
#define per(i, n)		rofba (i, 0, (n) - 1)
#define rof(i, n)		rofba (i, 1, n)
#define forstl(i, s)	for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)

#define __(args...) {dbg,args; cerr<<endl;}
struct debugger
{
    template<typename T> debugger& operator , (const T& v)
    {
        cerr<<v<<"\t";
        return *this;
    }
} dbg;
#define __1D(a,n) rep(i,n) { if(i) printf(" ") ; cout << a[i] ; }
#define __2D(a,r,c,f) forab(i,f,r-!f){forab(j,f,c-!f){if(j!=f)printf(" ");cout<<a[i][j];}cout<<endl;}

template<class A, class B> ostream &operator<<(ostream& o, const pair<A,B>& p)
{
    return o<<"("<<p.ff<<", "<<p.ss<<")";   //Pair print
}
template<class T> ostream& operator<<(ostream& o, const vector<T>& v)
{
    o<<"[";    //Vector print
    forstl(it,v)o<<*it<<", ";
    return o<<"]";
}
template<class T> ostream& operator<<(ostream& o, const set<T>& v)
{
    o<<"[";    //Set print
    forstl(it,v)o<<*it<<", ";
    return o<<"]";
}
template<class T> inline void MAX(T &a , T b)
{
    if (a < b ) a = b;
}
template<class T> inline void MIN(T &a , T b)
{
    if (a > b ) a = b;
}

//Fast Reader
template<class T>inline bool read(T &x)
{
    int c=gc();
    int sgn=1;
    while(~c&&c<'0'||c>'9')
    {
        if(c=='-')sgn=-1;
        c=gc();
    }
    for(x=0; ~c&&'0'<=c&&c<='9'; c=gc())x=x*10+c-'0';
    x*=sgn;
    return ~c;
}

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction

Long Pow(Long  b,Long  p)
{
    Long  ret = 1;
    while(p)
    {
        if(p&1) ret *= b ;
        p >>= (1ll) , b *= b ;
    }
    return ret ;
}

string toString(Long number)
{
    stringstream ss;
    ss << number;
    return ss.str();
}

const int N = 1 << 15;
char dp[N];
char x[] = { 'S', 'P', 'R' };
int ts, tp, tr;

void get(char c) {
    if (c == 'S') --ts;
    if (c == 'R') --tr;
    if (c == 'P') --tp;
}

void rec(string &s, int l, int r) {
    if (l == r) return;
    int m = (r + l) >> 1;
    int len = (r - l + 1) / 2;
    rec(s, l, m);
    rec(s, m+1, r);
    string a = s.substr(l, len);
    string b = s.substr(m + 1, len);
    if (a > b)
        for (int i = 0; i < len; ++i)
            swap(s[l + i], s[m + 1 + i]);

}

int main()
{
    FI; FO;
    int T = II;
    For(cs,T)
    {
        int n, s, p, r;
        cin >> n >> r >> p >> s;
        int mask = (1 << n);
        string ret = "Z";
        rep(ii, 3)
        {
            dp[1] = x[ii];
            ts = s, tp = p, tr = r;
            for (int i = 1; i < mask; ++i)
            {
                if (dp[i] == 'S')
                {
                    dp[i << 1] = 'P';
                    dp[i << 1 | 1] = 'S';
                }
                if (dp[i] == 'R')
                {
                    dp[i << 1] = 'R';
                    dp[i << 1 | 1] = 'S';
                }
                if (dp[i] == 'P')
                {
                    dp[i << 1] = 'P';
                    dp[i << 1 | 1] = 'R';
                }
            }
            for (int i = mask; i < (mask << 1); ++i)
            {
                get(dp[i]);
            }
            if (!ts && !tp && !tr)
            {
                string cur = "";
                for (int i = mask; i < (mask << 1); ++i)
                    cur += dp[i];
                rec(cur, 0, cur.size() - 1);
                ret = min(ret, cur);
            }
        }
        if (ret == "Z") ret = "IMPOSSIBLE";
        cout << "Case #" << cs << ": " << ret << endl ;
    }

}
