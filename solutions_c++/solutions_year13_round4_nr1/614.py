#include <cstdio>
#include <cstring>
using namespace std;
const int maxn = 200;
int n,m;
int enter[maxn] , leave[maxn] , cards[maxn];
const int mode = 1000002013;
void solve(int id)
{
    int ans = 0;
    const int maxf = 21;
    memset(enter,0,sizeof(enter));
    memset(leave,0,sizeof(leave));
    memset(cards,0,sizeof(cards));
    scanf("%d%d",&n,&m);
    for (int i = 1; i <= m ; ++i)
    {
        int x,y,num;
        scanf("%d%d%d" ,&x,&y,&num );
        enter[x] += num;
        leave[x] += num;
        ans += num * (y-x) * (maxf - y + x) / 2;
        ans %= mode;
    }
    for (int i = 1; i <=n ; ++i)
    {
        cards[i] += enter[i];
        int &cur = leave[i];
        for (int j = i ; cur ; --j)
        {
            int delta = min(cards[j],cur);
            ans -= delta *  (i - j) * (maxf - i + j) / 2;
            ans %= mode;
            cur -= delta;
            cards[k] -= delta;
        }
    }
    printf("Case #%d: %d\n",id,ans);
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i = 1; i <= t; ++i)
        solve(i);
    return 0;
}
