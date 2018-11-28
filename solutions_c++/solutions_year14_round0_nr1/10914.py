#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;


void read_row( set<int> & row_values, int chosen_row )
{
   for ( int row = 1; row <=4; ++row )
   {
      for ( int col = 1; col <= 4; ++col )
      {
         int aux;
         scanf( "%d", &aux );
         
         if ( row == chosen_row )
         {
            row_values.insert( aux );
         }
      }
   }   
}

int main()
{
   int nbCases;
   
   scanf( "%d", &nbCases );
   
   for ( int caseNb = 1; caseNb <= nbCases; ++caseNb )
   {
      int first;
      scanf( "%d", &first );
      
      set<int> first_row;
      read_row( first_row, first );
      
      int second;
      scanf( "%d", &second );
      
      set<int> second_row;
      read_row( second_row, second );
 
      vector<int> inter(8);
      vector<int>::iterator it = set_intersection( first_row.begin(), first_row.end(), 
                                                   second_row.begin(), second_row.end(),
                                                   inter.begin() );
      int size_inter = it - inter.begin();
      
      printf( "Case #%d: ", caseNb );
      
      if ( size_inter == 0 )
      {
         printf( "Volunteer cheated!" );
      }
      else if ( size_inter == 1 )
      {
         printf( "%d", inter[0] );
      }
      else
      {
         printf( "Bad magician!" );
      }
      
      printf( "\n" );
   }
   
   return 0;
}
