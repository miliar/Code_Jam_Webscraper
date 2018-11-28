/* Author: Vasile Mihail-Raul
 * Mail: vasile.raul@webmonsters.ro
 * Google Jam - Qualification Round - Ominous Omino
 */

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int maxim(int value1, int value2) {
    return value1 > value2 ? value1 : value2;
}

int minim(int value1, int value2) {
    return value1 < value2 ? value1 : value2;
}

int main(int argc, char* argv[]) {
    if(argc < 2) {
        printf("Error: not enough parameters\n");
        printf("Info: Usage: ./omino input_file output_file\n");
        return 0;
    }

    FILE *input;
    FILE *output;

    char inputFile[20];
    char outputFile[20];

    int numberOfTests;

    strcpy(inputFile, argv[1]);
    strcpy(outputFile, argv[2]);

    input = fopen(inputFile, "r");
    output = fopen(outputFile, "w");

    if(input == NULL) {
        printf("Error on opening input file!\n");
        return 0;
    }

    if(output == NULL) {
        printf("Error on opening output file!\n");
        return 0;
    }

    fscanf(input, "%d", &numberOfTests);

    for(int i = 1; i <= numberOfTests; i++) {
        int X, R, C, winner = 0; // 0 - Gabriel / 1 - Richard

        fscanf(input, "%d %d %d", &X, &R, &C);

        if (X == 1) { 
            winner = 0;
        } else if (X >= 7) { 
            winner = 1;
        } else if (maxim(R, C) < X) { 
            winner = 1;
        } else if((R * C) % X > 0) { 
            winner = 1;
        } else if(X == 2) { 
            winner = 0;
        } else if(minim(R, C) < ((float)X / 2)) {
            winner = 1;
        } else if((X % 2 == 1 && (((X + 1) / 2) > C || ((X + 1) / 2) > R)) || 
                  (X % 2 == 0 && ((X / 2) > C || (X / 2) > R || (X / 2) + 1 > C || (X / 2) + 1 > R))) {
            winner = 1;	
        }

        fprintf(output, "Case #%d: ", i);

        if(winner == 1) {
            fprintf(output, "RICHARD\n");
        } else {
            fprintf(output, "GABRIEL\n");
        }
    }

    fclose(input);
    fclose(output);

    return 0;
}

