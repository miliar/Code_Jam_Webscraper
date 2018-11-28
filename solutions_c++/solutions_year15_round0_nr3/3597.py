/* Author: Fleseriu Cristian Valentin
 * Mail: fleseriu.cristian@webmonsters.ro
 * Google Jam - Qualification Round - Dijkstra
 */

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using std::string;

char multiplyQuaternion(char a, char b, bool *minus) {
    bool m = *minus;
    char res;

    switch (a) {
        case '1':
            res = b;
        break;
        
        case 'i':
            switch (b) {
                case '1':
                    res = 'i';
                break;

                case 'i':
                    res = '1';
                    m = !m;
                break;

                case 'j':
                    res = 'k';
                break;

                case 'k':
                    res = 'j';
                    m = !m;
                break;
            }
        break;
        
        case 'j':
            switch (b) {
                case '1':
                    res = 'j';
                break;

                case 'i':
                    res = 'k';
                    m = !m;
                break;

                case 'j':
                    res = '1';
                    m = !m;
                break;

                case 'k':
                    res = 'i';
                break;
            }
        break;

        case 'k':
            switch (b) {
                case '1':
                    res = 'k';
                break;

                case 'i':
                    res = 'j';
                break;

                case 'j':
                    res = 'i';
                    m = !m;
                break;

                case 'k':
                    res = '1';
                    m = !m;
                break;
            }
        break;
    }
    //printf("\n a(%c)*b(%c)*m(%d)=acc(%c),m(%d)",a,b,*minus,res,m);
    *minus = m;
    return res;
}

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
        bool isCollapsable = false;
        int L, X;
        char seq[10000];

        bool trigI = false;
        bool trigJ = false; 
        bool trigK = false;
        // bool minus = false;

        fscanf(input, "%d", &L);
        fscanf(input, "%d", &X);

        fscanf(input, "\n");
        for(int j=0; j<L; j++) {
            fscanf(input, "%c", &seq[j]);
        } printf("######\n\n");

        char accumulator = '1';
        bool accMinus = false;

        // char stack[10000];

        for(int k=0; k<X; k++) {
            for(int j=0; j<L; j++) {
                printf("%c",seq[j]);
                if(!trigI) {
                    if(accumulator=='i') {
                        trigI = true;
                        printf("|");
                        accumulator = '1';
                    }
                    else {
                        accumulator = multiplyQuaternion(accumulator,seq[j],&accMinus);
                        if (accumulator == 'i') {
                            trigI = true;
                            printf("|");
                            accumulator = '1';
                        }
                    }
                }
                else if(!trigJ) {
                    if(accumulator=='j') {
                        trigJ = true;
                        printf("|");
                        accumulator = '1';
                    }
                    else {
                        accumulator = multiplyQuaternion(accumulator,seq[j],&accMinus);
                        if (accumulator == 'j') {
                            trigJ = true;
                        printf("|");
                            accumulator = '1';
                        }
                    }
                }
                else if (!trigK) {
                    if(accumulator=='k') {
                        trigK = true;
                        printf("|");
                        accumulator = '1';
                    }
                    else {
                        accumulator = multiplyQuaternion(accumulator,seq[j],&accMinus);
                        if (accumulator == 'k') {
                            trigK = true;
                        printf("|");
                            accumulator = '1';
                        }
                    }
                }
                else {
                    accumulator = multiplyQuaternion(accumulator,seq[j],&accMinus);
                }
            }
        }
        if (trigI && trigJ && trigK) {
            printf("@@%d %c@@",accMinus,accumulator);
        }
        if(trigI && trigJ && trigK && !accMinus && accumulator == '1') {
            isCollapsable = true;
        }

        fprintf(output, "Case #%d: ", i);
        if(isCollapsable) {
            fprintf(output, "YES");
        }
        else {
            fprintf(output, "NO");
        }
        fprintf(output, "\n");
    }

    fclose(input);
    fclose(output);

    return 0;
}

