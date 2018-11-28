// basic file operations
#include <iostream>
#include <fstream>
using namespace std;

#define DEBUG 0
#define trace if( DEBUG ) printf

int main (int argc, char **argv) {
   if( argc != 2 ) return -1;
   ifstream myfile;
   int ntests;

   myfile.open( argv[1] );
   myfile >> ntests;
   trace( "Ntests = %d\n",  ntests );

   for( int i = 1; i <=  ntests; i++ ) {
      trace( "-----------\n" );
      trace( "| Test %02d |\n", i );
      trace( "-----------\n" );

      double c, f, x;
      myfile >> c >> f >> x;
      trace( "%lf %lf %lf\n", c, f, x );

      double prod = 2.0;
      double total = 0;

      double cur = x / prod;
      double future = (c / prod) + x / (prod + f);
      while( cur > future)
      {
         total += c / prod;
         prod += f;

         cur = x / prod;
         future = (c / prod) + x / (prod + f);
      }

      total += x / prod;
//      cout << "Case #" << i << ": " << total << "\n";
      printf( "Case #%d: %.7lf\n", i, total );
   }

   myfile.close();
   return 0;
}
