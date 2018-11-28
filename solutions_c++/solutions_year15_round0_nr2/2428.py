#include <cstdio>
using namespace std;
int n;
int a[1010];
void solve(int t)
{
    scanf("%d",&n);
    for(int i = 0; i < n; i++)
        scanf("%d",&a[i]);
    int sol = 1000;
    for(int mx = 1; mx <= 1000; mx++)
    {
        int tmp = mx;
        for(int i = 0; i < n; i++)
        {
            if (a[i] <= mx)
                continue;
            tmp += a[i]/mx-(a[i]%mx==0);
        }
        if (sol > tmp)
            sol = tmp;
    }
    printf("Case #%d: %d\n",t,sol);
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1; i <= t; i++)
        solve(i);
    return 0;
}
