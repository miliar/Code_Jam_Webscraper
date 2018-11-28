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
   int x;
   int r;
   int c;
   bool rwin;
} testcase;

char shapes3[2][4][4] =
{
  {
   "xxx",
   "   ",
   "   ",
  },
  {
   "xx ",
   "x  ",
   "   ",
  },
};

char shapes4[5][5][5] =
{
  {
   "xxxx",
   "    ",
   "    ",
   "    ",
  },
  {
   "xxx ",
   "x   ",
   "    ",
   "    ",
  },
  {
   "xxx ",
   " x  ",
   "    ",
   "    ",
  },
  {
   "xx  ",
   "xx  ",
   "    ",
   "    ",
  },
  {
   "xx  ",
   " xx ",
   "    ",
   "    ",
  },
};

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   tc.rwin = false;

   if( (tc.r * tc.c) % tc.x != 0 )
      tc.rwin = true;

   int min = tc.c < tc.r ? tc.c : tc.r;
   int max = tc.c > tc.r ? tc.c : tc.r;

   if( (tc.x + 1) / 2 > min )
      tc.rwin = true;

   if( tc.x >= 7 )
      tc.rwin = true;

   if( min == 2 && max == 4 && tc.r == 3 )
      tc.rwin = true;

   if( tc.x == 3 )
   {
   }
   if( tc.x == 4 )
   {
      if( min == 2 )
      {
         if( max == 2 )
            tc.rwin = true;
         if( max == 4 )
            tc.rwin = true;
      }
   }
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   fscanf(fp, "%d %d %d\n", &tc.x, &tc.r, &tc.c);
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   fprintf(fp, "%s", tc.rwin ? "RICHARD" : "GABRIEL");
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
