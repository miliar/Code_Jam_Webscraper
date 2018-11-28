#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
int T,R,N,M,K;
int v[10];

int cal(int x)
{
    int d = 0,tmp;
    int md = 0;
    for (int j = 1; j <= K; ++j)
    {
        d = 0;
        tmp = v[j];
        while(tmp % x == 0)
        {
            tmp/=x;
            d++;
        }
        md = max(md,d);
    }
    return md;
}
int main()
{
    freopen("C-small-1-attempt2.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&T);
    for (int ca = 1; ca <= T; ++ca)
    {
        scanf("%d%d%d%d",&R,&N,&M,&K);
        printf("Case #%d:\n",ca);
        for (int i = 1; i <= R; ++i)
        {
            for (int j = 1; j <= K; ++j)
                scanf("%d",&v[j]);
            if (M == 2)
            {
                for (int j = 1; j <= 3; ++j)
                    printf("2");
            }else if (M== 3)
            {
                int d3 = cal(3);
                for (int j = 1; j <= d3;++j)
                    printf("3");
                for (int j = 1; d3 + j <= 3; ++j)
                    printf("2");
            }else if (M== 4)
            {
                int d2 = cal(2);
                int d3 = cal(3);
                int d4 = cal(4);
                if (d3 + d4 == N)
                {
                    for (int j = 1; j <= d3;++j)
                        printf("3");
                    for (int j = 1; j <= d4;++j)
                        printf("4");
                }else if (d2 + d3 <= N)
                {
                    for (int j = 1; j <= d3;++j)
                        printf("3");
                    for (int j = 1; d3 + j <= N;++j)
                        printf("2");
                }else
                {
                    for (int j = 1; j <= d3;++j)
                        printf("3");
                    for (int j = 1; j <= d4 && d3 + j <= N;++j)
                        printf("4");
                    for (int j = 1; d3 + d4 + j <= N;++j)
                        printf("2");
                }
            }else
            {
                int d2 = cal(2);
                int d4 = cal(4);
                int d3 = cal(3);
                int d5 = cal(5);
                for (int j = 1; j <= d3;++j)
                    printf("3");
                for (int j = 1; j <= d5;++j)
                    printf("5");
                if (d3 + d5 < N)
                {
                    if (d3 + d5 + d4 == N)
                    {
                        for (int j = 1; j <= d4;++j)
                            printf("4");
                    }else if (d3 + d5 + d2 == N)
                    {
                        for (int j = 1; j <= d2;++j)
                            printf("2");
                    }else
                    {
                        for (int j = 1; j <= d4; ++j)
                            printf("4");
                        for (int j = 1; d3 +d4+ d5 + j <= N;++j)
                            printf("2");
                    }
                }
            }
            printf("\n");
        }
    }
    return 0;
}
