#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    FILE *input = fopen("Input.in", "r+"), *output = fopen("output.out","r+");

    bool chiffres[10] = {false, false, false, false, false ,false , false ,false ,false ,false};

    int N;
    int i ,j;
    fscanf(input, "%d", &N);
    int n, nvn, cpt, temp;
    bool done;
    for ( i = 1; i <= N; i++)
    {
        fscanf(input, "%d", &n);
        if ( n == 0) fprintf(output, "Case #%d: INSOMNIA\n",i);
        else
        {
            done = false;
            nvn = 0;
            for ( j = 0; j < 10; j++) chiffres[j] = false;
            while( !done )
            {
                nvn += n;
                done = true;
                temp = nvn;
                while ( temp > 0)
                {
                    chiffres[(temp%10)] = true;
                    temp /= 10;
                }
                for ( j = 0; j < 10; j++)
                {
                    if ( !chiffres[j]) done = false;
                }
            }

            fprintf(output, "Case #%d: %d\n",i, nvn);
        }


    }
    fclose(output);
    fclose(input);
    return 0;
}

