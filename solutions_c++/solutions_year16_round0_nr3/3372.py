#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <queue>
#include <stack>
#include <cmath>
#include <vector>
#include <map>

#define ll long long
#define ull unsigned long long
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1

using namespace std;

const int inf = 0x3f3f3f3f;
const int M = 102;

ll a[35];
ll num;
ll n, m;
ll ans[15];

void judge(){
    for(int i = 2; i <= 10; i++){
        ll tmp = 1, tt = i;
        for(int j = 1; j < n; j++){
            tmp += a[j]*tt;
            tt = tt*i;
        }
        ll sq = (ll)sqrt(tmp+0.5);
        int f  = 1;
        for(int j = 2; j <= sq; j++){
            if(tmp%j == 0){
                ans[i] = j;
                f = 0;
                break;
            }
        }
        if(f)
            return;
    }
    num++;
    for(int i = n-1; i >= 0; i--)
        printf("%lld", a[i]);
    for(int i = 2; i <= 10; i++)
        printf(" %lld", ans[i]);
    printf("\n");
}

void dfs(int u){
    if(u == n-2){
        judge();
        return;
    }
    if(num >= m)
        return;
    a[u] = 0;
    dfs(u+1);
    if(num >= m)
        return;
    a[u] = 1;
    dfs(u+1);
}

int main(){

    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
        printf("Case #1:\n");
        num = 0;
        scanf("%lld%lld", &n, &m);
        memset(a, 0, sizeof(a));
        a[0] = 1;
        a[n-1] = 1;
        dfs(1);
    }


    return 0;
}









