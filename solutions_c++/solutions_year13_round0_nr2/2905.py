#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<utility>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<iomanip>
#include<queue>
#include<iterator>
using namespace std;

#define LL long long
#define MAXN 100 + 10
int n, m;
int a[MAXN][MAXN];
int b[MAXN][MAXN];
int mxd[MAXN], rmxd[MAXN];
bool solve()
{
    for(int i = 0; i < n; ++i) for(int j = 0; j < m; ++j) b[i][j] = 100;
    //for each row
    for(int i = 0; i < n; ++i)
    {
        int maxn = 0;
        for(int j = 0; j < m; ++j) maxn = max(a[i][j], maxn);
        for(int j = 0; j < m; ++j) b[i][j] = b[i][j] > maxn ? maxn : b[i][j];
    }
    //for each col
    for(int i = 0; i < m; ++i)
    {
        int maxn = 0;
        for(int j = 0; j < n; ++j) maxn = max(a[j][i], maxn);
        for(int j = 0; j < n; ++j) b[j][i] = b[j][i] > maxn ? maxn : b[j][i];
    }
  /*  //for the first row
    memset(mxd, 0, sizeof(mxd));
    memset(rmxd, 0, sizeof(rmxd));
    mxd[0] = a[0][0]; rmxd[m - 1] = a[0][m - 1];
    for(int i = 1, j = m - 2; i < m; ++i, --j)
    {
        mxd[i] = max(mxd[i - 1], a[0][i]);
        rmxd[j] = max(rmxd[j + 1], a[0][j]);
    }
    for(int i = 0; i < m; ++i)
    {
        for(int j = 0; j <= i; ++j) b[0][j] = b[0][j] > mxd[j] ? mxd[j] : b[0][j];
        for(int j = i + 1; j < m; ++j) b[0][j] = b[0][j] > rmxd[j] ? rmxd[j] : b[0][j];
    }
    //for the last row
    memset(mxd, 0, sizeof(mxd));
    memset(rmxd, 0, sizeof(rmxd));
    mxd[0] = a[n - 1][0]; rmxd[m - 1] = a[n - 1][m - 1];
    for(int i = 1, j = m - 2; i < m; ++i, --j)
    {
        mxd[i] = max(mxd[i - 1], a[n - 1][i]);
        rmxd[j] = max(rmxd[j + 1], a[n - 1][j]);
    }
    for(int i = 0; i < m; ++i)
    {
        for(int j = 0; j <= i; ++j) b[n - 1][j] = b[n - 1][j] > mxd[j] ? mxd[j] : b[n - 1][j];
        for(int j = i + 1; j < m; ++j) b[n - 1][j] = b[n - 1][j] > rmxd[j] ? rmxd[j] : b[n - 1][j];
    }
    //for  the first col
    memset(mxd, 0, sizeof(mxd));
    memset(rmxd, 0, sizeof(rmxd));
    mxd[0] = a[0][0]; rmxd[n - 1] = a[n - 1][0];
    for(int i = 1, j = n - 2; i < n; ++i, --j)
    {
        mxd[i] = max(mxd[i - 1], a[i][0]);
        rmxd[j] = max(rmxd[j + 1], a[j][0]);
    }
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j <= i; ++j) b[j][0] = b[j][0] > mxd[j] ? mxd[j] : b[j][0];
        for(int j = i + 1; j < n; ++j) b[j][0] = b[j][0] > rmxd[j] ? rmxd[j] : b[j][0];
    }
    //for the last col
    memset(mxd, 0, sizeof(mxd));
    memset(rmxd, 0, sizeof(rmxd));
    mxd[0] = a[0][m - 1]; rmxd[n - 1] = a[n - 1][m - 1];
    for(int i = 1, j = n - 2; i < n; ++i, --j)
    {
        mxd[i] = max(mxd[i - 1], a[i][m - 1]);
        rmxd[j] = max(rmxd[j + 1], a[j][m - 1]);
    }
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j <= i; ++j) b[j][m - 1] = b[j][m - 1] > mxd[j] ? mxd[j] : b[j][m - 1];
        for(int j = i + 1; j < n; ++j) b[j][m - 1] = b[j][m - 1] > rmxd[j] ? rmxd[j] : b[j][m - 1];
    }*/
    //judge
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            if(a[i][j] != b[i][j]) return false;
        }
    }
    return true;
}
int main(int argv, char **args)
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase = 1; kase <= T; ++kase)
    {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < m; ++j)
            {
                scanf("%d", &a[i][j]);
            }
        }
        if(solve()) printf("Case #%d: %s\n", kase, "YES");
        else printf("Case #%d: %s\n", kase, "NO");
    }
    return 0;
}
