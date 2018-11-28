//
//  main.cpp
//  ProblemA
//
//  Created by Maison Lagorce on 04/01/13.
//  Copyright (c) 2013 Gl0ub1l. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>

#define INPUT_FILENAME  "sample-in"
#define NB_TC           1

void checkTheWinner(char * inputMatrix, int indexOfTestCase) {
    char *solution = (char*)malloc (sizeof (*solution) * 256);;
    bool solutionFound = false;
    
    for( int row=0 ; row<4 && !solutionFound ; row++) {
        if( (inputMatrix[4*row] == 'X' || inputMatrix[4*row] == 'T') &&
           (inputMatrix[4*row+1] == 'X' || inputMatrix[4*row+1] == 'T') &&
           (inputMatrix[4*row+2] == 'X' || inputMatrix[4*row+2] == 'T') &&
           (inputMatrix[4*row+3] == 'X' || inputMatrix[4*row+3] == 'T') ) {
            strcpy(solution, "X won");
            solutionFound = true;
        } else if ((inputMatrix[4*row] == 'O' || inputMatrix[4*row] == 'T') &&
                   (inputMatrix[4*row+1] == 'O' || inputMatrix[4*row+1] == 'T') &&
                   (inputMatrix[4*row+2] == 'O' || inputMatrix[4*row+2] == 'T') &&
                   (inputMatrix[4*row+3] == 'O' || inputMatrix[4*row+3] == 'T') ) {
            strcpy(solution, "O won");
            solutionFound = true;
        }
    }
    for( int col=0 ; col<4 && !solutionFound ; col++) {
        if( (inputMatrix[col] == 'X' || inputMatrix[col] == 'T') &&
           (inputMatrix[col+4] == 'X' || inputMatrix[col+4] == 'T') &&
           (inputMatrix[col+8] == 'X' || inputMatrix[col+8] == 'T') &&
           (inputMatrix[col+12] == 'X' || inputMatrix[col+12] == 'T') ) {
            strcpy(solution, "X won");
            solutionFound = true;
        } else if ((inputMatrix[col] == 'O' || inputMatrix[col] == 'T') &&
                   (inputMatrix[col+4] == 'O' || inputMatrix[col+4] == 'T') &&
                   (inputMatrix[col+8] == 'O' || inputMatrix[col+8] == 'T') &&
                   (inputMatrix[col+12] == 'O' || inputMatrix[col+12] == 'T') ) {
            strcpy(solution, "O won");
            solutionFound = true;
        }
    }
    if( !solutionFound ) {
        if( (inputMatrix[0] == 'X' || inputMatrix[0] == 'T') &&
           (inputMatrix[5] == 'X' || inputMatrix[5] == 'T') &&
           (inputMatrix[10] == 'X' || inputMatrix[10] == 'T') &&
           (inputMatrix[15] == 'X' || inputMatrix[15] == 'T') ) {
            strcpy(solution, "X won");
            solutionFound = true;
        } else if( (inputMatrix[0] == 'O' || inputMatrix[0] == 'T') &&
                  (inputMatrix[5] == 'O' || inputMatrix[5] == 'T') &&
                  (inputMatrix[10] == 'O' || inputMatrix[10] == 'T') &&
                  (inputMatrix[15] == 'O' || inputMatrix[15] == 'T') ) {
            strcpy(solution, "O won");
            solutionFound = true;
        } else if( (inputMatrix[3] == 'X' || inputMatrix[3] == 'T') &&
                  (inputMatrix[6] == 'X' || inputMatrix[6] == 'T') &&
                  (inputMatrix[9] == 'X' || inputMatrix[9] == 'T') &&
                  (inputMatrix[12] == 'X' || inputMatrix[12] == 'T') ) {
            strcpy(solution, "X won");
            solutionFound = true;
        } else if( (inputMatrix[3] == 'O' || inputMatrix[3] == 'T') &&
                  (inputMatrix[6] == 'O' || inputMatrix[6] == 'T') &&
                  (inputMatrix[9] == 'O' || inputMatrix[9] == 'T') &&
                  (inputMatrix[12] == 'O' || inputMatrix[12] == 'T') ) {
            strcpy(solution, "O won");
            solutionFound = true;
        }
    }
    int nbEmpty = 0;
    for(int i=0 ; i<16 && !solutionFound ; i++) {
        if( inputMatrix[i] == '.' )
            nbEmpty ++;
    }
    if( !solutionFound ) {
        if( nbEmpty ) {
        strcpy(solution, "Game has not completed");
        } else {
            strcpy(solution, "Draw");
        }
    }
    printf("Case #%d: %s\n",indexOfTestCase,solution);
}

int main(int argc, const char * argv[])
{
    FILE * file = fopen("/Users/maisonlagorce/Downloads/A-large.in","r");
    int MAX_TC;
    fscanf(file, "%d", &MAX_TC);
    for( int indexOfTestCase=1 ; indexOfTestCase<=MAX_TC ; indexOfTestCase++ )
    {
        char matrix[16];
        fscanf(file, "%s", matrix);
        fscanf(file, "%s", matrix+4);
        fscanf(file, "%s", matrix+8);
        fscanf(file, "%s", matrix+12);
        checkTheWinner(matrix, indexOfTestCase);
    }
    fclose(file);
    return 0;
}


