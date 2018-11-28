#include <cstdio>
const int C[] = {1, 4, 9, 121, 484};
int main()
{
    FILE *fin = fopen("Fair and Square.in", "r"), *fout = fopen("Fair and Square.out", "w");
    int t, i, a, b, result, j;
    fscanf(fin, "%d", &t);
    for(i = 1; i <= t; i++)
    {
        fscanf(fin, "%d%d", &a, &b);
        result = 0;
        for(j = 0; j < 5; j++)
            if(a <= C[j] && C[j] <= b)
                result++;
        fprintf(fout, "Case #%d: %d\n", i, result);
    }
    return 0;
}
