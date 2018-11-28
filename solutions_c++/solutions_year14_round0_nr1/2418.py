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
#define eps 1e-8
#define INF 500000000
#define maxn 1100
#define mod 1000000007LL
#define Pi acos(-1.0)
#define link fjksldfjaslkdfjas
using namespace std;
typedef long long LL;
int a[4][4];
int iCase;
vector<int> aa;
vector<int> bb;
void solve(void){
    int tt; scanf("%d",&tt);
    aa.clear(); bb.clear();
    REP(i,4)REP(j,4) scanf("%d",a[i] + j);
    REP(i,4) aa.push_back(a[tt-1][i]);
    scanf("%d",&tt);
    REP(i,4)REP(j,4) scanf("%d",a[i] + j);
    REP(i,4) bb.push_back(a[tt-1][i]);
    sort(aa.begin(),aa.end());
    sort(bb.begin(),bb.end());
    int ans = 0;
    int last;
    REP(i,4){
        REP(j,4){
            if(aa[i] == bb[j]){
                ans++;
                last = aa[i];
            }
        }
    }
    printf("Case #%d: ",++iCase);
    if(ans == 1)printf("%d\n",last);
    else if(ans > 1)printf("Bad magician!\n");
    else printf("Volunteer cheated!\n");
}
int main(void){
    iCase = 0;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A1.out","w",stdout);
    int casenum; scanf("%d",&casenum);
    while(casenum--) solve();
    return 0;
}
