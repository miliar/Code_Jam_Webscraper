#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

/* 
 * runme:
 *   g++ -o filename.o filename.cpp
 *   ./filename.o A-example.in
 *
 * runme vim:
 *   :w | !g++ -o %.o % ; ./%.o A-example.in
 *                     && instead ?
 *
 * where A-example.in could be: [ABCD]-(example|small|large).in
 */

/*
 * store one test case, both problem and solution
 */
typedef struct testcase_s {
   int n;
   int m; // input row length
   int lawn[100][100];
   bool possible;
} testcase;

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   tc.possible = true;
   for( int x = 0; x < tc.n; ++x )
   {
      for( int y = 0; y < tc.m; ++y )
      {
         int height = tc.lawn[x][y];

         //scan up/down to check for something higher. 
         bool vpossible = true;
         for( int i=0; i<tc.n; ++i )
            if( tc.lawn[i][y] > height )
               vpossible = false;
         bool hpossible = true;
         for( int i=0; i<tc.m; ++i )
            if( tc.lawn[x][i] > height )
               hpossible = false;
        
         const char *c;
         if( hpossible && vpossible )
            c = "+";
         else if( hpossible )
            c = "-";
         else if( vpossible )
            c = "|";
         else
            c = ".";
         // printf("%s", c);

         if( !hpossible && !vpossible )
         {
            tc.possible = false;
            // return;
         }
      }
      // printf("\n");
   }
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   fscanf(fp, "%d %d ", &tc.n, &tc.m);
   // printf("%d %d\n", tc.n, tc.m);
   for( int i=0; i<tc.n; ++i )
      for( int j=0; j<tc.m; ++j )
         fscanf(fp, "%d ", &tc.lawn[i][j]);
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   if( tc.possible )
      fprintf(fp, "YES");
   else
      fprintf(fp, "NO");
}

/*
 * Process command line argument (input file), read input and write output.
 */
int main(int argc, char **argv)
{
   if( argc != 2 )
   {
      printf("argc != 1\n");
      return 1;
   }

   const char *infilename = argv[1];
   char outfilename[256] = {0};
   const char *endname = strstr(infilename, ".in");
   int namelen = endname == NULL ? strlen(infilename) : endname - infilename;
   if( namelen > sizeof(outfilename) - 5 )
      namelen = sizeof(outfilename) - 5;
   memcpy(outfilename, infilename, namelen);
   strcpy(outfilename + namelen, ".out");

   testcase arrCases[100] = {0};
   int nNumCases;

   FILE *fpInput = fopen(infilename, "r");
   if( NULL == fpInput )
   {
      printf("file '%s' not found\n", infilename);
      return 2;
   }
   try {
      // read in first line.  parse to single int
      char szNumCases[256] = {0};
      if( NULL == fgets(szNumCases, sizeof(szNumCases), fpInput) )
      // if( 1 > fscanf(fpInput, "%d[\n]", &nNumCases) )
      {
         printf("test case count not found at top of file\n");
         throw std::exception();
      }
      nNumCases = atoi(szNumCases);


      for( int iCase = 0; iCase < nNumCases; ++iCase )
      {
         readtestcase(arrCases[iCase], fpInput);
      }
   } catch (std::exception &ex) {
      printf("exception during file read\n");
      fclose(fpInput);
      return 3;
   }
   fclose(fpInput);

   for( int iCase = 0; iCase < nNumCases; ++iCase )
   {
      // solve(arrCases[iCase]);  // solve before writing to output file.
   }

   FILE *fpOutput = fopen(outfilename, "w");
   if( NULL == fpOutput )
   {
      printf("can't write file '%s'\n", outfilename);
      return 4;
   }
   for( int iCase = 0; iCase < nNumCases; ++iCase )
   {
      solve(arrCases[iCase]); // solve as file is written.  
      fprintf(fpOutput, "Case #%d: ", 1 + iCase);
      writetestcase(arrCases[iCase], fpOutput);
      fprintf(fpOutput, "\n"); 
//      fprintf(fpOutput, "Case #%d: %s\n", 1 + iCase, arrCases[iCase].szOut);
      fflush(fpOutput);
   }
   fclose(fpOutput);

   return 0;
}
