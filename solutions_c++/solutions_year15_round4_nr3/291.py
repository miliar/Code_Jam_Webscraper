//by david942j
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <ctime>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <cstdlib>
#define openfile(s) freopen(s".in","r",stdin);freopen(s".out","w",stdout)
#define mpr std::make_pair
#define lg(x) (31-__builtin_clz(x))
#define __count __builtin_popcount
#define X first
#define Y second
#define mst(x) memset(x,0,sizeof(x))
#define mst1(x) memset(x,-1,sizeof(x))
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR1(i,n) for(int i=1;i<=n;i++)
#define FORit(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define pb push_back
#define RI(x) scanf("%d",&x)
#define RID(x) int x;RI(x)
using namespace std;
typedef long long LL;
typedef double LD;
typedef vector<int> VI;
typedef std::pair<int,int> PII;
template<class T>inline void maz(T &a,T b){if(a<b)a=b;}
template<class T>inline void miz(T &a,T b){if(a>b)a=b;}
template<class T>inline T abs(T a){return a>0?a:-a;}
inline int max(int a,int  b){return a>b?a:b;}
/*void RI() {}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}*/
const int N=1010,INF=1e9;
const LD EPS=1e-6;

int m;
int n;
char s[200000];
int top;
map<string,int>M;
int type[10000];
struct Sen{
    VI V;
    void read() {
        gets(s);
        V.clear();
        //fprintf(stderr,"read: %s\n",s);
        string tmp="";
        int n=strlen(s);
        for(int i=0;i<n;i++) 
            if(s[i]!=' '){
                tmp="";
                while(i<n && s[i]!=' ')tmp+=s[i++];
                if(M.count(tmp)==0)M[tmp]=++top;
                V.pb(M[tmp]);
            }
    }
    void set(int s) {
        for(auto c:V)
            type[c] |= 1<<s;
    }
}A[N];
int calc(int s){
    FOR1(i,top)type[i]=0;
    A[0].set(0);
    A[1].set(1);
    for(int i=2;i<n;i++) 
        A[i].set((s&(1<<i-2))!=0);
    int ans=0;
    FOR1(i,top)if(type[i]==3)ans++;
    return ans;
}
int solve() {
    int nn = 1<<n-2,ans=INF;
    for(int i=0;i<nn;i++)
        miz(ans,calc(i));
    return ans;
}
int main() {
    int w=1;
    RID(T);
    while(T--) {
        RI(n);
        top=0;
        M.clear();
        getchar();
        A[0].read();
        A[1].read();
        for(int i=2;i<n;i++)A[i].read();
        printf("Case #%d: %d\n",w++,solve());
    }

    return 0;
}
/*
0 + 9 + 19 + 109 + 199 + 1099
10000 41299 
*/
