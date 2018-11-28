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
#define eps 1e-9
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

map<string, int> bst;
map<string, int>::iterator it;
int color[5100];
int muban[5100];
vector<int> e[110];
vector<int>::iterator oh;
vector<int> pool;
char s[25][15000];
int ans = INF, n, tot;
void exec(int ind) {
    int len = strlen(s[ind]);
    string temp;
    bool have = false;
    for(int i = 0;i < len;i ++) {
        if(s[ind][i] == ' ' || s[ind][i] == '\n') {
            if(have == true) {
                if(bst[temp] == 0) {
                    bst[temp] = ++tot;
                }
                e[ind].push_back(bst[temp]);
                temp.clear();
            }
            have = false;
        }else {
            temp.push_back(s[ind][i]);
            have = true;
        }
    }
    if(have == true) {
        if(bst[temp] == 0) {
            bst[temp] = ++tot;
        }
        e[ind].push_back(bst[temp]);
        temp.clear();
    }
}
void solve(void) {
    ans = INF;
    bst.clear();
    scanf("%d\n", &n);
    tot = 0;
    rst(muban, 0);
    for(int i = 0;i < n;i ++) {
        e[i].clear();
        gets(s[i]);
        exec(i);
    }
    int cap = (1 << n);
    int large = 0;
    int ss = e[0].size();
        for(int j = 0;j < ss;j ++) {
            muban[e[0][j]] = 1;
        }
        ss = e[1].size();
        for(int j = 0;j < ss;j ++) {
            int tt = e[1][j];
            if(muban[tt] == 1) large ++;
            muban[tt] |= 2;
    }
    for(int i = 0;i < cap;i ++) {
        if((i & 1)) continue;
        if((i & 2) == 0) continue;
        memcpy(color, muban, sizeof(muban));
        int temp = 0;
        for(int j = 2;j < n;j ++) {
            int co;
            if(i & (1 << j)) {
                co = 2;
            }else {
                co = 1;
            }
            ss = e[j].size();
            for(int k = 0;k < ss;k ++) {
                int tt = e[j][k];
                if(color[tt] + co == 3) temp ++;
                color[tt] |= co;
            }
        }
        if(temp + large < ans) {
            ans = temp + large;
        }
    }
    printf("Case #%d: %d\n", ++iCase, ans);
}

int main(void) {
    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    iCase = 0;
    int casenum; scanf("%d", &casenum);
    while(casenum --) solve();
    return 0;
}
