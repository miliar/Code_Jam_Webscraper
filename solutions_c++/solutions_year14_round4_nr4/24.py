// @author 1rw6
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

#define MAXN 1005
#define MAXL 1005
#define MAXK 1005

const int mod=1000000007;

int dp[30][MAXK];
int cm[MAXK][MAXK];

inline int add(int a,int b) {
    return a+b<mod?a+b:a+b-mod;
}
inline int subtract(int a,int b) {
    return a<b?a-b+mod:a-b;
}
inline int mult(int a,int b) {
    return (long long)a*b%mod;
}
inline int sub(int n,const vector<int> &s) {
    int k=s.size();
    int sol=1;
    for(int i=0;i<k;i++)
        sol=mult(sol,cm[n][s[i]]);
    return sol;
}
inline int gao(int n,const vector<int> &s) {
    int k=s.size();
    if(!k) return 1;
    int sol=0;
    for(int i=0;i<n;i++) {
        int val=mult(sub(n-i,s),cm[n][n-i]);
        if(i&1) val=subtract(0,val);
        sol=add(sol,val);
    }
    /*printf("%d:",n);
    for(int i=0;i<k;i++)
        printf(" %d",s[i]);
    printf("\n => %d\n",sol);*/
    return sol;
}

class Node {
    public:
        int cnt[27];
        Node *next[27];
        Node() {
            memset(cnt,0,sizeof(cnt));
            memset(next,0,sizeof(next));
        }
        ~Node() {
            for(int i=0;i<27;i++)
                delete next[i];
        }
        Node *get_next(int ind) {
            if(!next[ind]) next[ind]=new Node();
            return next[ind];
        }
        void append(string &s,int x,int pre) {
            if(x>=s.length()) {
                cnt[26]++;
                return;
            }
            int ind=s[x]-'A';
            if(x>=pre) cnt[ind]++;
            get_next(ind)->append(s,x+1,pre);
        }
        void dfs(int inc,int &ans) {
            vector<int> arr;
            for(int i=0;i<27;i++)
                if(cnt[i]) arr.PB(cnt[i]);
            ans=mult(ans,gao(inc,arr));
            for(int i=0;i<27;i++)
                if(next[i]) next[i]->dfs(cnt[i],ans);
        }
};

int nstring,sz;
string str[MAXN];

inline int diff(string from,string to) {
    int i;
    for(i=0;i<from.length()&&i<to.length();i++)
        if(from[i]!=to[i]) break;
    return to.length()-i;
}

void solve() {
    //
    Node rt;
    sort(str,str+nstring);
    int maxnd=sz;
    for(int i=0;i<nstring;i++) {
        string prev=(i<sz?"":str[i-sz]);
        int d=diff(prev,str[i]);
        int pre=str[i].length()-d;
        rt.append(str[i],0,pre);
        maxnd+=d;
        //fprintf(stderr,"%s ",str[i].c_str());
        //DPRII(i,d);
    }
    //
    int ways=1;
    rt.dfs(sz,ways);
    //
    PRI(maxnd,ways);
}

int main(void)
{
    int t,cas;
    RI(t);
    memset(cm,0,sizeof(cm));
    for(int i=0;i<MAXK;i++) {
        cm[i][0]=cm[i][i]=1;
        for(int j=1;j<i;j++)
            cm[i][j]=add(cm[i-1][j-1],cm[i-1][j]);
    }
    for(cas=1;cas<=t;cas++) {
        RI(nstring,sz);
        for(int i=0;i<nstring;i++)
            cin >> str[i];
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread

