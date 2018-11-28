#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdint.h>
#include <math.h>

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
typedef struct testcase_s
{
   long long a;  // 1 x 10^100 = 1 x 2^512
   long long b;
   long long n;
} testcase;

bool ispalin(long long n)
{
   int count = 0;
   int digits[101] = {0};
   while( n > 0 )
   {
      digits[count] = n % 10;
      ++count;
      n /= 10;
   }
   bool ret = true;
   for( int j = 0; j < count / 2 + 1; ++j )
      if( digits[j] != digits[count - j - 1] )
      {
         ret = false;
         break;
      }
   return ret;
}

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   // printf(".");

   tc.n = 0;
   for( long long i = 1; ; ++i )
   {
      long long n = i * i;

      if( n < tc.a )
         continue;
      if( n > tc.b )
         break;

      if( ispalin(i) && ispalin(n) )
         ++tc.n;
   }
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   fscanf(fp, "%lld %lld ", &tc.a, &tc.b);
//   printf("\n\n%lld %lld", tc.a, tc.b);
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   fprintf(fp, "%lld", tc.n);
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

   testcase arrCases[10000] = {0};
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
