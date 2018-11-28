#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    FILE *in = fopen("in.txt", "rt");
    FILE *out= fopen("out.txt", "wt");

    unsigned int cases = 0;
    unsigned int A = 0;
    unsigned int B = 0;
    unsigned int K = 0;

    fscanf(in, "%d\n", &cases);
    for (unsigned int idx = 0; idx < cases; idx++)
    {
        fscanf(in, "%d %d %d\n", &A, &B, &K);
        unsigned int a1 = 0;
        unsigned int b1 = 0;
        unsigned int count = 0;
        unsigned int t = 0;
        if (K == 0)
        {
            fprintf(out, "Case #d: 1\n", idx+1);fflush(out);
        }
        //if (A == B && B == K)
        //{
        //    fprintf(out, "Case %d: 1\n", idx+1);
        //}
        while (a1 < A)
        {
            while (b1 < B)
            {
                t=a1&b1;
                if (t < K)
                    count++;
                b1++;
            }
            a1++;
            b1=0;
        }
        fprintf(out, "Case #%d: %d\n", idx+1, count);fflush(out);
    }
    fclose(in);
    fclose(out);
    return 0;
}