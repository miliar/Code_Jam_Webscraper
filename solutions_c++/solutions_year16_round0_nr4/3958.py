#include <iostream>
#include <stdio.h>
int main()
{
    int T;
    int K,C,S;
    FILE *file = fopen("4.out", "w");
    scanf("%d",&T);getchar();
    for (int k = 0; k < T;++k)
    {
        scanf("%d %d %d", &K, &C, &S);
        getchar();
        fprintf(file, "Case #%d: ",k+1);
        fprintf(file, "1");
        for (int i = 2; i <= K; ++i)
        {
            fprintf(file, " %d", i);
        }
        fprintf(file, "\n");
    }
    fclose(file);
    return 0;
}
