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

#define T_MAX   (50)

#define N_MAX   (1000)


int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        int32 i, j;
        uint32 N;
        double wt_blk[2][N_MAX];
        uint8 vb_blk[2][N_MAX];
        uint32 dw_point;
        uint32 w_point;

        /* Test Case run once */
        dw_point = 0;
        w_point = 0;
        scanf("%d", &N);

        /* load data */
        for (i=0; i<2; i++)
        {
            for (j=0; j<N; j++)
            {
                scanf("%lg", &wt_blk[i][j]);
                //printf("%f\n", wt_blk[i][j]);
            }
        }

        /* sorting */
        std::sort(wt_blk[0], wt_blk[0] + N);
        std::sort(wt_blk[1], wt_blk[1] + N);
#if 0
        for (i=0; i<N; i++)
        {
            printf("%g ", wt_blk[0][i]);
        }
        printf("\n");
        for (i=0; i<N; i++)
        {
            printf("%g ", wt_blk[1][i]);
        }
#endif

        /* DW */
        for (i=0; i<2; i++)
        {
            for (j=0; j<N; j++)
            {
                vb_blk[i][j] = 1;   /* valid */
            }
        }

        // max to win the best choice
        for (i=0,j=0; i<N; i++)
        {
            for (; j<N; j++)
            {
                if (vb_blk[1][(N-1)-j] == 0)
                    continue;

                if (wt_blk[0][(N-1)-i] > wt_blk[1][(N-1)-j])
                {
                    dw_point++;
                    vb_blk[1][(N-1)-j] = 0;
                    break;
                }
            }
        }

        /* W */
        // max to win the best choice (for Ken)
        for (i=0,j=0; i<N; i++)
        {
            for (; j<N; j++)
            {
                if (vb_blk[0][(N-1)-j] == 0)
                    continue;

                if (wt_blk[1][(N-1)-i] > wt_blk[0][(N-1)-j])
                {
                    w_point++;
                    vb_blk[0][(N-1)-j] = 0;
                    break;
                }
            }
        }

        /* Print */
        printf("Case #%d: %u %u\n", Ti, dw_point, (N - w_point));
    }

    return 0;
}
