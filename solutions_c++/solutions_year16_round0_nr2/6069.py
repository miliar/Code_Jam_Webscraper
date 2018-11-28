

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



using namespace std;

#define SMALL_INPUT_FILE "B-small-attempt0.in"
#define LARGE_INPUT_FILE "B-large.in"
#define OUTPUT_FILE "pancakeflip-output.txt"
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

   int T,i = 1 , k;

   char pancakes[101];
   int minmoves;
   fscanf( inpfile , "%d", &T);

   while ( T--)
   {
     minmoves = 0;

     fscanf( inpfile , "%s", pancakes);
     printf( "%s\n" , pancakes);

     if ( pancakes[0] == '-')
        minmoves++;



     for ( int j= 1 ; pancakes[j] != '\0'; j++)
     {

         if ( pancakes[j]=='-' && pancakes[j-1] == '+')
            minmoves+= 2;


     }

     fprintf( outfile , "Case #%d: %d\n", i++ , minmoves);



   }



    fclose(inpfile);
    fclose(outfile);

    return 0;
}

