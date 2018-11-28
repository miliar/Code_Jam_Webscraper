#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int T;
int N, L;

char G[101][51], B[51];

int main()
{
    freopen("D_small_in.txt", "r", stdin);
    freopen("D_small_out.txt", "w", stdout);

    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%d %d", &N, &L);

        for(int Ni = 0; Ni < N; Ni++)
            scanf("%s", G[Ni]);

        scanf("%s", B);

        printf("Case #%d: ", Ti);

        for(int Ni = 0; Ni < N; Ni++)
            if( !strcmp(G[Ni], B) )
            {
                puts("IMPOSSIBLE");
                goto flag;
            }

        if( L == 1 )
        {
            printf("0? 0\n");
            goto flag;
        }

        for(int Li = 1; Li < L; Li++)
            putchar('?');
        putchar(' ');

        for(int Li = 0; Li < L; Li++)
            printf("10");
        printf("?");
        for(int Li = 0; Li < L; Li++)
            printf("1");
        putchar('\n');

        flag:;
    }
}
