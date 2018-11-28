#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    long P,Q,T;
    int min_ancestor;
    bool possible = true;

    FILE * input;
    FILE * output;

    input = fopen("A-small-attempt0.in", "r");
    output = fopen("output.out", "w");

    fscanf(input, "%ld", &T);

    for (int i = 0; i < T; i++)
    {
        fscanf(input, "%ld/%ld", &P, &Q);

        if (!(Q == 0) && !(Q & (Q - 1)))
        {
            min_ancestor = 0;
            while (P > 0)
            {
                min_ancestor++;
                Q = Q >> 1;

                if (P == Q)
                    break;

                while ((P == 0) || (P & (P - 1)))
                    P--;

                if (P == Q)
                    break;

                while (!(P%2))
                {
                    P = P >> 1;
                    Q = Q >> 1;
                }

                if (P == Q)
                    break;
            }

            fprintf(output, "Case #%d: %d\n", i+1, min_ancestor);
        }
        else
        {
            fprintf(output, "Case #%d: impossible\n", i+1);
        }
    }

    fclose(input);
    fclose(output);

    return 0;
}
