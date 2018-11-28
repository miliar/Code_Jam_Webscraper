#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

typedef long long LL;

bool vis[11];

bool Judge(LL n)
{
    while(n)
    {
        vis[n%10] = true;

        n/= 10;
    }

    int ans = 0;

    for(int i = 0;i<=9;i++)
    {
        if(vis[i])
        {
            ans++;
        }
    }

    return ans ==10;

}

LL n;

int main()
{
    int T,z = 1;

    scanf("%d",&T);

    while(T--)
    {
        scanf("%lld",&n);

        memset(vis,false,sizeof(vis));

        printf("Case #%d: ",z++);

        if(!n) printf("INSOMNIA\n");

        else
        {
            LL m = n;
            while(!Judge(m))
            {
                m+=n;
            }

            printf("%lld\n",m);
        }


    }
    return 0;
}
