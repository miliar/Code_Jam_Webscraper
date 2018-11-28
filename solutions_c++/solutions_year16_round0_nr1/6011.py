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

#define SMALL_INPUT_FILE "A-small-attempt0.in"
#define LARGE_INPUT_FILE "A-large.in"
#define OUTPUT_FILE "countsheep-output.txt"
#define MAX_B 1000



bool checkAll(bool arr[10])
{
    for (int i = 0 ;  i < 10 ; ++i)
    {
        if ( arr[i] != true)
            return false;
    }
    return true;
}


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

   int T,i = 1;
   long N,curnum, num;
   bool counted[10];


    fscanf( inpfile , "%d", &T);


   while ( T--)
   {
       fscanf( inpfile , "%ld", &N);


        fill(counted , counted+10 , 0);
       bool done = false;
       for ( curnum = N ;  ; curnum += N)
       {
           // if N==0 INSOMNIA
           if ( curnum == 0 )
               break;

           num = curnum;
           while ( num > 0)
           {
               counted[ num % 10] = true;
               num /= 10;
           }

           if (checkAll(counted))
           {
               done = true;
               break;
           }

       }

       if (done)
       {
           fprintf( outfile , "Case #%d: %ld\n", i++ , curnum);
       }
        else
        {
           fprintf( outfile , "Case #%d: INSOMNIA\n", i++ );
        }


   }




    fclose(inpfile);
    fclose(outfile);

    return 0;
}
