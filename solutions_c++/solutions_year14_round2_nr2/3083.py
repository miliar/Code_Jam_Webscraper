#include <cstdio>




int get_result(unsigned int a, unsigned int b, unsigned int k)
{
    int sum = 0;

    for(unsigned int i = 0; i < a; i++)
        for(unsigned int j = 0; j < b; j++)
            if ((i & j) < k)
                sum++;
    return sum;
}

int main()
{
    int sum = 0;
    int T = 0;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        unsigned int a,b,k;
        scanf("%u%u%u", &a, &b, &k);
        sum = get_result(a, b, k);
        printf("Case #%d: %d\n", t, sum);
    }
    return sum;
}
