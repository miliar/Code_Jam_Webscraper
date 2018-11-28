#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

void flip (char* stack, int count);

int main(int argc, char *argv[])
{
    FILE *input, *output;
    input=fopen("input", "r");
    output=fopen("output", "w");

    int lines = 0;
    fscanf (input, "%i", &lines);
    printf("Line count: %i\n", lines);

    for (int line=0; line < lines; line++)
    {
        printf("Line %i\n", line);
        int K, C, S;
        fscanf (input, "%i %i %i", &K, &C, &S);

        printf("K: %i C: %i S: %i\n", K,C,S);
        if (! (C * S >= K))
            fprintf(output, "Case #%i: IMPOSSIBLE\n", line+1);
        else if (S>=K)
        {
            fprintf(output, "Case #%i:", line+1);
            for (int i = 0; i < K; i++)
                fprintf(output, " %i", i+1);
            fprintf(output, "\n");
        }
        else
        {
            float requiredStudentCount = (float)K/(float)C;
            requiredStudentCount = ceil(requiredStudentCount);
            printf("requiredStudentCount: %f\n", requiredStudentCount);
            int i = 0;
            fprintf(output, "Case #%i:", line+1);
            for(int student = 0; student<requiredStudentCount; student++)
            {
                printf("Student %i\n", student);
                unsigned long long int tile = 0;
                for(int level = 0; level < C; level++)
                {
                    unsigned long long int offset=pow(K,level);
                    unsigned long long int thisOffset;
                    if (i<K)
                    {
                        thisOffset=offset*i;
                        printf("(%i ^ %i * %i)+", K,level,i);
                    }
                    else
                    {
                        thisOffset=offset*0;
                        printf("(%i ^ %i * %i)+", K,level,0);
                    }
                    tile=tile+thisOffset;
                    i++;
                }
                fprintf(output, " %llu", tile + 1);
            }
            fprintf(output, "\n");
        }

    }
    return 0;
}

