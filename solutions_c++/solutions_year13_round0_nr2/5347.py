#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <ctime>
#include <cstdlib>
#define Hash1 (LL)11111
#define Hash2 (LL)13337
#define lson l,m,rt << 1
#define rson m + 1,r,rt << 1 | 1
#define eps 1e-8
#define ft first
#define sd second
#define zero(x) (((x)>0?(x):-(x))<eps)
#define LL long long
#define Test puts("END")
#define pi acos(-1.0)
#pragma comment(linker, "/STACK:32000000")
using namespace std;
const int MOD = 1000000007;
const int INF = 1000000000;
const int N = 12;
const int M = 1000;

int h[N][N],n,m,rec[N][N];
bool solve();

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int t = 1;t <= cas;t ++){
        scanf("%d%d",&n,&m);
        for(int i = 0;i < n;i ++)
            for(int j = 0;j < m;j ++){
                scanf("%d",&h[i][j]);
                rec[i][j] = h[i][j];
            }
        bool ret = solve();
        printf("Case #%d: ",t);
        if(ret) puts("YES");
        else puts("NO");
    }
    return 0;
}

bool solve()
{
    for(int i = 0;i < n;i ++){
        int mx = 0;
        for(int j = 0;j < m;j ++)
            mx = max(mx,h[i][j]);
        for(int j = 0;j < m;j ++)
            h[i][j] = mx;
    }
    /*puts("__________________");
    for(int i = 0;i < n;i ++)
        for(int j = 0;j < m;j ++)
            printf("%d%c",h[i][j],j == m - 1 ? '\n' : ' ');
    puts("__________________");*/
    for(int j = 0;j < m;j ++){
        int mn = INF;
        for(int i = 0;i < n;i ++){
            if(h[i][j] != rec[i][j]) mn = rec[i][j];
        }
        if(mn == INF) continue;
        for(int i = 0;i < n;i ++)
            h[i][j] = mn;
    }
    for(int i = 0;i < n;i ++)
        for(int j = 0;j < m;j ++)
            if(h[i][j] != rec[i][j]) return false;
    return true;
}