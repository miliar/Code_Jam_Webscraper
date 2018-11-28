// @author kelvin
// #includes {{{
#include <cstdio>
#include <cstdlib>
#include <cmath>
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

#define MAXN 105

const double eps=1e-8;

class Coor {
    public:
        long long x,y;
        Coor(long long x=0,long long y=0):x(x),y(y) {}
        Coor& operator+=(const Coor &b) {
            x+=b.x;
            y+=b.y;
            return *this;
        }
        Coor operator+(const Coor &b) const {
            return Coor(*this)+=b;
        }
        Coor& operator-=(const Coor &b) {
            x-=b.x;
            y-=b.y;
            return *this;
        }
        Coor operator-(const Coor &b) const {
            return Coor(*this)-=b;
        }
};

inline long long dot(Coor a,Coor b) { return a.x*b.x+a.y*b.y; }
inline long long cross(Coor a,Coor b) { return a.x*b.y-a.y*b.x; }
bool cmp(Coor a,Coor b) {
    return cross(a,b)>0;
}

inline long long readf2l() {
    double x;
    scanf("%lf",&x);
    return (long long)(x*10000+0.5);
}

int n;
long long sum,temp;
Coor vec[MAXN];

double intersect(Coor a,Coor b) {
    if(a.x>b.x) swap(a,b);
    if(a.x>0||b.x<0) return 0;
    if(a.x==b.x) return max(a.y,b.y);
    return a.y+(double)(b.y-a.y)*(0-a.x)/(b.x-a.x);
}

bool solve() {
    Coor p,o;
    sort(vec,vec+n,cmp);
    // minkowski
    double my=0.0;
    for(int i=0;i<2*n;i++) {
        Coor dv=(i<n)?vec[i]:o-vec[i-n];
        Coor np=p+dv;
        // p--np
        // printf("%.3lf %.3lf  %.3lf %.3lf\n",p.x,p.y,np.x,np.y);
        // printf("> %.3lf\n",intersect(p,np));
        my=max(my,intersect(p,np));
        p=np;
    }
    if(my<=eps) return 0;
    double sol=sum/my;
    printf("%.9lf\n",sol);
    return 1;
}

int main(void)
{
    int t;
    RI(t);
    for(int cas=1; cas<=t; cas++) {
        RI(n);
        sum=readf2l();
        temp=readf2l();
        for(int i=0;i<n;i++) {
            vec[i].y=readf2l();
            vec[i].x=readf2l();
            vec[i].x-=temp;
            vec[i].x*=vec[i].y;
        }
        printf("Case #%d: ",cas);
        if(!solve()) puts("IMPOSSIBLE");
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread
