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
   double c; // cookies to buy farm
   double f; // additional cookies per second per farm
   double x; // cookies needed to win
   double elapsed;
} testcase;

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   double rate = 2;
   double cookies = 0;
   double elapsed = 0;

   while( cookies < tc.x )
   {
      // calculate time to win at current rate:
      double twin = (tc.x - cookies) / rate;
      double fwin = 0;
      if( cookies >= tc.c ) // have option to buy farm.
      {
         double frate = rate + tc.f;
         double fcookies = cookies - tc.c;
         fwin = (tc.x - fcookies) / frate;
         if( fwin < twin )
         {
            rate = frate;
            cookies = fcookies;
         }
      }
      // calculate time to next decision point.
      double tchoice = (tc.c - cookies) / rate;
//      printf("twin = %lf, fwin = %lf, tchoice = %lf, elapsed = %lf\n",
//            twin, fwin, tchoice, elapsed);
//      fgetc(stdin);
      if( twin <= tchoice || tchoice <= 0)
      {
         elapsed += twin;
         break;
      }
      cookies += rate * tchoice;
      elapsed += tchoice;
   }
   tc.elapsed = elapsed;
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   fscanf(fp, "%lf %lf %lf\n", &tc.c, &tc.f, &tc.x);
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   fprintf(fp, "%7.7lf", tc.elapsed);
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
