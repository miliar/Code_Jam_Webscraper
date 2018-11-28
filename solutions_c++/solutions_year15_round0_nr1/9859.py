/* Author: Vasile Mihail-Raul
 * Mail: vasile.raul@webmonsters.ro
 * Google Jam - Qualification Round - Standing Ovation
 */

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
    if(argc < 2) {
        printf("Error: not enough parameters\n");
        printf("Info: usage: ./stading input_file output_file\n");
        return 0;
    }

    FILE *input;
    FILE *output;

    char inputFile[10];
    char outputFile[10];

    int numberOfCases;

    strcpy(inputFile, argv[1]);
    strcpy(outputFile, argv[2]);

    input = fopen(inputFile, "r");
    output = fopen(outputFile, "w");

    if(input == NULL) {
        printf("Error on opening input file\n");
        return 0;
    }

    if(output == NULL) {
        printf("Error on opening output file\n");
        return 0;
    }

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

