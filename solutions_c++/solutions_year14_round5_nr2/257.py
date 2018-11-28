// @author kelvin
// #includes {{{
#include <bits/stdc++.h>
using namespace std;
// }}}
// #defines {{{
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define POP() pop_back()
#define F first
#define S second
#define PR printf
void RI() {}
template<typename... T>
void RI(int& head,T&... tail) {
    scanf("%d",&head);
    RI(tail...);
}
void PRI(int x) {
    printf("%d\n",x);
}
template<typename... Args>
void PRI(int head,Args... tail) {
    printf("%d ",head);
    PRI(tail...);
}
#define RF(x) scanf("%lf",&(x))
#define RS(x) scanf("%s",x)
#define DPRI(x) fprintf(stderr,"<"#x"=%d>\n",x)
#define DPRII(x,y) fprintf(stderr,"<"#x"=%d, "#y"=%d>\n",x,y)
#define DPRIII(x,y,z) fprintf(stderr,"<"#x"=%d, "#y"=%d, "#z"=%d>\n",x,y,z)
#define DPRIIII(x,y,z,w) fprintf(stderr,"<"#x"=%d, "#y"=%d, "#z"=%d "#w"=%d>\n",x,y,z,w)
#define DPRF(x) fprintf(stderr,"<"#x"=%lf>\n",x)
#define DPRS(x) fprintf(stderr,"<"#x"=%s>\n",x)
#define DPRMSG(x) fprintf(stderr,#x"\n")
#define DPRPII(x) fprintf(stderr,"<"#x"=(%d,%d)>\n",x.F,x.S)
typedef pair<int,int> pii;
// }}}
// #functions {{{
pii operator+(const pii &a,const pii &b) { return MP(a.F+b.F,a.S+b.S); }
pii operator-(const pii &a,const pii &b) { return MP(a.F-b.F,a.S-b.S); }
pii& operator+=(pii &a,const pii &b) { a.F+=b.F; a.S+=b.S; return a; }
pii& operator-=(pii &a,const pii &b) { a.F-=b.F; a.S-=b.S; return a; }
template <class T,class U>
bool cmp_second(const pair<T,U> &a,const pair<T,U> &b) { return a.second<b.second; }
template <class T>
T gcd(T a,T b) { a=abs(a); b=abs(b); while(b) { T t=b; b=a%b; a=t; } return a; }
template <class T>
pair<T,T> ext_gcd(T a,T b) {
   T a0=1,a1=0,b0=0,b1=1;
   if(a<0) { a=-a; a0=-1; }
   if(b<0) { b=-b; b1=-1; }
   while(b) {
      T t,q=a/b;
      t=b; b=a-b*q; a=t;
      t=b0; b0=a0-b0*q; a0=t;
      t=b1; b1=a1-b1*q; a1=t;
   }
   return MP(a0,a1);
}
inline int sg(int x) { return x?(x>0?1:-1):0; }
inline string concatenate_strings(vector<string> ss) {
   string s;
   for(int i=0;i<ss.size();i++)
      s+=ss[i];
   return s;
}
template <class T>
inline vector<T> read_from_string(string s) {
   vector<T> ret; stringstream ss(s,stringstream::in);
   while(1) { T x; ss>>x; ret.push_back(x); if(ss.eof()) break; }
   return ret;
}
// }}}

#define MAXN 105
#define MAXH 205

int dmg1,dmg2,n;
int hp[MAXN],gold[MAXN];
//
/*int dp[MAXN][2];

int solve1() {
    // 1: my turn next
    dp[0][0]=dp[0][1]=0;
    for(int i=0;i<n;i++) {
        if(hp[i]<=dmg2) {
            dp[i+1][0]=max(dp[i][0],dp[i][1]+gold[i]);
            dp[i+1][1]=max(dp[i][0],dp[i][1]);
        } else {
            dp[i+1][0]=max(dp[i][0],dp[i][1])+gold[i];
            dp[i+1][1]=max(dp[i][0],dp[i][1]);
        }
    }
    return max(dp[n][0],dp[n][1]);
}*/

const int maxval=MAXN*MAXH;
const int inf=1000000000;
//int dp[MAXN][maxval+1][2];
int dp[MAXN][maxval+1];

inline void relax(int &x,int val) { if(val>x) x=val; }
inline int kill1(int h) {
    int used=0;
    while(h%dmg2>dmg1&&h>=0) {
        h-=dmg1+dmg2;
        used++;
    }
    if(h<0) return -1;
    else return h/dmg2;
}
inline int kill0(int h) {
    int used=0;
    if(h<=dmg2) return -1;
    h-=dmg2;
    while(h%dmg2>dmg1&&h>=0) {
        h-=dmg1+dmg2;
        used++;
    }
    if(h<0) return -1;
    else return h/dmg2;
}
/*inline bool ok(int h) {
    if(dmg1>dmg2) return (h-dmg1+dmg2-1)/dmg2;
}*/
inline pii kill(int h) {
    int t=0;
    while(h>0) {
        if(h<=dmg1) return MP(t+1,(h-1)/dmg2);
        int rem=(h-1)%dmg2+1;
        if(rem<=dmg1) return MP(t+1,max(h-dmg1+dmg2-1,0)/dmg2);
        h-=dmg1;
        t++;
    }
    assert(false);
}
inline int nokill(int h) {
    return (h+dmg2-1)/dmg2;
}

int solve2() {
    int sol=0;
    for(int i=0;i<=n;i++)
        for(int u=0;u<=maxval;u++)
            dp[i][u]=-inf;
            //for(int b=0;b<2;b++)
            //    dp[i][u][b]=-inf;
    dp[0][0]=dp[0][1]=0;
    for(int i=0;i<n;i++) {
        int h=hp[i];
        int g=gold[i];
        /*
        int k1=kill1(h);
        int k0=kill0(h);
        int nk=nokill(h);
        */
        pii ret=kill(h);
        int c1=ret.F;
        int c2=ret.S;
        int nk=nokill(h);
        //printf("%d: %d %d %d\n",h,c1,c2,nk);
        for(int u=0;u<=maxval;u++) {
            if(dp[i][u]<0) continue;
            // dont hit
            relax(dp[i+1][u+nk],dp[i][u]);
            //relax(dp[i+1][u+nk-1][1],dp[i][u][0]);
            //relax(dp[i+1][u+nk-1][0],dp[i][u][0]);
            //relax(dp[i+1][u+nk][1],dp[i][u][1]);
            //relax(dp[i+1][u+nk][0],dp[i][u][1]);
            // hit
            if((dmg2<h||u>=c1)&&c1<=u+c2) relax(dp[i+1][u+c2-c1],dp[i][u]+g);
            //DPRI(dp[i][u]);
        }
    }
    for(int u=0;u<=maxval;u++)
        sol=max(sol,dp[n][u]);
    return sol;
}

int solve() {
    //if(dmg1>=dmg2) return solve1();
    //else return solve2();
    return solve2();
}

int main(void)
{
    int t,cas;
    RI(t);
    for(cas=1;cas<=t;cas++) {
        RI(dmg1,dmg2,n);
        for(int i=0;i<n;i++)
            RI(hp[i],gold[i]);
        int sol=solve();
        printf("Case #%d: %d\n",cas,sol);
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread

