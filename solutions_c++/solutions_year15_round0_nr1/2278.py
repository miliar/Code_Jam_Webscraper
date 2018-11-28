// #include <stdlib.h>
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
 *  mswin - :w | !cl % & %:r.exe M-example.in
 *
 * where M-example.in could be: [ABCD]-(example|small|large).in
 */

/*
 * store one test case, both problem and solution, no intermediates
 */
typedef struct testcase_s {
   int smax;
   int k[1001];
   int minf; // min friends to invite
} testcase;

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   // printf("\n");
   int standing = 0;
   for( int i=0; i<=tc.smax; ++i )
   {
      if( standing >= i )
      {
         // printf("i=%d, standing=%d\n", i, standing);
         standing += tc.k[i];
      }
      else
      {
         int missing = i - standing;
         // printf("i=%d, missing=%d\n", i, missing);
         tc.minf += missing;
         standing += missing + tc.k[i];
      }
   }
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   fscanf(fp, "%d ", &tc.smax);
   for( int i=0; i<=tc.smax; ++i )
   {
      int c = fgetc(fp);
      c -= '0';
      tc.k[i] = c;
   }
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   fprintf(fp, "%d", tc.minf);
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
      solve(cases[i]);
      
      fprintf(out, "Case #%d: ", 1 + i);
      writetestcase(cases[i], out);
      fprintf(out, "\n"); 
      fflush(out);
   }
   fclose(out);
}
