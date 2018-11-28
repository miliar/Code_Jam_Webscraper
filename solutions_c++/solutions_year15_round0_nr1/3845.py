#include <stdio.h>
#include <stdlib.h>

FILE * f;
FILE * fl;
char v[1024];

int main()
{
    int test, cases;
    int shyMax; ///maximum shyness (vettore persone - 1)
    int i;

    f = fopen("A-large.in", "r");
    fl = fopen("A-large.out", "w");
    fscanf(f, "%d", &cases);

    for(test = 0; test < cases; test++)
    {
        int out = 0;
        int people = 0;
        fscanf(f, "%d", &shyMax);

        //printf("\n%d ", shyMax); ///debug

        fscanf(f, "%s", v);
        for(i = 0; i <= shyMax; i++)
        {
            if(people < i)
            {
                out += i - people;
                people = i + (v[i] - 48);
            }
            else
            {
                people += (v[i] - 48);
            }

        }
        if(test == cases-1)
            fprintf(fl, "Case #%d: %d", test+1, out);
        else
            fprintf(fl, "Case #%d: %d\n", test+1, out);
    }
    fclose(f);

    /*f = fopen("A-small-attempt1.out", "w");
    for(test = 0; test < cases; test++)
    {
        fprintf(f, "Case #%d: %d\n", test+1, out);
    }*/

    fclose(fl);
    return 0;
}
