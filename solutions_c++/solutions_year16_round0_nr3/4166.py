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
int judge(LL x){
    int m = sqrt(x + 0.5);
    for(int i = 2; i <= m; i ++){
        if(x % i == 0){
            return i;
        }
    }
    return 0;
}
int temp[33];
LL xpow(LL x, LL k){
    LL ret = 1;
    while(k){
        if(k & 1) ret = ret * x;
        x = x * x;
        k >>= 1;
    }
    return ret;
}
LL d[12];
int main(){
    fin();
    fout();
    int T = getint();
    for(int ka = 1; ka <= T; ka ++){
        int n = getint(), m = getint();
        int cnt = 0;
        printf("Case #1:\n");
        for(int s = 1; s < (1 << n); s ++){
            if(cnt == m) break;
            if((s & 1) == 0) continue;
            if((s & (1 << (n - 1))) == 0) continue;
            for(int i = 0; i < n; i ++){
                if((s & (1 << i))) temp[i] = 1;
                else temp[i] = 0;
            }
            int flag = 1;
            for(int i = 2; i <= 10; i ++){
                LL ret = 0;
                for(int j = 0; j < n; j ++){
                    if(temp[j]) ret = ret + xpow(i, j);
                }
                d[i] = judge(ret);
                if(d[i] == 0){
                    flag = 0;
                    break;
                }
            }
            if(flag){
                cnt ++;
                for(int i = 0; i < n; i ++) cout << temp[n - 1 - i];
                printf(" ");
                for(int i = 2; i <= 10; i ++){
                    if(i > 2) cout << " ";
                    cout << d[i];
                }
                puts("");
            }
        }
    }
    return 0;
}



