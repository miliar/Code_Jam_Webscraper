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
#define S_MAX   (100 + 1)   /* including \0 */

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        char    c;
        char    S[S_MAX];
        int32   len;
        int32   i;
        char    t;  /* target */
        int32   answer;

        /* Test Case run once */
        scanf("%s", S);
        //printf("S = %s\n", S);

        t = '-';
        answer = 0;
        for (i=(strlen(S)-1); i>=0; i--)
        {
            if (S[i] == t)
            {
                answer += 1;
                t = (t != '+')? '+' : '-';
            }
        }

        /* Print */
        printf("Case #%d: %u\n", Ti, answer);
    }

    return 0;
}
