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
map<int,int> bst;
map<int,int>::iterator it;
int iCase;
int n,m;
void solve(void){
    bst.clear();
    scanf("%d%d",&n,&m);
    FOR(i,1,n){
        int tt; scanf("%d",&tt);
        if(bst[tt] == 0){
            bst[tt] = 1;
        }else{
            bst[tt]++;
        }
    }
    int ans = 0;
    while(n > 0){
        ans++;
        it = bst.begin();
        //printf("itbegin is %d   %d\n",it->first,it->second);
        int kk = it->first;
        if(it->second == 1){
            bst.erase(it);
        }else{
            (it->second)--;
        }
        n--;
        if(n == 0)break;
        //printf("m-kk is %d\n",m-kk);
        it = bst.upper_bound(m - kk);
        //printf("find is %d num is %d\n",it->first,it->second);
        if(it == bst.begin())continue;
        it--;
        if(it->second == 1){
            bst.erase(it);
        }else{
            (it->second)--;
        }
        n--;
    }
    printf("Case #%d: %d\n",++iCase,ans);
}
int main(void){
    //freopen("A-large.in" , "r" , stdin);
    //freopen("out.out" , "w" , stdout);
    iCase = 0;
    int casenum; scanf("%d",&casenum);
    while(casenum--) solve();
    return 0;
}
