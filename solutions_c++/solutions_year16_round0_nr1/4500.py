#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
typedef long long ll;
bool vis[10];
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    cin >> T;
    for(int tt = 1; tt <= T; tt++)
    {
        ll a, b;
        scanf("%lld", &a);
        b = a;
        ll c = b * 1000000;
        memset(vis, false, sizeof(vis));
        bool ans = true;
        if(a == 0)
            ans = false;
        else
        {
            while(b <= c)
            {
                ll cur = b;
                while(cur)
                {
                    vis[cur % 10] = true;
                    cur /= 10;
                }
                bool ok = true;
                for(int i = 0; i < 10; i++)
                    if(!vis[i])
                        ok = false;
                if(ok)
                    break;
                b += a;
            }
        }
        if(ans)
            printf("Case #%d: %d\n", tt, b);
        else
            printf("Case #%d: INSOMNIA\n", tt);
    }
}
