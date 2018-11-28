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
 *  mswin - :w | !cl % & %:r.exe M-example.in
 *
 * where M-example.in could be: [ABCD]-(example|small|large).in
 */

/*
 * store one test case, both problem and solution, no intermediates
 */
typedef struct testcase_s {
   int od;
   int d;
   int hist[1001];
   int m;
} testcase;

/*
 * Process one test case, read input and fill in output within struct.
 *
int rsolve(testcase &tc, int maxt)
{
   int mint = 1;

   // based on max, faster to eat or faster to split?
   int maxi = -1;
   for( int i=0; i<tc.d; ++i )
      if( mint < tc.p[i] )
      {
         mint = tc.p[i];
         maxi = i;
      }
   if( mint == 1 )
      return 1;

   if( maxt == 1 )
      return 1001;

   // all best splits?
   int i = maxi;
      for( int j = 1; j <= tc.p[i] / 2; ++j )
      {
         int m = tc.p[i] - j;
         tc.p[tc.d] = m;
         tc.p[i] = j;
         tc.d += 1;
         // printf(">i=%d, j=%d, tc.d=%d\n", i, j, tc.d);
         int t = rsolve(tc, maxt - 1) + 1;
         int ot = t + tc.d - tc.od;
         // printf("<i=%d, j=%d, tc.d=%d ot=%d,\n", i, j, tc.d, ot);
         if(mint > t)
            mint = t;
         tc.d -= 1;
         tc.p[i] = j + m;
         tc.p[tc.d] = 0;
      }

   return mint;
}
/**/

void solve(testcase &tc)
{
   int sum = 0;
   int max = 0;
   for( int i=1; i <= 1000; ++i )
   {
      sum += i * tc.hist[i];
      if( tc.hist[i] > 0 )
         max = i;
   }

   tc.m = max;
   for( int i=2; i <= 1000; ++i )
   {
      // can we get i pancakes on all plates? what does it cost?
      int cost = 0;
      for( int j = max; j > i; --j )
      {
         if( tc.hist[j] == 0 )
            continue;
         int factor = ceil( (double)j / i );
         cost += tc.hist[j] * (factor - 1);
//         printf("i=%d,j=%d,factor=%d,cost=%d\n", i, j, factor, cost);
      }
      if( cost + i < tc.m )
         tc.m = cost + i;
   }
//   printf("\n");
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   int p;
   for(int i=0; i < 1001; ++i )
      tc.hist[i] = 0;

   fscanf(fp, "%d\n", &tc.d);
   for(int i=0; i<tc.d; ++i )
   {
      fscanf(fp, "%d ", &p);
      tc.hist[p] += 1;
   }
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   fprintf(fp, "%d", tc.m);
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
