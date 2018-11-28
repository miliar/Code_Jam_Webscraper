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
//#define abs(x) ((x)>0?(x):(-(x)))
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
#define maxn 110000
#define mod 1000000007LL
#define Pi acos(-1.0)
#define link fjksldfjaslkdfjas
using namespace std;
typedef long long LL;
double C,F,X;
int iCase;
void solve(void){
    double ans = 0.0;
    double v = 2.0;
    scanf("%lf%lf%lf",&C,&F,&X);
    while(X * F > C * (v + F)){
        ans += C / v;
        v += F;
    }
    ans += X / v;
    printf("Case #%d: ",++iCase);
    printf("%.7lf\n",ans);
}
int main(void){
    iCase = 0;
    //freopen("B-large.in","r",stdin);
    //freopen("Blarge.out","w",stdout);
    int casenum; scanf("%d",&casenum);
    while(casenum--) solve();
}
