#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <array>
#include <algorithm>

bool inVector( std::vector<int>& a, int n )
{
   for ( int x : a ) {
      if ( x == n )
         return true;
   }
   return false;
}

void dupeInts( std::vector<int>& a, std::vector<int>& b, std::vector<int>& c )
{
   c.push_back( 0 );

   for ( int x : a ) {
      if ( inVector( b, x ) ) {
         c[0]++;
         c.push_back( x );
      }
   }
}


int _tmain(int argc, _TCHAR* argv[])
{
   int testCases = 0;
   std::vector<std::array<int,2>> answers;
   std::vector< std::vector<int> > cards;

   int tcase = 0;
   int round = 0;
   int n = 0;

   std::string line;

   std::ifstream infile( "jam1.txt" );

   if ( infile.is_open() ) {
      while ( std::getline( infile, line ) ) {
         if ( testCases == 0 ) {
            testCases = strtoul( line.c_str(), NULL, 10 );

            if ( testCases < 0 || testCases > 100 )
               return 1;

            for ( int i = 0; i < testCases; i++ )
               answers.push_back( std::array<int, 2>() );

            continue;

         } else if ( ((answers[tcase][0] == 0 && round == 0) || (answers[tcase][1] == 0 && round == 1)) && (n == 0 || n == 5) ) {
               
            answers[tcase][round] = strtoul( line.c_str(), NULL, 10 );

            if ( answers[tcase][round] > 4 || answers[tcase][round] == 0 )
               return 1;

            if ( n == 0 || n == 5 )
               n = 1;

            round++;

            continue;

         } else if ( n < 5 && answers[tcase][round-1] != 0) {
            std::istringstream is( line );
            cards.push_back( std::vector<int>( std::istream_iterator<int>( is ), std::istream_iterator<int>() ) );
            n++;
         }
         
         if (round == 2 && n == 5) {
            std::vector<int> d;
            dupeInts( cards[tcase*4*2+answers[tcase][0]-1], cards[tcase*4*2+answers[tcase][1]-1+4], d );

            if ( d[0] == 1 )
               std::cout << "Case #" << tcase + 1 << ": " << d[1] << std::endl;
            else if ( d[0] > 1 )
               std::cout << "Case #" << tcase + 1 << ": " << "Bad magician!" << std::endl;
            else if ( d[0] == 0 )
               std::cout << "Case #" << tcase + 1 << ": " << "Volunteer cheated!" << std::endl;
            else
               std::cout << d[0] << " " << d.size();


            n = 0;
            round = 0;
            tcase++;
            continue;
         }
      }
      infile.close();
   }

	return 0;
}
