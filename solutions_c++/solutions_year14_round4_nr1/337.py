#pragma  comment(linker, "/STACK:36777216")
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <iomanip>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define  lc(x) (x << 1)
#define  rc(x) (lc(x) + 1)
#define  lowbit(x) (x & (-x))
#define  PI    (acos(-1))
#define  lowbit(x) (x & (-x))
#define  EPS   1e-10
#define  MAXN  500055
#define  MAXM  2005
#define  LL    long long
#define  DB    double
#define  ULL   unsigned long long
#define  INF   0x7fffffff
#define  pb    push_back
#define  mp    make_pair
#define  MOD   1000000007

using namespace std;

int t, n, x, cas;

bool cmp(int a, int b){return a > b;}

bool flag[10005];
int a[10005];

int main(){
    freopen("A.in", "r", stdin);
    //freopen("A-small-attempt1.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> t;
    while(t --){
        scanf("%d", &n);
        scanf("%d", &x);
        memset(flag, 0, sizeof(flag));
        for(int i = 1; i <= n; i ++) scanf("%d", &a[i]);
        sort(a + 1, a + 1 + n, cmp);
        int ans = 0;
        for(int i = 1; i <= n; i ++){
            if(flag[i] == 0){
                ans ++;
                flag[i] = true;
                for(int j = i + 1; j <= n; j ++)
                if(!flag[j] && a[i] + a[j] <= x){
                    flag[j] = 1; break;
                }
            }
        }
        printf("Case #%d: %d\n", ++ cas, ans);
    }
}
