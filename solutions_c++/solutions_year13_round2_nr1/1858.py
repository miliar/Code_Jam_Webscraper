// #include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <set>
#include <stdlib.h>

// using namespace std;

/* 
 * runme:
 *   g++ -o filename.o filename.cpp
 *   ./filename.o M-example.in
 *
 * runme vim:
 *  unix  - :w | !g++ -o %.o % ; ./%.o A-example.in
 *                                              && instead of ; ?
 *  mswin - :w | !cl % & %:r.exe A-example.in
 *
 * where M-example.in could be: [ABCD]-(example|small|large).in
 */

/*
 * store one test case, both problem and solution, no intermediates
 */
typedef struct testcase_s {
   int a;
   int n;
   int o[100];
   int minOps;
} testcase;

int compareint(const void *a, const void *b)
{
   return ( *(int*)a - *(int*)b );
}

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
//   printf("%d %d\n", tc.a, tc.n);

   // a can absorb smaller o, grows by o each time.
   // allowed operations: add a mote, remove a mote
   // what are minimum changes to allow a to absorb all o

   // determine if solveable, find first too-big mote.  
   qsort(tc.o, tc.n, sizeof(int), compareint);
   int moves = 0;
   int a = tc.a;
   for( int i=0; i<tc.n; ++i )
   {
      int o = tc.o[i];
      if( a <= o )
      {
         int removes = tc.n - i;
         int adds = 0;
         if( a <= 1 )
            adds = removes + 1;  // not solveable, a can't absorb.  
         else while( a <= o )
         {
            a += a - 1;
            ++adds;
         }

         // printf("  moves = %d, r=%d,a=%d\n", moves, removes, adds);

         if( removes <= adds )
         {            
            moves += removes;
            break;
         }
         else
         {
            moves += adds;
         }
      }
      a += o;
   }

   tc.minOps = moves > tc.n ? tc.n : moves; // need to "back-track" for remove being better?
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   fscanf(fp, "%d %d ", &tc.a, &tc.n);
   for( int i=0; i<tc.n; ++i )
      fscanf(fp, "%d ", &tc.o[i]);
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   fprintf(fp, "%d", tc.minOps);
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
   testcase cases[t];
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
