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
#define C_MAX   (4)

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        uint32 a1,a2;
        uint32 r1[16];
        uint32 r2[16];
        uint32 pos = 0;
        uint32 pos_num[16];
        int32 i, j;

        /* Test Case run once */
        pos = 0;

        scanf("%d", &a1);
        for (i=0; i<4; i++)
        {
            scanf("%d %d %d %d", &r1[(4*i)+0], &r1[(4*i)+1], &r1[(4*i)+2], &r1[(4*i)+3]);
        }

        scanf("%d", &a2);
        for (i=0; i<4; i++)
        {
            scanf("%d %d %d %d", &r2[(4*i)+0], &r2[(4*i)+1], &r2[(4*i)+2], &r2[(4*i)+3]);
        }

        for (i=0; i<4; i++)
        {
            for (j=0; j<4; j++)
            {
                if (r1[((a1 - 1)*4)+i] == r2[((a2 - 1)*4)+j])
                {
                    pos_num[pos] = r1[((a1 - 1)*4)+i];
                    pos++;
                }
            }
        }

#if 0
        for (i=0; i<16; i++)
        {
            printf("row1[%u] = %u\n", i, r1[i]);
            printf("row2[%u] = %u\n", i, r2[i]);
        }
#endif

        /* Print */
        if (pos == 0)
            printf("Case #%d: Volunteer cheated!\n", Ti);
        else if (pos == 1)
            printf("Case #%d: %d\n", Ti, pos_num[0]);
        else
            printf("Case #%d: Bad magician!\n", Ti);
    }

    return 0;
}
