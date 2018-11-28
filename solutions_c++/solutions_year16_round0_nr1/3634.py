#include <bits/stdc++.h>

using namespace std;

int ap[12],K;

void descomp(long long x)
{
    while(x)
    {
        ap[x%10]++;
        x/=10;
    }
}

bool check()
{
    for(int i = 0; i <= 9; ++i)
        if(ap[i] == 0)
            return false;
    return true;
}

void go(int tt)
{
    int step = 0;
    long long aux = K;
    while(1)
    {
        ++step;
        descomp(aux);
        if(check() == true)
        {
            ///if(step > 53)
            {
                ///printf("%d\n",step);
                printf("Case #%d: %lld\n",tt,aux);

            }
            return;
        }
        if(step > 10000)
            break;
        aux += 1LL*K;

    }
    printf("Case #%d: INSOMNIA\n",tt);
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;

    scanf("%d",&T);
    for(int i = 1; i <= T; ++i)
    {
        scanf("%d",&K);
        if(K == 0)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        memset(ap,0,sizeof(ap));
        go(i);
    }
    /**
    srand(time(0));
    while(1)
    {
        while(K == 0)
            K = rand() % 200;
        memset(ap,0,sizeof(ap));
        go(1);
        K = 0;
    }
    */
    return 0;
}
