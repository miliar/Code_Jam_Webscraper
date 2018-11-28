#include <vector>
#include <iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<queue>
#include <set>
#include<map>
#include<string>
#include<stdexcept>
#include<errno.h>

using namespace std;
template <class T> void show(T a, int n) { for (int i = 0; i < n; ++i) cout << a[i] << ' '; cout << endl; }
template <class T> void show(T a, int r, int l) { for (int i = 0; i < r; ++i) show(a[i], l); cout << endl; }
#define max(a, b) (a > b?a:b)
#define min(a, b) (a < b?a:b)

#define ms(a, v)    memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
#define pii pair<int, int>

typedef long long LL;

const int N = 128 * 2;
const int M = 5000;
const int oo = 10000 * 10000 * 10;

int n, m;
int g[111][111];

bool check(int ii, int jj)
{
    int i,j;
    for (j = 0;j < m;++j)
        if (g[ii][j] > g[ii][jj])
            break;
    if (j == m)
        return true;

    for (i = 0; i < n;++i)
        if (g[i][jj] > g[ii][jj])
            break;
    if (i == n)
        return true;

    return false;
}

bool solve()
{
    int i, j, k;
    vector<int> e[111];
    for (int i = 0; i < n;++i)
    {
        for (int j = 0;j < m;++j)
            if (!check(i,j))
                return false;
    }
    return true;
}

int main()
{
        freopen("in", "r", stdin);
        freopen("out1","w",stdout); 
    int i, j, cas = 0;
    scanf("%d", &cas);
    for (int cc = 0; cc < cas;++cc)
    {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n;++i)
            for (int j = 0;j < m;++j)
                scanf("%d",  &g[i][j]);
        printf("Case #%d: ", cc + 1);

        if (solve())
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}

