#include<cstdio>

int main()
{
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; ++i)
    {
        int K, C, S;
        scanf("%d", &K);
        scanf("%d", &C);
        scanf("%d", &S);
        printf("Case #%d:", i+1);
        for(int j=1; j<=K; ++j) printf(" %d", j);
        printf("\n");
    }
    return 0;
}
