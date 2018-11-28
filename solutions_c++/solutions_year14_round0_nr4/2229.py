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
int iCase;
int n;
double a[maxn] , b[maxn];
void solve(void){
    scanf("%d",&n);
    FOR(i,1,n) scanf("%lf",a+i);
    FOR(i,1,n) scanf("%lf",b+i);
    sort(a+1,a+n+1);
    sort(b+1,b+n+1);
    //FOR(i,1,n) printf("%.3lf  ",a[i]);printf("\n");
    //FOR(i,1,n) printf("%.3lf  ",b[i]);printf("\n");
    int aa = 0 , bb = 0;
    int now = 1;
    FOR(i,1,n){
        if(a[i] > b[now]){
            aa++;
            now++;
        }
    }
    now = 1;
    FOR(i,1,n){
        if(b[i] > a[now]){
            bb++;
            now++;
        }
    }
    printf("Case #%d: %d %d\n",++iCase,aa,n - bb);
}
int main(void){
    iCase = 0;
    //freopen("D-large.in","r",stdin);
    //freopen("Dlarge.out","w",stdout);
    int casenum; scanf("%d",&casenum);
    while(casenum--) solve();
}
