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

#define D_MAX   (1000)
#define Pi_MAX  (1000)

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        int32 i, j,k;
		int32 D;
		int32 P[D_MAX];
		int32 same;
		int32 times_split;
		int32 max_height;
		int32 sum_cost;
		int32 p;
		int32 cost_min;
		int32 gain_min;
		

        /* Test Case run once */
		scanf("%d", &D);

		times_split = 0;
		max_height = 0;
		sum_cost = 0;
		printf("CASE# %u (D = %u)\n", Ti, D);
		for (i=0; i<D; i++)
		{
			scanf("%d", &P[i]);
		}
		sort(P, P+D);
		reverse(P, P+D);
#if 1
		printf("P: ");
		for (i=0; i<D; i++)
		{
			printf("[%u] ", P[i]);
		}
		printf("\n");
#endif
		for (i=0; i<D; i++)
		{
			p = P[i];
			j = 1;
			//printf("[DBG] p = %u, j = %u\n", p, j);
#if 1
			/* find out how many same numbers */
			same = 1;
			for (k=i+1; k<D; k++)
				if ((P[k] == P[i])|| (P[k] == (P[i] - 1))) same++; else break;
		    //printf("same: %u\n", same);
#endif 

			while((p > max_height) && (((p - (p - (p / 2))) - j) > 0) && (((p - (p - (p / 2))) - j) >= same))
			//while((p > max_height) && (((p - (p - (p / 2))) - j) > 0))
			{
				printf("[DBG] D(%u) [%u] split to %u, %u\n", i, p, (p - (p - (p / 2))), (p - (p / 2)));

				/* special min */
				sum_cost += j;
				p = (p - (p / 2));
				j = j * 2;
				//printf("[DBG] p = %u, j = %u\n", p, j);


				/* find out how many same numbers */
				same = 1;
				for (k=i+1; k<D; k++)
					if ((P[k] == p) ||(P[k] == (p - 1)))  same++; else break;
				//printf("same: %u\n", same);
			}
			if (p > max_height) max_height = p;
			//printf("[DBG] p = %u, max_height = %u\n", p, max_height);

		}

        /* Print */
        printf("Case #%d: %u\n", Ti, (sum_cost + max_height));
    }

    return 0;
}
