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
int ca;
int n , m , K;
int ans[N];

void work()
{
    printf("Case #%d: " , ++ca);
    scanf("%d%d%d",&n,&m,&K);
    if (n > m) swap(n , m);
    int i , j;
    for (i = 0 ; i <= n * m ; ++ i) {
        ans[i] = i;
    }
    if (n == 3) {
        for (i = 1 ; i <= m - 2 ; ++ i) {
            ans[3 * i + 2] = 2 * i + 2;
        }
    }
    if (n == 4) {
        ans[5] = 4;
        ans[8] = 6;
        ans[10] = 7;
        ans[12] = 8;
        if (m == 5) {
            ans[11] = 8;
            ans[16] = 10;
            ans[14] = 9;
            ans[13] = 9;
        }
    }
    for (i = 1 ; i <= n * m ; ++ i)
        for (j = i + 1 ; j <= n * m ; ++ j)
            ans[j] = min(ans[i] + j - i , ans[j]);
    printf("%d\n" , ans[K]);
}

int main()
{
    freopen("1.txt" , "r" , stdin);
    freopen("2.txt" , "w" , stdout);

    int _; scanf("%d", &_); while (_ --)
        work();
    return 0;
}
