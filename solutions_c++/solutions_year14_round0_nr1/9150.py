#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
using namespace std;


typedef long long LL;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}
const int N = 20;
int vis[N];
int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int t, cas = 1, i, j, k;
    scanf("%d", &t);
    while(t--)
    {
        memset(vis, 0, sizeof(vis));
        for(i = 1; i <= 2; i++)
        {
            int row, val;
            scanf("%d", &row);
            for(j = 1; j <= 4; j++)
                for(k = 1; k <= 4; k++)
                {
                    scanf("%d", &val);
                    if(j == row)
                        vis[val]++;
                }
        }
        int ans = -1, cnt = 0;
        for(i = 1; i <= 16; i++)
            if(vis[i] == 2)
            {
                ans = i;
                cnt++;
            }
        printf("Case #%d: ", cas++);
        if(cnt == 1)
            printf("%d\n", ans);
        else if(cnt == 0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
    return 0;
}
