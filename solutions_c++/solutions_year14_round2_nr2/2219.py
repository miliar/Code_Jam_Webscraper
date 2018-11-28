#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;

typedef signed long long    int64;
typedef unsigned long long  uint64;
typedef signed int          int32;
typedef unsigned int        uint32;
typedef signed short        int16;
typedef unsigned short      uint16;
typedef signed char         int8;
typedef unsigned char       uint8;

#define T_MAX   (100)

#define A_MAX   (1000000000)
#define B_MAX   (1000000000)
#define K_MAX   (1000000000)

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        int32 i, j;
        uint32 A, B, K;
        uint32  a,b,k;
        uint32  win;

        /* Test Case run once */
        scanf("%u %u %u", &A, &B, &K);

        win = 0;
        for (a=0; a<A; a++)
        {
            for (b=0; b<B; b++)
            {
                if ((a & b) < K)
                    win++;
            }
        }

        /* Print */
        printf("Case #%d: %u\n", Ti, win);
    }

    return 0;
}
