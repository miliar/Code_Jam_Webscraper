#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000

int splits(int *arr, int cakes)
{
    int divs = 0;

    for (int i=1000; i>cakes; i--)
    {
        if (i % cakes)
        {
            divs += (arr[i] * (i / cakes));
        }
        else
        {
            divs += (arr[i] * ((i / cakes)-1));
        }
    }
    return divs;
}
    
int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int N, M;
    int a[10000];
    int i, j, k;

    if (argc != 2)
    {
        exit(-1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Usage: file is no good\n");
        exit(-1);
    }


    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    T = atoi(token);

    for (i=0; i<T; i++)
    {
        double C, F, X;
        double t, t1, t2;
        double rate;
        int D;
        int P[1001];
        int time=0;

        for (j=1; j<1001; j++) P[j]=0;

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);
        D = atoi(token);

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        /* if highest number is odd, decrement all (+1 min)
         * otherwise:
         *   if only one largest, divide it by 2 (+1 min)
         *   no point dividing if there are h/2 highest items
         */


        /* Tally up the pancakes */

        subtoken = strtok_r(token, " ", &sptr2);
        P[atoi(subtoken)]++;

        for (j=1; j<D; j++)
        {
            subtoken = strtok_r(NULL, " ", &sptr2);
            P[atoi(subtoken)]++;
        }

#if 0
        for (j=1000; j>0; j--)
        {
            while (P[j] > 0)
            {
                //printf("There are %d dishes with %d pancakes\n", P[j], j);
                if (j % 2)
                {
                    /* Find the next size down */
                    for (k=j-1; k>0 && P[k] == 0; k--);

                    /* If the next num down */
                    if (k > 0 &&
                        j - k > P[j]);

                    /* Shift pancakes */
                    for (k=1; k<j; k++)
                    {
                        P[k] = P[k+1];
                    }
                    P[j] = 0;
                    //printf("eat %d\n", j);
                    time++;
                }
                /* if you have 8 dishes with 20 pancakes, ok
                * if you have 10 dishes with 20 pancakes, ok
                * if you have 12 dishes with 20 pancakes, forget it */
                else
                {
                    int half = 0;

                    for (k=(j/2)+1; k<j+1; k++)
                    {
                        half += P[k];
                    }
                    if ((j / 2) >= half)
                    {
                        P[j]--;
                        P[j/2] += 2;
                        //printf("share %d cakes, %d left\n", j, P[j]);
                        time++;
                    }
                    else
                    {
                        /* Just eat */
                        for (k=1; k<j; k++)
                        {
                            P[k] = P[k+1];
                        }
                        P[j] = 0;
                        //printf("just eat\n");
                        time++;
                    }
                }
            };
        }
#endif
#if 0
        /* We want to split until the it's no longer worthwhile to do so */
        for (j=1000; j>0; j--)
        {
            if (P[j] > 0)
            {
                printf("%d dishes with %d cakes\n", P[j], j);
                if (time + P[j] < j)
                {
                    printf("- split them\n");
                    while (P[j] > 0)
                    {
                        P[j]--;
                        if (j % 2)
                        {
                            // odd split
                            P[(j+1)/2]++;
                            P[(j-1)/2]++;
                        }
                        else
                        {
                            // even split
                            P[j/2] += 2;
                        }
                        time++;
                        printf("- > time is now %d\n", time);
                    };
                }
                else /* end of the line */
                {
                    time += j;
                    break;
                }
            }
        }
#endif
        /*
21/7 = 3  (equal, so 2)
17/7 = 2  ==> 4 + 7 = 11

x - 1 / 7

21-1/6 = 3
17-1/6 = 3 ==> 6 + 6 = 12
cuts < selected
*/
        time = 10000000;
        for (j=1000; j>0; j--)
        {
            int mins = splits(P, j);

            //printf("mins = %d, j = %d\n", mins, j);
            if (time > mins + j) time = mins + j;
        }


        printf("Case #%d: %d\n", i+1, time);
    }


    fclose(fp);
    return 0;
}
