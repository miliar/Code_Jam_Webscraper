// @author kelvin
// #includes {{{
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <algorithm>
#include <sstream>
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

#define MAXN 20000 // 1<<12

int p,n,c[6];
int g[MAXN],req[6];
char str[MAXN],tmp[MAXN];
char zz[4]="PRS";

inline int last(int x) {
    return x&(-x);
}

void solve() {
    g[n]=0;
    for(int b=n-1;b>0;b--) {
        int x=b+last(b);
        g[b]=(g[x]+1)%3;
    }
    memset(req,0,sizeof(req));
    for(int b=n;b>0;b--)
        req[g[b]]++;
    //
    for(int i=0;i<3;i++) {
        req[i+3]=req[i];
        c[i+3]=c[i];
    }
    //puts("");
    //printf(">> c: %d %d %d\n",c[0],c[1],c[2]);
    //printf(">> req: %d %d %d\n",req[0],req[1],req[2]);
    //
    for(int s=0;s<3;s++) {
        bool ok=true;
        for(int i=0;i<3;i++) {
            if(req[i]!=c[s+i]) {
                ok=false;
                break;
            }
        }
        //printf("<s=%d> %d %d %d\n",s,req[s+0],req[s+1],req[s+2]);
        if(ok) {
            for(int b=1;b<=n;b++)
                str[b]=zz[(g[b]+s)%3];
            for(int l=1;l<n;l*=2) {
                for(int i=1;i<=n;i+=l*2) {
                    char *a=str+i;
                    char *b=str+i+l;
                    if(strncmp(a,b,l)>0) {
                        strncpy(tmp,a,l);
                        strncpy(a,b,l);
                        strncpy(b,tmp,l);
                    }
                }
            }
            str[n+1]=0;
            puts(str+1);
            return;
        }
    }
    //
    puts("IMPOSSIBLE");
    return;
}

int main(void)
{
    int t;
    RI(t);
    for(int cas=1; cas<=t; cas++) {
        RI(p,c[1],c[0],c[2]);
        n=1<<p;
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread
