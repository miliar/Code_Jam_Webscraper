//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>   //����ɳ��....������д���ˡ���
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
#define eps 1e-9
#define INF 1500000000
#define maxn 110000
#define mod  1000000007LL
#define HASHMOD 3894229
#define Pi acos(-1.0)
#define link fjksldfjaslkdfjas
#define y1 fksjdlf
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

int iCase;

int n, a[1100];
void solve(void) {
    scanf("%d",&n);
    FOR(i,1,n) scanf("%d",a+i);
    int ans = INF;
    for(int cut = 1; cut <= 1000; cut++) {
        int temp = 0;
        FOR(i,1,n) {
            temp += (a[i] - 1) / cut;
        }
        temp += cut;
        if(temp < ans) ans = temp;
    }
    printf("Case #%d: %d\n",++iCase,ans);
}

int main(void) {
    iCase = 0;
    //freopen("B-large.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int casenum; scanf("%d",&casenum);
    while(casenum--) solve();
}
