#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;
typedef long long LL;
#define N 105
#define M 100005
int ca;
int n , m , a[N] , t[N];
char s[N][N];
int sum , ans;

int u[M][26];
int cnt;

void dfs(int k) {
    if (k == n) {
        cnt = m;
        for (int i = 1 ; i <= m ; ++ i) {
            if (!t[i]) return;
            memset(u[i] , 0 , sizeof(u[m]));
        }
        for (int i = 0 ; i < n ; ++ i) {
            int x = a[i];
            for (int j = 0 ; s[i][j] ; ++ j) {
                int c = s[i][j] - 'A';
                if (!u[x][c]) {
                    u[x][c] = ++ cnt;
                    memset(u[cnt] , 0 , sizeof(u[cnt]));
                }
                x = u[x][c];
            }
        }
        if (cnt > ans)
            ans = cnt , sum = 1;
        else if (cnt == ans)
            ++ sum;
        return;
    }
    for (int i = 1 ; i <= m ; ++ i) {
        a[k] = i , ++ t[i];
        dfs(k + 1);
        -- t[i];
    }
}

void work() {
    printf("Case #%d: " , ++ ca);
    ans = sum = 0;
    scanf("%d%d",&n,&m);
    for (int i = 0 ; i < n ; ++ i) {
        scanf("%s" , s[i]);
    }
    dfs(0);
    printf("%d %d\n" , ans , sum);
}

int main()
{
    freopen("~input.txt" , "r" , stdin);
    freopen("~output.txt" , "w" , stdout);
    int _; scanf("%d",&_); while (_ --)
        work();
    return 0;
}
