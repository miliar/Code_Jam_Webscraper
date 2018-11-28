//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <stack>
#include <map>
#include <vector>
#include <set>
#include <bitset>
#include <string>
#include <queue>
using namespace std;
#define rep(i,l,r) for(i = l; i <= r; i++)
#define red(i,l,r) for(i=(l);i>=(r);i--)
#define u_long unsigned long long
#define fff(i, u) for(i = head[u]; i != -1; i = nxt[i])
#define fin() freopen("in.txt", "r", stdin)
#define fout() freopen("out.txt", "w", stdout)
#define clr(vis, a) memset(vis, a, sizeof(vis))
#define LL long long
#define ls id << 1
#define rs id << 1 | 1
#define lson id << 1, l, mid
#define rson id << 1 | 1, mid + 1, r
#define mid ( (l + r) >> 1 )
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define X first
#define Y second
#define eps 1e-9
#define pi acos(-1)
const int maxn = 2e3 + 10;
const int maxm = maxn * 4 + 10;
const int inf = 1e9;
const LL mod = 1e8+7;
int getint() {
    char c;
    while((c = getchar()) && !(c >= '0' && c <= '9') && c != '-');
    int ret = c - '0', sgn = 0;
    if(c == '-') sgn = 1, ret = 0;
    while((c = getchar()) && c >= '0' && c <= '9')
        ret = ret * 10 + c - '0';
    if(sgn) ret = -ret;
    return ret;
}
char s[110];
int main(){
    fin();
    fout();
    int T = getint();
    for(int ka = 1; ka <= T; ka ++){
        scanf("%s", s);
        int len = strlen(s);
        int cnt = 1;
        for(int i = 1; i < len; i ++){
            if(s[i] == s[i-1]) continue;
            else cnt ++;
        }
        if(s[len-1] == '+') cnt--;
        printf("Case #%d: %d\n",ka, cnt);
    }
    return 0;
}



