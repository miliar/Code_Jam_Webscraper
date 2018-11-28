//
//  main.cpp
//  Qual2013-B
//
//  Created by Jonathan Zaid on 4/13/13.
//  Copyright (c) 2013 Jonathan Zaid. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
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

#define TESTSUITE       SMALLFILE_NAME

int isPalindrome(char *str)
{
    int isPalindrome = 1;
    char *start = &str[0];
    char *end = &str[strlen(str)-1];
    while (start < end)
        {
        if (*start != *end)
            {
            isPalindrome = 0;
            break;
            }
        start++;end--;
        }
    
    return isPalindrome;
    
}


void runTest(FILE *in, FILE *out)
{
    int nTestCases;
    fscanf(in, "%d\n", &nTestCases);
    for(int nTest=0;nTest<nTestCases;nTest++)
        {
        long long A,B;
        fprintf(out, "Case #%d: ",nTest+1);
        fscanf(in, "%lld %lld\n",&A,&B);
        long long sqrtA, sqrtB;
        sqrtA = sqrt(A);
        sqrtB = sqrt(B);
        int counter = 0;
        for(long long sqrtVal=sqrtA;sqrtVal<=sqrtB;sqrtVal++)
            {
            char str[101];
            snprintf(str, sizeof(str),"%lld", sqrtVal);
            if (isPalindrome(str))
                {
                long long testVal = sqrtVal * sqrtVal;
                if (testVal >= A && testVal <= B)
                    {
                    snprintf(str, sizeof(str),"%lld", testVal);
                    if (isPalindrome(str))
                        {
                        counter++;
                        fprintf(stderr,"%lld %lld %lld %lld\n", A, B, testVal, sqrtVal);
                        }
                    }
                }
            }
        fprintf(out,"%d\n", counter);
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
 lowest number. 
 e.g. 111
 is palindrome? 111 yes
 211 no
 2143 no
 112
121
 131
 141
 151
 
 make last digit same as first only if it is >= than the first
 increment left digit. if > 9 add another digit. If > B done
 
 
 */

/*
 
 Problem
 
 Little John likes palindromes, and thinks them to be fair (which is a fancy word for nice). A palindrome is just an integer that reads the same backwards and forwards - so 6, 11 and 121 are all palindromes, while 10, 12, 223 and 2244 are not (even though 010=10, we don't consider leading zeroes when determining whether a number is a palindrome).
 
 He recently became interested in squares as well, and formed the definition of a fair and square number - it is a number that is a palindrome and the square of a palindrome at the same time. For instance, 1, 9 and 121 are fair and square (being palindromes and squares, respectively, of 1, 3 and 11), while 16, 22 and 676 are not fair and square: 16 is not a palindrome, 22 is not a square, and while 676 is a palindrome and a square number, it is the square of 26, which is not a palindrome.
 
 Now he wants to search for bigger fair and square numbers. Your task is, given an interval Little John is searching through, to tell him how many fair and square numbers are there in the interval, so he knows when he has found them all.
 
 Solving this problem
 
 Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has 1 Small input and 2 Large inputs. Once you have solved the Small input, you will be able to download any of the two Large inputs. As usual, you will be able to retry the Small input (with a time penalty), while you will get only one chance at each of the Large inputs.
 
 Input
 
 The first line of the input gives the number of test cases, T. T lines follow. Each line contains two integers, A and B - the endpoints of the interval Little John is looking at.
 
 Output
 
 For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of fair and square numbers greater than or equal to A and smaller than or equal to B.
 
 Limits
 
 Small dataset
 
 1 ≤ T ≤ 100.
 1 ≤ A ≤ B ≤ 1000.
 
 First large dataset
 
 1 ≤ T ≤ 10000.
 1 ≤ A ≤ B ≤ 1014.
 
 Second large dataset
 
 1 ≤ T ≤ 1000.
 1 ≤ A ≤ B ≤ 10100.
 
 Sample
 
 
 Input
 
 Output
 
 3
 1 4
 10 120
 100 1000
 Case #1: 2
 Case #2: 0
 Case #3: 2
 

 */
