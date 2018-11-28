/*
  Author : Enjoy
  Method : 二分图匹配
         dfs(x, c)对x染色c（二分图染色）
         find(x, fa)找x（前驱为fa）的增广路。
         f[]染色数组，ne[]增广路前驱数组，di[],bj[],di[]表示边。
         n,bs表示点数边数。 
*/
#include<iostream>
#include<iomanip>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
#define maxn 500 + 10
#define maxm 2000000 + 10

int a[100000];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int ts, ks, n, m, i, j;
    cin >> ts;
    for (ks = 0; ks < ts; ks++){
        cin >> n >> m;
        for (i = 0; i < n; i++) cin >> a[i];
        sort(a, a + n);
        j = 0;
        for (i = n - 1; i >= j; i--)
            if (a[i] + a[j] <= m) j++;
        printf("Case #%d: %d\n", ks + 1, n - 1 - i);
    }
    return 0;
}
