#include <bits/stdc++.h>
using namespace std;

int T;
long long N;
bool vis[10];
bool check()
{
    for (int i = 0; i < 10; ++i)
        if (!vis[i])
            return 0;
    return 1;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int t = 1; t <= T; ++t)
    {
        memset(vis,0,sizeof(vis));
        scanf("%lld",&N);
        if (!N)
            printf("Case #%d: INSOMNIA\n",t);
        else
        {
            long long ct = 1;
            while (!check())
            {
                long long cur = N*ct;
                while (cur)
                {
                    vis[cur%10] = 1;
                    cur /= 10;
                }
                ct++;
            }
            printf("Case #%d: %lld\n",t,(ct-1)*N);
        }
    }
	return 0;
}
