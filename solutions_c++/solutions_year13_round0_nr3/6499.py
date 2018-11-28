#include <math.h>
#include <stdio.h>
int palind (int);


int main ()
{
    double val;
    int i, tc, min, max, icount = 0, caseNum = 1;

    printf ("enter the number of testcases :");
    scanf ("%d", &tc);

    while (tc)
    {
         tc--;
//        printf ("enter min and max values :");
        scanf ("%d %d", &min, &max);

        for (i = min; i <= max; i++)
        {
            val = sqrt (i);
            if (val != (int) val)
                continue;
            else {
                if (!palind (i) )
                {
                     if(!palind (val) )
                     {
                         icount++;
 //                        printf ("\t%d:palind - success\n", i);
                     }
                }
            }
        }
        printf ("Case #%d: %d\n", caseNum, icount);
        icount = 0;
        caseNum++;
    }
    return 0;
}

int palind (int org)
{
    int dup = org, res = 0;

    while (dup)
    {
         res = (res * 10) + (dup%10);
         dup /= 10;
    }

//    printf ("%d org: %d\n", res, org);
    if (res == org)
        return 0;
    else
        return -1;
}