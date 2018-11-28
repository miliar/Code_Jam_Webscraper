#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main()
{
    int t, N, cas, res1, res2;
    long mote[101];
    int i,j;
    long A;

    scanf("%d", &t);
    cas=0;
    while(t--)
    {
        cas++;
        scanf("%ld%d", &A, &N);

        for(i=0;i<N;i++)
            scanf("%ld", &mote[i]);

        qsort(mote, N, sizeof(int), compare);

        res1=0;
        res2=0;
        for(i=0;i<N;i++)
        {
            if(A > mote[i])
            {
                A += mote[i];
            }
            else
            {
                res1 = 0;
                while((A <= mote[i]) && (A!=1))
                {
                    res1++;
                    A = ((2*A) -1);
                }
                if((res1 > (N-i)) ||(A==1))
                {
                    res2 += (N - i);
                    break;
                }
                else
                    res2 += res1;
                    A += mote[i];
            }
        }

        printf("Case #%d: %d\n", cas, res2);
    }

    return 0;
}
