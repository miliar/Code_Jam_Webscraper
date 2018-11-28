#include<stdio.h>

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
    freopen("out.txt", "w", stdout);
#endif
    long long int root[] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002,
        20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011,
        1110111, 1111111, 2000002, 2001002, 10000001};

    long long int square[40];

    for(int i = 0; i < 40; i++)
        square[i] = root[i] * root[i];

    int c, d;
    long long int t, a, b;
    scanf("%lld", &t);

    for(int i = 1; i <= t; i++)
    {
        scanf("%lld %lld", &a, &b);
        c = d = -1;
        for(int j = 0; j < 40; j++)
        {
            if(square[j] >= a)
            {
                c = j;
                break;
            }
        }
        for(int j = 0; j < 40; j++)
        {
            if(square[j] > b)
            {
                d = j;
                break;
            }
        }

        printf("Case #%d: ", i);
        if(d-c > 0)
            printf("%d\n", d-c);
        else
            printf("0\n");

    }
    return 0;

}
