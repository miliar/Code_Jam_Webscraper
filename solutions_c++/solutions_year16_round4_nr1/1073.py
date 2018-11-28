/*
Author :: MD. Musfiqur Rahman Sanim
Aust cse 28th Batch
ID:11.02.04.097
*/


//{ Template
using namespace std;
//{ headers
#include<bits/stdc++.h>
//}
//{ Loops
#define forab(i,a,b) for (__typeof(b) i = (a); i <= (b); ++i)
#define rep(i,n) forab (i, 0, (n) - 1)
#define For(i,n) forab (i, 1, n)
#define rofba(i,a,b) for (__typeof(b) i = (b); i >= (a); --i)
#define per(i,n) rofba (i, 0, (n) - 1)
#define rof(i,n) rofba (i, 1, n)
#define forstl(i,s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
//}
//{ Floating-points
#define EPS 1e-7
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2*acos (0.0)
//}
typedef long long int64;
typedef unsigned long long int64u;
#define memo(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define db double
#define pb push_back
#define eb emplace_back
#define pii pair<int ,int >
#define NL puts("")
#define ff first
#define ss second
//{
//Intput_Output
#define gc getchar
#define II ({ int a; read(a); a;})
#define IL ({ int64 a; read(a);  a;})
#define ID ({ db a; scanf("%lf",&a);  a;})
#define IC ({ char a; scanf("%c",&a);  a;})
#define IS ({ string a; cin >> a;  a;})
#define OC printf("Case #%d: ",cs);
//}
//}
#define _stl(x) {__stl_print__(x);}
#define __(args...) {dbg,args; cerr<<endl;}
template<class T>inline bool read(T &x){int c=gc();int sgn=1;while(~c&&c<'0'|c>'9'){if(c=='-')sgn=-1;c=gc();}for(x=0;~c&&'0'<=c&&c<='9';c=gc())x=x*10+c-'0';x*=sgn;return ~c;}
struct debugger{template<typename T> debugger& operator , (const T& v){cerr<<v<<"    "; return *this; }}dbg;
template <class T> void __stl_print__ (T &x) { // for all STL containers
    cerr << "["; forstl (i, x) cerr << (i != x.begin () ? ", " : "") << *i; cerr << "]" << endl;
}
template <class T, class U> inline T max (T &a, U &b)
{
    return a > b ? a : b;
}
template <class T, class U> inline T min (T &a, U &b)
{
    return a < b ? a : b;
}
template <class T, class U> inline T swap (T &a, U &b)
{
    T tmp = a;
    a = b;
    b = tmp;
}
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 Direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[6]={2,1,-1,-2,-1,1};int dy[6]={0,1,1,0,-1,-1}; //Hexagonal Direction

const int64 INF = (1ll)<<50;
const int mx = 1e5 + 7;
const int mod = 1000000007 ;
const db pi = PI;
int EQ(double d) {
    if ( fabs(d) < EPS ) return 0;
    return d > EPS ? 1 : -1 ;
}
string st;
int n,r,p,s;
string call(char ch,int pos){
    if(pos == 0) {
        string xx = "";
        xx += ch;
        return xx;
    }

    if(ch == 'R'){
        string a = call('S',pos-1);
        string b = call('R',pos-1);
        if(a < b) return a+b;
        else return b+a;

    }
    if(ch == 'S'){
        string a = call('P',pos-1);
        string b = call('S',pos-1);
        if(a < b) return a+b;
        else return b+a;
    }
    if(ch == 'P'){
        string a = call('R',pos-1);
        string b = call('P',pos-1);
        if(a < b) return a+b;
        else return b+a;
    }
}

bool check(string xx){
    int x1 = 0,x2 = 0,x3 = 0;

    int len = xx.size();
    rep(i,len){
        if(xx[i] == 'R')x1++;
        if(xx[i] == 'P')x2++;
        if(xx[i] == 'S')x3++;
    }

    return ((x1 == r) && (x2 == p) && (x3 == s));
}

int main() {
#ifdef Sanim
    //geting WA check int64 & int64u
    freopen ("in.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
#endif
    int t = II;
    For(cs,t){
        n = II,r = II,p = II,s = II;
        st = "";
        rep(i,p) st += "P";
        rep(i,r) st += "R";
        rep(i,s) st += "S";
        bool flag = true;
        OC;
        string R = call('R',n);
        string P = call('P',n);
        string S = call('S',n);
        if(check(R)){
            st = R;
            flag = 0;
        }
        if(check(P)){
            if(st == "" || st < P) st = P;
            flag = 0;
        }
        if(check(S)){
            if(st == "" || st < S) st = S;
            flag = 0;
        }

        if(flag){
            cout << "IMPOSSIBLE" << endl;
        }else cout << st << endl;
    }
}
