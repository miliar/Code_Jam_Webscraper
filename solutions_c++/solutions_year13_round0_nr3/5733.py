#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//char number[1000000000000001]; //large
char number[10001];

bool is_palindromo(int n)
{
    sprintf(number, "%lu", n);
    char *c = number, *d = number + strlen(number)-1;
    for(; *c; c++, d--)
    {
        if (*c != *d)
            return false;
    }
    return true;
}
int main()
{
    unsigned long T = 0, A = 0, B = 0, X = 0;

    scanf("%lu", &T);

    for (int i = 1; T--; i++)
    {
        scanf("%lu %lu", &A, &B);
        A = (int) ceil(sqrt(A));
        B = (int) floor(sqrt(B));
        X = 0;
        for(;A <= B; ++A)
        {
            if (is_palindromo(A) && is_palindromo( A * A ))
                X++;
        }
        printf("Case #%d: %d\n", i, X);
    }

    return 0;
}
