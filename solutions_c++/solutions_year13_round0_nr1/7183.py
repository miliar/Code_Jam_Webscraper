//
//  main.cpp
//  Qual2013-A
//
//  Created by Jonathan Zaid on 4/13/13.
//  Copyright (c) 2013 Jonathan Zaid. All rights reserved.
//

#include <stdio.h>
#include <math.h>
#include <iostream>

// few generic routines to make things easier
void openFiles(const char *testName, FILE **in, FILE **out);


#define ROWS    4
#define COLS    4

unsigned int winningCombinations[] = {
    0xF000, 0x0F00, 0x00F0, 0x000F,
    0x1111, 0x2222, 0x4444, 0x8888,
    0x1248, 0x8421
};

#define TESTFILE_NAME   "test"
#define SMALLFILE_NAME  "small"
#define LARGEFILE_NAME  "large"

#define TESTSUITE       LARGEFILE_NAME

void runTest(FILE *in, FILE *out)
{
    int nTestCases;
    fscanf(in, "%d\n", &nTestCases);
    for(int nTest=0;nTest<nTestCases;nTest++)
        {
        char line[10];
        fprintf(out, "Case #%d: ",nTest+1);
        int row, col;
        int hole = 0;
        unsigned int X = 0,  O = 0;
        
        for (row=0;row<ROWS;row++)
            {
            fgets(line, sizeof(line), in);
            for(col=0;col<COLS;col++)
                {
                switch (line[col])
                    {
                    case 'X': X |= 1; break;
                    case 'O': O |= 1; break;
                    case 'T': X |= 1; O |= 1; break;
                    case '.': hole = 1;
                    }
                X <<= 1;
                O <<= 1;
                }
            }
        X >>= 1;
        O >>= 1;
        int combination;
        char winner = 0;
        for(combination=0;combination<(sizeof(winningCombinations)/sizeof(unsigned int));combination++)
            {
            if ((O & winningCombinations[combination]) == winningCombinations[combination] )
                {
                winner = 'O';
                break;
                }
            if ((X & winningCombinations[combination]) == winningCombinations[combination])
                {
                winner = 'X';
                break;
                }
            }
        if (winner)
            fprintf(out,"%c won\n", winner);
        else if (hole)
            fprintf(out,"Game has not completed\n");
        else
            fprintf(out, "Draw\n");
        fgets(line, sizeof(line), in);
        } // for all the testcases
    
}


int main(int argc, const char * argv[])
{
    if (argc > 1)   // can specify a directory so we will read from file with testname specified in TESTSUITE
        {
        FILE *in, *out;
        const char *dir = "./";
        char testName[1024];
        if (strncmp(argv[1], "-d", 2) == 0)
            dir = &argv[1][2];
        snprintf(testName, sizeof(testName), "%s/%s",dir,TESTSUITE);
        openFiles(testName, &in, &out);
        runTest(in, out);
        fclose(in);
        fclose(out);
        fflush(stdout);
        }
    else
        {
        runTest(stdin, stdout);  // run from stdin/stdout
        }
    
    
    return 0;
}


// open input/output files. If name not specified, just use stdin/stdout
// otherwise the name should be without a suffix and the input file has ".in" appended and the output file ".out"
void openFiles(const char *testName, FILE **in, FILE **out)
{
    if (testName && *testName)
        {
        char outName[1024+4];
        char inName[1024+4];
        snprintf(inName, sizeof(inName), "%s.in", testName);
        snprintf(outName, sizeof(outName), "%s.out", testName);
        *in = fopen(inName, "r");
        *out = fopen(outName, "w");
        }
    else
        {
        *in = stdin;
        *out = stdout;
        }
    
}

/*
 Problem
 
 Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.
 
 After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.
 
 Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:
 
 "X won" (the game is over, and X won)
 "O won" (the game is over, and O won)
 "Draw" (the game is over, and it ended in a draw)
 "Game has not completed" (the game is not over yet)
 If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable.
 Input
 
 The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.
 
 Output
 
 For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.
 
 Limits
 
 The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.
 
 Small dataset
 
 1 ≤ T ≤ 10.
 
 Large dataset
 
 1 ≤ T ≤ 1000.
 
 Sample
 
 
 Input
 
 Output
 
 6
 XXXT
 ....
 OO..
 ....
 
 XOXT
 XXOO
 OXOX
 XXOO
 
 XOX.
 OX..
 ....
 ....
 
 OOXX
 OXXX
 OX.T
 O..O
 
 XXXO
 ..O.
 .O..
 T...
 
 OXXX
 XO..
 ..O.
 ...O
 
 Case #1: X won
 Case #2: Draw
 Case #3: Game has not completed
 Case #4: O won
 Case #5: O won
 Case #6: O won

 
 */

