#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

// gcc -o xxxx .c

#define ITEM 4

int TC = 1, T, N, result;
int i,j, count;

long long A, B, K;

int main ()
{
    for (scanf ("%d", &T); TC <= T; TC++)
    {
        scanf ("%I64d %I64d %I64d", &A, &B, &K);
                 
        count = 0;   
        for (i = 0 ; i < A; i++)
        {
           for (j = 0 ; j < B; j++)
             if ((i&j) < K)
                count ++;
        }
                    
         printf ("Case #%d: %d\n", TC, count);

    }

    return 0;
}
