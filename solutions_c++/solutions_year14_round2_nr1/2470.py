// #include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

// using namespace std;

/* 
 * runme:
 *   g++ -o filename.o filename.cpp
 *   ./filename.o M-example.in
 *
 * runme vim:
 *  unix  - :w | !g++ -o %.o % ; ./%.o M-example.in
 *                                              && instead of ; ?
 *  mswin - :w | !cl % & %:r.exe a-example.in
 *
 * where M-example.in could be: [ABCD]-(example|small|large).in
 */

/*
 * store one test case, both problem and solution, no intermediates
 */
typedef struct testcase_s {
   char arrStrings[103][103];
   int numStrings;
   int numMoves;
} testcase;

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   tc.numMoves = -1;

   // make all strings identical with actions
   // 1) repeat any single character
   // 2) delete any one repeat character

   // TODO: Figure out "middle" value to copy...

   char *p[100];
   int numMovesSoFar = 0;
   for( int i=0; i<tc.numStrings; ++i )
      p[i] = tc.arrStrings[i];

   for( int i=1; i<tc.numStrings; ++i )
   {
      char *p1 = tc.arrStrings[0];
      char *p2 = tc.arrStrings[1];
      while( *p1 != '\0' || *p2 != '\0' )
      {
         if( *p1 != *p2 )
            return;
         char c = *p1;
         while( c == *p1 )
            ++p1;
         while( c == *p2 )
            ++p2;
      }
   }

   int lens[100];
   while( 1 )
   {
      char c = *p[0];
      for( int i=0; i<tc.numStrings; ++i )
      {
         if( c != *p[i] )
         {
            printf("\n--error can't fail--");
            return;
         }
         if( c == '\0' )
            continue;
         //printf("p[%d] = %s, ", i, p[i]);
         lens[i] = 0;
         while( *p[i] == c )
         {
            ++lens[i];
            ++p[i];
         }
         //printf("lens[%d] = %d, ", i, lens[i]);
      }
      if( c == '\0' )
         break;
      //printf("\n");

     int maxLen = 0;
     //printf("%c ", c);
     for( int i=0; i<tc.numStrings; ++i )
     {
        //printf("%d, ", lens[i]);
        if( maxLen < lens[i] )
           maxLen = lens[i];
     }
     //printf("\n");

     if( tc.numStrings == 2 )
     {
        numMovesSoFar += abs(lens[0] - lens[1]);
        continue;
     }

      // moves = min difference of all lengths to one value...
      int minMove = 500;
      for( int tryLen = 1; tryLen <= maxLen; ++tryLen )
      {
         int move = 0;
         for( int i=0; i<tc.numStrings; ++i )
            move += abs(lens[i] - tryLen);

         if( move < minMove )
            minMove = move;
      }
      numMovesSoFar += minMove;
   }
   tc.numMoves = numMovesSoFar;
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   fscanf(fp, "%d\n", &tc.numStrings);
   for( int i=0; i<tc.numStrings; ++i )
   {
      fgets(tc.arrStrings[i], sizeof(tc.arrStrings[i]) - 1, fp);
      size_t n = strcspn(tc.arrStrings[i], "\r\n");
      tc.arrStrings[i][n] = '\0';
   }
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   if( tc.numMoves < 0 )
      fprintf(fp, "Fegla Won");
   else
      fprintf(fp, "%d", tc.numMoves);
}

testcase cases[100];

/*
 * Process command line argument (input file), count test cases, call solve().
 */
int main(int argc, char **argv)
{
   FILE *in = stdin;
   FILE *out = stdout;
   if( argc >= 2 )
   {
      char outname[256];
      const char *end = strrchr(argv[1], '.');
      int len = NULL == end ? strlen(argv[1]) : end - argv[1];
      sprintf(outname, "%.*s.out", len, argv[1]);
      in = fopen(argv[1], "r");
      out = fopen(outname, "w");
   }

   int t;
   fscanf(in, "%d ", &t);
   for( int i=0; i<t; ++i )
   {
      readtestcase(cases[i], in);
   }
   fclose(in);

   for( int i = 0; i < t; ++i )
   {
      //printf("\n\n-- solving case #%d --\n", i + 1);
      solve(cases[i]);
      
      fprintf(out, "Case #%d: ", 1 + i);
      writetestcase(cases[i], out);
      fprintf(out, "\n"); 
      fflush(out);
   }
   fclose(out);
}
