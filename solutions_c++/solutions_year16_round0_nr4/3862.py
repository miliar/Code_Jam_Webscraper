

#include <cstdio>      // fscanf,fprintf
#include <cstdlib>     // exit
#include <cerrno>
#include <cstring>     // strncmp,strncpy
#include <ctime>       // clock_t type,clock()
#include <cmath>

#include <iostream>      //
#include <vector>        // vector
#include <algorithm>     // max,min,
#include <numeric>       // accumulate

//MACROS for algorithmic programming

// jamcoins

using namespace std;

#define SMALL_INPUT_FILE "D-small-attempt0.in"
#define LARGE_INPUT_FILE "D-large.in"
#define OUTPUT_FILE "fractiles-output.txt"
#define MAX_B 1000


int main( int argc  , char ** argv )
{
  FILE * inpfile, * outfile ;
  char filename[20] , c;
  clock_t curtime;
  if ( argc == 2)
  {
      if ( strncmp( argv[1] , "small" , 5 ) == 0)
      {
          inpfile = fopen(SMALL_INPUT_FILE , "r");

      }

  }

   else
   {
       c = getchar();
       if ( c == 's')
       {
           strncpy( filename , SMALL_INPUT_FILE , sizeof(filename));
       }
       else
       {
           strncpy( filename , LARGE_INPUT_FILE , sizeof(filename) );
       }

   }



   inpfile = fopen( filename , "r");
   outfile = fopen( OUTPUT_FILE , "w+");

   if ( !inpfile || !outfile )
   {
       perror( "Error: ");
       exit(1);
   }

   int T,i = 1 ;

   unsigned long long positions;
   int K,C,S;

   fscanf( inpfile , "%d", &T);

   while ( T--)
   {
      fscanf( inpfile , "%d %d %d", &K, &C, &S);

      // K = S;
      unsigned long long p = pow( K , C-1);

      positions = 1;
      fprintf( outfile , "Case #%d:" , i++ );
      for ( int k = 1 ; k <= S ; ++k)
      {
           fprintf( outfile , " %I64d" , positions );
           positions += p ;



      }

      fprintf(outfile , "\n");





    }
    fclose(inpfile);
    fclose(outfile);

    return 0;
}

