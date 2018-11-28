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
#define N_MAX   (100)
#define L_MAX   (100)

char    str_tmp[L_MAX+1];
char    str[N_MAX][L_MAX];
int32   len[N_MAX][L_MAX];
int32   mid[L_MAX];
int32   type[N_MAX];


int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        uint32 N;
        int32 n, i, j, k;
        int32 pos;
        int32 steps;

        /* Test Case run once */
        scanf("%d", &N);

        memset(str, 0, sizeof(str));
        memset(len, 0, sizeof(len));
        memset(type, 0, sizeof(type));

        for (n=0; n<N; n++)
        {
            scanf("%s", &str_tmp[0]);

            //printf("strlen(str_tmp) = %lu\n", (strlen(str_tmp)));

            type[n] = 0;

            for (j=0; j<strlen(str_tmp); j++)
            {
                //printf("<%c>", str_tmp[j]);
                if (str_tmp[j] == 0)
                {
                    //str[n][type[n]] = 0;
                    break;
                }
                else if (j==0)
                {
                    str[n][j] = str_tmp[j];
                    len[n][j] = 1;
                    type[n] = 1;
                }
                else if (str_tmp[j-1] == str_tmp[j])
                {   /* same */
                    //printf("same \n");
                    len[n][(type[n]-1)] += 1;
                }
                else if (str_tmp[j-1] != str_tmp[j])
                {   /* diff */
                    //printf("diff \n");
                    str[n][type[n]] = str_tmp[j];
                    len[n][type[n]] = 1;
                    type[n] += 1;
                }
            }
        }

        pos = 0;
        //printf("str[0] = %s\n", str[0]);
        //printf("str[1] = %s\n", str[1]);
        for (i=1; i<N; i++)
        {
            if (type[0] != type[i])
            {
                //printf("type[0] = %u, type[%u] = %u\n", type[0], i, type[i]);
                pos = -1;   /* impossible */
                break;
            }
            for (j=0; j<type[0]; j++)
            {
                if (str[0][j] != str[i][j])
                {
                    pos = -1;   /* impossible */
                    break;
                }
            }
        }

        if (pos != -1)
        {
            /* find the middle */
            memset(mid, 0, sizeof(mid));

            steps = 0;

            for (j=0; j<type[0]; j++)
            {
                mid[j] = 0;

                for (n=0; n<N; n++)
                {
                    mid[j] += len[n][j];
                }
                mid[j] = mid[j]/N;
                //mid[j] = len[0][j];
                //printf("mid[%u] = %u", j, mid[j]);

                for (n=0; n<N; n++)
                {
                    if (len[n][j] != mid[j])
                    {
                        if (len[n][j] > mid[j])
                        {
                            steps += (len[n][j] - mid[j]);
                        }
                        else
                        {
                            steps += (mid[j] - len[n][j]);
                        }
                    }
                }
            }
        }


        /* Print */
        if (pos != -1)
            printf("Case #%d: %d\n", Ti, steps);
        else
            printf("Case #%d: Fegla Won\n", Ti);
    }

    return 0;
}
