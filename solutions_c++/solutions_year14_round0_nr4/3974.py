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
 *  mswin - :w | !cl % & %:r.exe d-example.in
 *
 * where M-example.in could be: [ABCD]-(example|small|large).in
 */

/*
 * store one test case, both problem and solution, no intermediates
 */
typedef struct testcase_s {
   int n;
   double p1b[1000];
   double p2b[1000];
   int dpoints;
   int opoints;
} testcase;

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   /**
   printf("n = %d\n", tc.n);
   for( int i=0; i<tc.n; ++i )
      printf("%lf ", tc.p1b[i]);
   printf("\n");
   for( int i=0; i<tc.n; ++i )
      printf("%lf ", tc.p2b[i]);
   printf("\n");
   /**/

   // player1 = naomi
   // player2 = ken

// there is a unique strategy that Ken can follow to maximize his points 
// without assuming anything about Naomi's strategy, and Ken always uses it. 

   // ken's strategy: pick his weakest winning block?  (isn't very unique)
   // ken must not realize he's being lied to (scale balance match)

   double tblocks[1000];
   for( int i=0; i<tc.n; ++i )
      tblocks[i] = tc.p2b[i];

   // optimal war:  (naomi's order doesn't matter?)
   for( int i=0; i<tc.n; ++i )
   {
      double p1block = tc.p1b[i];
      int p2chosen = -1;
      for( int j=0; j<tc.n; ++j )
      {
         if( tblocks[j] < 0 )  // current entry already burned
         {
         }
         else if( p2chosen < 0 ) // have to choose something.
         {
            p2chosen = j;
         }
         else if( tblocks[p2chosen] > p1block ) // have winner, minimze it.
         {
            if( p1block < tblocks[j] && tblocks[j] < tblocks[p2chosen] )
               p2chosen = j;
         }
         else if( tblocks[p2chosen] == p1block ) // tie, look for win.
         {
            if( tblocks[p2chosen] < tblocks[j] ) // upgrade to win.
               p2chosen = j;
         }
         else if( tblocks[p2chosen] < p1block ) // currently losing
         {
            if( tblocks[j] >= p1block ) // upgrade to win or tie
               p2chosen = j;
            else if( tblocks[p2chosen] > tblocks[j] ) // minimize loss
               p2chosen = j;
         }
      }
      // p2 has chosen.
      tc.opoints += p1block > tblocks[p2chosen];
      tblocks[p2chosen] = -1;
      // printf("p1chosen = %d, p2chosen = %d\n", i, p2chosen);
   }

   double tblocks1[1000];
   for( int i=0; i<tc.n; ++i )
      tblocks1[i] = tc.p1b[i];
   double tblocks2[1000];
   for( int i=0; i<tc.n; ++i )
      tblocks2[i] = tc.p2b[i];

   // decietful war:
   for( int t = 0; t < tc.n; ++t )
   {
      // find ken's highest block, if can beat beat.
      // if can't beat, use lowest block.  claim slightly less
      int p2chosen = -1;
      for( int j=0; j<tc.n; ++j )
      {
         if( tblocks2[j] < 0 )
            continue;
         else if( p2chosen < 0 )
            p2chosen = j;
         else if( tblocks2[j] > tblocks2[p2chosen] )
            p2chosen = j;
      }

      // printf("w2 = %lf, p2chosen = %d\n", tblocks2[p2chosen], p2chosen);

      int p1chosen = -1;
      for( int i=0; i<tc.n; ++i )
      {
         if( tblocks1[i] < 0 )
            ;
         else if( p1chosen < 0 )
            p1chosen = i;
         else if( tblocks1[i] > tblocks2[p2chosen] ) // any winner
            p1chosen = i;
         else if( tblocks1[p1chosen] > tblocks2[p2chosen] ) // any winner
            ;
         else if( tblocks1[i] < tblocks1[p1chosen] ) // lowest loser
            p1chosen = i;
      }

      // both have chosen.
      tc.dpoints += tblocks1[p1chosen] > tblocks2[p2chosen];
      // printf("w1 = %lf, w2 = %lf, p1chosen = %d, p2chosen = %d\n",
      //      tblocks1[p1chosen], tblocks2[p2chosen], p1chosen, p2chosen);
      tblocks1[p1chosen] = -1;
      tblocks2[p2chosen] = -1;
   }
   // printf("deceitful points = %d, optimal points = %d\n", tc.dpoints, tc.opoints);
   // fgetc(stdin);   
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   fscanf(fp, "%d\n", &tc.n);
   for( int i=0; i<tc.n; ++i )
      fscanf(fp, "%lf ", &tc.p1b[i]);
   for( int i=0; i<tc.n; ++i )
      fscanf(fp, "%lf ", &tc.p2b[i]);
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   fprintf(fp, "%d %d", tc.dpoints, tc.opoints);
}

testcase cases[101];

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
