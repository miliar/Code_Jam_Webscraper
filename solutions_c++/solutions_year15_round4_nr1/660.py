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
#include <cctype>
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
#define INF 15000000
#define maxn 2000000
#define mod  1000000007LL
#define HASHMOD 3894229
#define Pi acos(-1.0)
#define link fjksldfjaslkdfjas
#define y1 fksjdlf
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

int iCase;

int uu[110], dd[110], ll[110], rr[110];
char puzzle[110][110];
int row, col;
void solve(void) {
    scanf("%d%d", &row, &col);
    for(int i = 0;i < row;i ++) {
        scanf("%s", puzzle[i]);
    }
    int ans = 0;
    rst(uu, -1);
    rst(dd, -1);
    rst(ll, -1);
    rst(rr, -1);
    for(int i = 0;i < row;i ++) {
        for(int j = 0;j < col;j ++) {
            if(puzzle[i][j] == '.') continue;
            if(uu[j] == -1) uu[j] = i;
            dd[j] = MAX(dd[j], i);
            if(ll[i] == -1) ll[i] = j;
            rr[i] = MAX(rr[i], j);
        }
    }
    for(int i = 0;i < row;i ++) {
        for(int j = 0;j < col;j ++) {
            if(puzzle[i][j] == '.') continue;
            if(ll[i] == rr[i] && uu[j] == dd[j]) {
                ans = INF;
                break;
            }
        }
        if(ans == INF) break;
    }
    if(ans == INF) {
        printf("Case #%d: IMPOSSIBLE\n", ++ iCase);
        return;
    }
    for(int i = 0;i < row; i ++) {
        if(ll[i] == -1) continue;
        if(ll[i] == rr[i]) {
            if(puzzle[i][ll[i]] == '<' || puzzle[i][ll[i]] == '>') {
                ans ++;
                if(uu[ll[i]] == i) {
                    puzzle[i][ll[i]] = 'v';
                }else if(dd[ll[i]] == i) {
                    puzzle[i][ll[i]] = '^';
                }else {
                    puzzle[i][ll[i]] = '.';
                }
            }
        }else {
            if(puzzle[i][ll[i]] == '<') {
                ans ++;
                puzzle[i][ll[i]] = '>';
            }
            if(puzzle[i][rr[i]] == '>') {
                ans ++;
                puzzle[i][rr[i]] = '<';
            }
        }
    }
    for(int j = 0;j < col;j ++) {
        if(uu[j] == -1) continue;
        if(dd[j] == uu[j]) {
            if(puzzle[dd[j]][j] == '^' || puzzle[dd[j]][j] == 'v') {
                ans ++;
            }
        }else {
            if(puzzle[uu[j]][j] == '^') {
                ans ++;
                puzzle[uu[j]][j] = 'v';
            }
            if(puzzle[dd[j]][j] == 'v'){
                ans ++;
                puzzle[dd[j]][j] = '^';
            }
        }
    }
    printf("Case #%d: %d\n", ++iCase, ans);
}

int main(void) {
    //freopen("A-large.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    iCase = 0;
    int casenum; scanf("%d", &casenum);
    while(casenum --) solve();
    return 0;
}
