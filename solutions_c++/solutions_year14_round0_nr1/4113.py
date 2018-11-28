#include <stdlib.h>
#include <stdio.h>
#include <string.h>

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
   int row1;
   int row2;
   int cards1[4][4];
   int cards2[4][4];
   int cardFace;
} testcase;

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   int *chosen1 = tc.cards1[tc.row1];
   int *chosen2 = tc.cards2[tc.row2];

   int nTotalMatches = 0;
   for( int i=0; i<4; ++i )
   {
      int nMatches = 0;
      for( int j=0; j<4; ++j )
      {
         if( chosen1[i] == chosen2[j] )
            ++nMatches;
      }
      // printf("column%d: matches = %d\n", i, nMatches);
      if( nMatches == 1 ) {
         tc.cardFace = chosen1[i];
         ++nTotalMatches;
      }
      else if( nMatches > 1 )
      {
         tc.cardFace = -1;
      }
   }
   if( nTotalMatches > 1 )
      tc.cardFace = -1;
   else if( nTotalMatches <= 0 )
      tc.cardFace = -2;
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   char line[1024];

   fgets(line, sizeof(line) - 1, fp);
   tc.row1 = atoi(line) - 1;
   for( int i=0; i<4; ++i )
   {
      fscanf(fp, "%d %d %d %d\n",
            &tc.cards1[i][0],
            &tc.cards1[i][1],
            &tc.cards1[i][2],
            &tc.cards1[i][3]
            );
   }

   fgets(line, sizeof(line) - 1, fp);
   tc.row2 = atoi(line) - 1;
   for( int i=0; i<4; ++i )
   {
      fscanf(fp, "%d %d %d %d\n",
            &tc.cards2[i][0],
            &tc.cards2[i][1],
            &tc.cards2[i][2],
            &tc.cards2[i][3]
            );
   }
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   if( tc.cardFace == -1 )
      fprintf(fp, "Bad magician!");
   else if( tc.cardFace == -2 )
      fprintf(fp, "Volunteer cheated!");
   else
      fprintf(fp, "%d", tc.cardFace);
}

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
   testcase cases[101];
   for( int i=0; i<t; ++i )
   {
      readtestcase(cases[i], in);
   }
   fclose(in);

   for( int i = 0; i < t; ++i )
   {
      solve(cases[i]);
      
      fprintf(out, "Case #%d: ", 1 + i);
      writetestcase(cases[i], out);
      fprintf(out, "\n"); 
      fflush(out);
   }
   fclose(out);
}
