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
#define N_MAX   (1000000)

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
		uint32 N;         /* original N */
        uint32 nn;          /* n * N */
        uint32 r;
    	uint32 digit_map;   /* bit 9..0 */
        uint32 answer;

        /* Test Case run once */
        scanf("%u", &N);
        if (N <= 0)
        {
            printf("Case #%d: INSOMNIA\n", Ti);
            continue;
        }
        else
        {
            int32 i;

            /* clear info */
            digit_map = 0;
            answer = 0;

            for (i=1; i<=100; i++)   /* it should cover the whole possible cases */
            {
                nn = i * N; /* init */

                while (nn > 0)
                {
                    r = nn % 10;
                    digit_map |= 0x1 << r;
                    if ((digit_map & 0x3FF) == 0x3FF)
                    {
                        /* i-th is the answer */
                        answer = i * N;
                        break;
                    }
                    nn /= 10;   /* the next digit */
                }

                if (answer)
                    break;
            }

        }

        /* Print */
        printf("Case #%d: %u\n", Ti, answer);
    }

    return 0;
}
