// basic file operations
#include <iostream>
#include <fstream>
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

      int A, B, K;
      myfile >> A >> B >> K;
      trace( "%d %d %d\n", A, B, K );

      int res = 0;
      for( int i = 0; i < A; i++ )
         for( int j = 0; j < B; j++ )
         {
            trace( "\t%d %d %d\n", i, j, i & j );
            if( (i & j) < K ) res++;
         }

      printf( "Case #%d: %d\n", i, res );
   }

   myfile.close();
   return 0;
}
