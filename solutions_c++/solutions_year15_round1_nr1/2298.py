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
#define	N_MAX	(1000)
#define mi_MAX  (10000)

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
    	uint32 N;
		uint32 mi[N_MAX];
        int32 i, j;
		uint32 min_first;
		uint32 min_second;
		uint32 min_rate;

        /* Test Case run once */
		scanf("%u", &N);

		min_first = 0;
		min_second = 0;
		min_rate = 0;
		for (i=0; i<N; i++)
		{
			scanf("%u", &mi[i]);

			
			if ((i > 0) && (mi[i] < mi[(i-1)]))
			{
				/* first method */
				min_first += (mi[(i-1)] - mi[i]);

				/* second method (part 1) */
				if (min_rate < (mi[(i-1)] - mi[i]))
					min_rate = (mi[(i-1)] - mi[i]);
			}
		}

		/* second method (part 2) */
		for (i=1; i<N; i++)
		{
			if (mi[(i-1)] < min_rate)
				min_second += mi[(i-1)];
			else
				min_second += min_rate;
		}

        /* Print */
        printf("Case #%d: %u %u\n", Ti, min_first, min_second);
    }

    return 0;
}

