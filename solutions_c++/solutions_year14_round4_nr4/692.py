//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>   //我是沙茶....今天又写搓了。。
#include <fstream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <climits>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <utility>
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define abs(x) ((x)>0?(x):(-(x)))
#define FOR(i,a,b) for(int i = (a);i<=(b);i++)
#define FORD(i,a,b) for(int i = (a);i>=(b);i--)
#define REP(i,n) for(int i = 0;i<(n);i++)
#define rst(x,k) memset(x,k,sizeof(x))
#define lowbit(x) ((x)&(-(x)))
#define h(x) (1<<(x))
#define lson (ind<<1)
#define rson (ind<<1|1)
#define eps 1e-7
#define INF 100000000
#define maxn 110000
#define mod 1000000007LL
#define HASHMOD 3894229
#define Pi acos(-1.0)
#define link fjksldfjaslkdfjas
#define y1 fksjdlf
using namespace std;
typedef unsigned long long LL;
typedef pair<int,int> pii;
struct tire{
    int son[1010][26];
    int tot;
    void INIT(void){
        tot = 0;
        rst(son[tot],0);
    }
    void getnew(void){
        tot++;
        rst(son[tot],0);
    }
    void Insert(char *s){
        int now = 0;
        int len = strlen(s);
        REP(i,len){
            int cc = s[i] - 'A';
            if(son[now][cc] == 0){
                getnew();
                son[now][cc] = tot;
            }
            now = son[now][cc];
        }
    }
}sb;
int iCase;
int n,m;
char s[10][15];
int way , maxr;
vector<int> q[15];
void dfs(int dep){
    if(dep == m+1){
        int aa = 0;
        FOR(i,1,n){
            sb.INIT();
            int ss = q[i].size();
            if(ss == 0)return;
            REP(j,ss){
                sb.Insert(s[q[i][j]]);
            }
            aa += (sb.tot + 1);
        }
        if(aa > maxr){
            maxr = aa;
            way = 1;
        }else if(aa == maxr) way++;
        return;
    }
    for(int i = 1;i<=n;i++){
        q[i].push_back(dep);
        dfs(dep+1);
        q[i].pop_back();
    }
}
void solve(void){
    scanf("%d%d",&m,&n);
    way = 0 , maxr = -1;
    FOR(i,1,n)q[i].clear();
    FOR(i,1,m) scanf("%s",s[i]);
    dfs(1);
    printf("Case #%d: %d %d\n",++iCase,maxr,way);
}
int main(void){
    //freopen("D-small-attempt0.in" , "r" , stdin);
    //freopen("out.out" , "w" , stdout);
    iCase = 0;
    int casenum; scanf("%d",&casenum);
    while(casenum--) solve();
    return 0;
}
