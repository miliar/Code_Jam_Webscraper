//
// Created by Acka on 4/9/16.
//

#include <stdio.h>

int main()
{
    freopen("/Users/acka/ClionProjects/ProblemSolving/D-small-attempt0.in", "r", stdin);
    freopen("/Users/acka/ClionProjects/ProblemSolving/D-small-attempt0.out", "w", stdout);

    int tc, st = 1; for(scanf("%d", &tc); tc--;){
        int K, C, S; scanf("%d %d %d", &K, &C, &S);

        printf("Case #%d:", st++);
        for(int i = 1; i <= K; i++)
            printf(" %d", i);
        printf("\n");
    }
    return 0;
}