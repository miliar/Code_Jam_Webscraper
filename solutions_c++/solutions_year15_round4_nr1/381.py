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
const int N=110,INF=1e9;
const LD EPS=1e-6;

int m,n;
int A[N];
char s[N][N];
map<PII,bool>M;
int dx[]={1,0,-1,0},dy[]={0,1,0,-1};
char ss[] = "v>^<";
int find(char c){   
    FOR(i,4)if(ss[i]==c)return i;
}
int test(int x,int y,int lastd){
    if(x<0||y<0||x>=n||y>=m)return 1;
    if(s[x][y]=='.'){
        return test(x+dx[lastd],y+dy[lastd],lastd);
    }
    if(lastd != -1)return 0;
    int d = find(s[x][y]);
    return test(x+dx[d],y+dy[d],d);
}
int solve() {
    int ans=0;
    FOR(i,n)FOR(j,m) if(s[i][j]!='.'){
        char tmp=s[i][j];
        if(!test(i,j,-1))continue;
        bool ok = false;
        FOR(k,4) {
            s[i][j] = ss[k];
            if(!test(i,j,-1))ok=true;
        }
        if(ok)ans++;
        else return -1;
    }
    return ans;
}
int main() {
    int w=1;
    RID(T);
    while(T--) {
        RI(n);RI(m);
        FOR(i,n)scanf("%s",s[i]);
        int ans=solve();
        if(ans==-1)printf("Case #%d: IMPOSSIBLE\n",w++);
        else printf("Case #%d: %d\n",w++,ans);
    }

    return 0;
}
/*

*/
