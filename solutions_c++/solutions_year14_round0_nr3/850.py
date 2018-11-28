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

#define T_MAX   (230)
#define RC_MAX  (50)

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        int32 i, j;
        int32 x, y;
        char map[RC_MAX][RC_MAX];
        int32 R, C, M;
        int32 r,c;
        int32 m = 0;
        int32 end = 0;

        /* Test Case run once */
        scanf("%d %d %d", &R, &C, &M);

        /* reset */
        memset (&map, '.', sizeof(map));

        /* clear */

        /* begin */
        x = 0; y = 0;
        r = R; c = C;
        m = M;
        end = 0;

        while ( ((c > 2) && (r > 2) && (m >= (r + c - 1))) )
        {
            //printf("%s():%d", __FUNCTION__, __LINE__);
            for (i=0; i<r; i++)
            {
                map[(c-1)][i] = '*';
            }
            for (i=0; i<(c-1); i++)
            {
                map[i][(r-1)] = '*';
            }
            m = m - (r + c - 1);
            r = r - 1;
            c = c - 1;
        }

        while ( m > 0 )
        {
            if ( ((r == c) || (r ==1) || (c == 1)) && (m == ((r * c) - 1)) )
            {
                //printf("%s():%d\n", __FUNCTION__, __LINE__);
                for (i=0; i<r; i++)
                {
                    map[(c-1)][i] = '*';
                }
                for (i=0; i<(c-1); i++)
                {
                    map[i][(r-1)] = '*';
                }
                m = m - (r * c - 1);
                r = r - 1;
                c = c - 1;
            } 
            else if ( ((r == 1) || ((r <= c) && (r >= 2))) && (c > 2) && (m >= r) )
            {
                //printf("%s():%d\n", __FUNCTION__, __LINE__);
                for (i=0; i<r; i++)
                {
                    map[c-1][i] = '*';
                }
                m = m - r;
                c = c - 1;
            }
            else if ( ((c == 1) || (c >= 2)) && (r > 2) && (m >= c))
            {
                //printf("%s():%d\n", __FUNCTION__, __LINE__);
                for (i=0; i<c; i++)
                {
                    map[i][r-1] = '*';
                }
                m = m - c;
                r = r - 1;
            }
            else if ((m <= r) && (c != 2))
            {
                if ((r - m) >= 2)
                {
                    //printf("%s():%d\n", __FUNCTION__, __LINE__);
                    for (i=0; i<m; i++)
                    {
                        map[c-1][r-1-i] = '*';
                    }
                    m = 0;
                    break;
                }
                else
                {
                    //printf("%s():%d\n", __FUNCTION__, __LINE__);
                    for (i=0; i<(m-1); i++)
                    {
                        map[c-1][r-1-i] = '*';
                    }
                    m = 1;
                    c = c - 1;
                }
            }
            else if ((m <= c) && (r != 2))
            {
                if ((c - m) >= 2)
                {
                    //printf("%s():%d\n", __FUNCTION__, __LINE__);
                    for (i=0; i<m; i++)
                    {
                        map[c-1-i][r-1] = '*';
                    }
                    m = 0;
                    break;
                }
                else
                {
                    //printf("%s():%d\n", __FUNCTION__, __LINE__);
                    for (i=0; i<(m-1); i++)
                    {
                        map[c-1-i][r-1] = '*';
                    }
                    m = 1;
                    r = r - 1;
                }
            }
            else
            {
                /* fail */
                break;
            }
        }

        /* print */
        map[0][0] = 'c';

        printf("Case #%d:\n", Ti);

        /* is it possible ? */
        if (m == 0)
        {
            /* print the map */
            for (y=0; y<R; y++)
            {
                for (x=0; x<C; x++)
                {
                    printf("%c", map[x][y]);
                }
                printf("\n");
            }
        }
        else
        {
            printf("Impossible\n");
#if 0
            printf("--------------------------------------------------------\n");
            printf("m = %u\n", m);
            /* print the map */
            for (y=0; y<R; y++)
            {
                for (x=0; x<C; x++)
                {
                    printf("%c", map[x][y]);
                }
                printf("\n");
            }
#endif
        }

    }

    return 0;
}
