#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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
        int N = -1;
        fscanf (input, "%i", &N);
        printf("Line %i: %i\n", line, N);
        if (N==0)
            fprintf(output, "Case #%i: INSOMNIA\n", line+1);
        else
        {
            bool found = false;
            int i = 0;
            bool foundDigits[10] = {0};
            while (!found)
            {
                char Nstring[11];
                sprintf(Nstring, "%d", N*(i+1));
                for (uint pos = 0; pos < strlen(Nstring); pos ++) {
                    char thisDigit = -1;
                    thisDigit = Nstring[pos];
                    int thisDigitInt = atoi(&thisDigit);
                    foundDigits[thisDigitInt]=true;

                    //Now check if they have all been found:
                    bool missedDigit = false;
                    for (int j=0; j<10; j++)
                        if (foundDigits[j]==false) {missedDigit = true; break;}
                    if (!missedDigit)
                        found = true;
                    if (found)
                    {
                        fprintf(output, "Case #%i: %i\n", line+1, N*(i+1));
                        break;
                    }
                }
                if (found)
                    break;
                i++;
            }
        }
    }
    return 0;
}
