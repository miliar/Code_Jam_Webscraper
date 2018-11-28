#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <queue>
#include <ctime>
#include <vector>
#include <algorithm>
#define ll long long
#define L(rt) (rt<<1)
#define R(rt)  (rt<<1|1)
using namespace std;

const int INF = 1e8;
const int maxn = 20;

int n;
double nao[maxn], ken[maxn];
bool vis[maxn];
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf("%lf", &nao[i]);
        for(int i = 0; i < n; i++)
            scanf("%lf", &ken[i]);
        int ans1 = 0, ans2 = 0;
        sort(nao, nao + n);
        sort(ken, ken + n);
        memset(vis, false, sizeof(vis));
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                if(nao[j] > ken[i] && !vis[j])
                {
                    vis[j] = true;
                    ans1++;
                    break;
                }
        memset(vis, false, sizeof(vis));
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                if(ken[j] > nao[i] && !vis[j])
                {
                    vis[j] = true;
                    ans2++;
                    break;
                }
        printf("Case #%d: ", ++ca);
        printf("%d %d\n", ans1, n - ans2);
    }
    return 0;
}
