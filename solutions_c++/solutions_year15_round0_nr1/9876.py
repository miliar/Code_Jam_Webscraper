#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *input;
    FILE *output;

    int numberOfCases;

    input = fopen("input.txt", "r");
    output = fopen("output.txt", "w");

    fscanf(input, "%d", &numberOfCases);

    for(int i = 1; i <= numberOfCases; i++) {
        int Smax;
        int sum = 0;
        int pplNeed = 0;
        char* shyness;

        fscanf(input, "%d", &Smax);

        shyness = (char *) malloc(Smax + 1);
        
        fscanf(input, "%s", shyness);
        
        for(int j = 0; j <= Smax; j++) {
            int aud = shyness[j] - '0';

            if(aud != 0 && j > sum) {
                pplNeed += j - sum;
                sum += pplNeed;
            }

            sum += aud; 
        }

        fprintf(output, "Case #%d: %d\n", i, pplNeed);
    }

    fclose(input);
    fclose(output);

    return 0;
}

