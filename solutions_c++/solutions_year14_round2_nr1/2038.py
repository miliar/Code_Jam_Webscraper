// basic file operations
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

#define DEBUG 0
#define trace if( DEBUG ) printf

/*
qsort( device, N, sizeof(uint64_t), compare );
int compare (const void * a, const void * b)
{
  return ( *(uint64_t*)a - *(uint64_t*)b );
}
*/

int calc( string s1, string s2 )
{
   int i1 = 0, i2 = 0, res = 0;
   while( i1 < s1.length() || i2 < s2.length() )
   {
      if( s1[i1] == s2[i2] ) { i1++; i2++; }
      else if( i1 > 0 && s1[i1 - 1] == s2[i2] ) { i2++; res++; }
      else if( i2 > 0 && s1[i1] == s2[i2 - 1] ) { i1++; res++; }
      else { res = -1; break; }
   }
   return res;
}

int main (int argc, char **argv)
{
   if( argc != 2 ) return -1;
   ifstream myfile;
   int ntests;

   myfile.open( argv[1] );
   myfile >> ntests;
   trace( "Ntests = %d\n",  ntests );

   for( int i = 1; i <=  ntests; i++ )
   {
      trace( "-----------\n" );
      trace( "| Test %02d |\n", i );
      trace( "-----------\n" );

      int N;
      myfile >> N;

      string list[100];

      for( int i = 0; i < N; i++ ) { myfile >> list[i]; }
      for( int i = 0; i < N; i++ ) { trace( "%s ", list[i].c_str() ); }
      trace( "\n" );

      int res = -1;
      int total = 0;
      for( int j = 0; j < N; j++ )
      {
         if( i == j ) continue;
         total += calc( list[0], list[j] );
      }
      if( total < res || res == -1 ) res = total;

      if( res == -1 )
      {
         printf( "Case #%d: Fegla Won\n", i );
         continue;
      }

      int index[100];
      for( int i = 0; i < N; i++ ) { index[i] = 0; }

      res = 0;
      while( index[0] < list[0].length() )
      {
         total = 0;

         int l[100]; for( int i = 0; i < N; i++ ) { l[i] = 0; }
         char cur = list[0][ index[0] ];
         for( int i = 0; i < N; i++ )
         {
            while( list[i][ index[i] ] == cur )
            {
               total++;
               l[i]++;
               index[i]++;
            }
         }
         trace( "%c %d ", cur, total );
         double average = double(total) / N;
         trace( "%f ", average );
         average = round( average );

         total = 0;
         for( int i = 0; i < N; i++ ) { total += fabs( l[i] - average ); }
         res += total;
         trace( "%d %d\n", total, res );
      }

      printf( "Case #%d: %d\n", i, res );
   }

   myfile.close();
   return 0;
}
