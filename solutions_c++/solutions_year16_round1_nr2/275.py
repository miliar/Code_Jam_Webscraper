//{{{
#include <bits/stdc++.h>
using namespace std;
//types
typedef long long ll;
typedef pair<int,int> pii;
//input
bool SR(int &x){return scanf("%d",&x)==1;}bool SR(ll &x){return scanf("%lld",&x)==1;}
bool SR(double &x){return scanf("%lf",&x)==1;}bool SR(char *s){return scanf("%s",s)==1;}
bool RI(){return true;}
template<typename I,typename... T>bool RI(I &x,T&... tail){return SR(x) && RI(tail...);}
//output
void SP(const int x){printf("%d",x);}void SP(const ll x){printf("%lld",x);}
void SP(const double x){printf("%.16lf",x);}void SP(const char *s){printf("%s",s);}
void PL(){puts("");}
template<typename I,typename... T>void PL(const I x,const T... tail)
{SP(x);if(sizeof...(tail)) putchar(' ');PL(tail...);}
//macro
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,n) for(int i=0;i<int(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=int(b);i++)
#define pb push_back
#define mkp make_pair
#define F first
#define S second
//debug
#ifdef darry140
template<typename I>
void _DOING(const char *s,I&& x){cerr<<s<<"="<<x<<endl;}//without ','
template<typename I,typename... T>
void _DOING(const char *s,I&& x,T&&... tail)//with ','
{
    int c=0;
    static const char bra[]="({[";
    static const char ket[]=")}]";
    while(*s!=',' || c!=0)//eg. mkp(a,b)
    {
        if(strchr(bra,*s)) c++;
        if(strchr(ket,*s)) c--;
        cerr<<*s++;
    }
    cerr<<"="<<x<<", ";
    _DOING(s+1,tail...);
}
#define debug(...) do{\
    fprintf(stderr,"%s:%d - ",__PRETTY_FUNCTION__,__LINE__);\
    _DOING(#__VA_ARGS__,__VA_ARGS__);\
}while(0)
template<typename It>
ostream& _OUTC(ostream &s,It b,It e)//container
{
    s<<"{";
    for(auto it=b;it!=e;it++) s<<(it==b?"":" ")<<*it;
    s<<"}";
    return s;
}
template<typename A,typename B>
ostream& operator <<(ostream&s, const pair<A,B> &p){return s<<"("<<p.F<<","<<p.S<<")";}
template<typename A,typename B>
ostream& operator <<(ostream&s, const map<A,B> &c){return _OUTC(s,ALL(c));}
template<typename T>
ostream& operator <<(ostream&s, const set<T> &c){return _OUTC(s,ALL(c));}
template<typename T>
ostream& operator <<(ostream&s, const vector<T> &c){return _OUTC(s,ALL(c));}
#else
#define debug(...)
#endif
//}}}

int main()
{
    int t;RI(t);
    REP1(cas,1,t)
    {
        int n;RI(n);
        set<int> s;
        REP(i,2*n-1) REP(j,n)
        {
            int x;RI(x);
            if(s.count(x)) s.erase(x);
            else s.insert(x);
        }
        vector<int> ans(ALL(s));
        printf("Case #%d: ",cas);
        assert(is_sorted(ALL(ans)) && SZ(ans)==n);
        REP(i,n) printf("%d%c",ans[i]," \n"[i==n-1]);
    }
    return 0;
}




































/*End Of File*/

