#include <iostream>
#include <cstdio>

using namespace std;

bool use[10];

void add(int x)
{
    while(x)
    {
        use[x%10] = true;
        x /= 10;
    }
}

int main()
{
    freopen("A_large.in", "r", stdin);
    freopen("A_large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        int N;
        scanf("%d", &N);

        printf("Case #%d: ", Ti);

        if( N == 0 )
        {
            puts("INSOMNIA");
            continue;
        }

        for(int i = 0; i <= 9; i++) use[i] = false;

        int num = 0;
        while(1)
        {
            num += N;
            add(num);

            bool OK = true;
            for(int i = 0; i <= 9; i++)
                OK &= use[i];

            if( OK )
            {
                printf("%d\n", num);
                break;
            }
        }

    }
}
