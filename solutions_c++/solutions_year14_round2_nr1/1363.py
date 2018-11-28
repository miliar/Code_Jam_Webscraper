#include<stdio.h>
#include<string.h>
#define L 110

int abs(int n)
{
    return n < 0? -n : n;
}

int main()
{

    int t, n, x, y;
    char s[L], can[L], temp_can[L];
    int i, j, k, lcan, rep[L][L], possible, p, sum;
    scanf("%d", &t);
    for (x = 1; x <= t; x++) {
        scanf("%d", &n);
        for (i = 0; i < n; i++)
            for (j = 0; j < L; j++)
                rep[i][j] = 0;

        scanf("%s", s);
        can[0] = s[0];
        lcan = 0;
        for (j = 0; s[j]; j++) {
            if (can[lcan] != s[j])
                can[++lcan] = s[j];
            rep[0][lcan]++;
        }
        can[++lcan] = 0;

        possible = 1;
        for (i = 1; i < n; i++) {
            scanf("%s", s);
            temp_can[0] = s[0];
            k = 0;
            for (j = 0; s[j]; j++) {
                if(temp_can[k] != s[j])
                    temp_can[++k] = s[j];
                rep[i][k]++;
            }
            temp_can[++k] = 0;
            if (strcmp(can, temp_can) != 0) possible = 0;
        }

        if (possible) {
            y = 0;
            for (j = 0; j < lcan; j++) {
                p = 2000000000;
                for (k = 0; k < n; k++) {
                    sum = 0;
                    for (i = 0; i < n; i++) {
                        sum += abs(rep[i][j] - rep[k][j]);
                    }
                    if (sum < p) p = sum;
                }
                y += p;
            }
            printf("Case #%d: %d\n", x, y);
        }
        else
            printf("Case #%d: Fegla Won\n", x);
    }
    return 0;
}
