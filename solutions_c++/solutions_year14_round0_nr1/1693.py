#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <climits>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#define REP(i,n) for( int (i)=0;(i)<(int)(n); ++(i))
#define REPR(i,n) for( int (i) = n; (i)>=0; --(i))
#define REPN(i,x,y) for( int i = x; (i) < (int)(y); (i)++ )
#define REPIT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define ZERO(x) memset(x,0,sizeof(x))
#define NEG(x) memset(x,-1,sizeof(x))
#define SZ(x) (int)(x).size()
#define RI(n) scanf("%d",&(n))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RS(x) scanf("%s",x)
#define OI(x) printf("%d\n",(x))
#define OII(x,y) printf("%d %d\n",(x),(y))
#define MP(x,y) make_pair((x),(y))
#define FT first
#define SD second
#define PB push_back
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
LL LLMAX = 9223372036854775807LL;
const int MOD = 1000000007;
const int maxn = 500+10;
int g[4][4];
int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif
    int T;
    RI(T);
    for(int kase = 1;kase<=T;++kase){
        int a1;
        RI(a1);
        REP(i,4)REP(j,4)RI(g[i][j]);
        set<int> s;
        REP(i,4)s.insert(g[a1-1][i]);
        RI(a1);
        REP(i,4)REP(j,4)RI(g[i][j]);
        int ans=-1,cc=0;
        REP(i,4)if(s.count(g[a1-1][i])>0){
            cc++;
            ans = g[a1-1][i];
        }
        if(cc>1)printf("Case #%d: Bad magician!\n",kase);
        else if(cc==0)printf("Case #%d: Volunteer cheated!\n",kase);
        else printf("Case #%d: %d\n",kase,ans);
    }
}


