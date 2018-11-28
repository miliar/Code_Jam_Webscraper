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
 *  mswin - :w | !cl % & %:r.exe b-example.in
 *
 * where M-example.in could be: [ABCD]-(example|small|large).in
 */

/*
 * store one test case, both problem and solution, no intermediates
 */
typedef struct testcase_s {
   int a;
   int b;
   int k;

   int pairs;
} testcase;

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   // randa & randb = winner
   // randa 0 <= randa < a
   // randb 0 <= randb < b
   // buy all answers < k

   // how many possible winners were bought?
  
   // Case #1:
   // 3 4 2 = 10
   /*
   0 & 0 = 0
   1 & 0 = 0
   2 & 0 = 0
   0 & 1 = 0
   1 & 1 = 1
   2 & 1 = 0
   0 & 2 = 0
   1 & 2 = 0
   2 & 2 = 2
   0 & 3 = 0
   1 & 3 = 1
   2 & 3 = 2
   */

   tc.pairs = 0;
   for( unsigned int a = 0; a < tc.a; ++a )
      for(unsigned int b = 0; b < tc.b; ++b )
         if( (a & b) < tc.k )
            ++tc.pairs;
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   fscanf(fp, "%d %d %d\n", &tc.a, &tc.b, &tc.k);
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   fprintf(fp, "%d", tc.pairs);
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
