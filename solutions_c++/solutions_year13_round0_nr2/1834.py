#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::string Lawnmower ( const std::vector<std::vector<int> > &heights )
{
   const size_t n = heights.size ();
   const size_t m = heights[0].size ();

   std::cerr << n << "," << m << std::endl;

   for ( size_t i=0; i<n; i++ )
   {
      for ( size_t j=0; j<m; j++ )
         std::cerr << heights[i][j] << " ";
      std::cerr << std::endl;
   }

   std::vector<int> ax (n), bx (m);

   for ( size_t i=0; i<n; i++ )
   {
      for ( size_t j=0; j<m; j++ )
         ax[i] = std::max ( ax[i], heights[i][j] );

      std::cerr << ax[i] << " ";
   }
   std::cerr << std::endl;

   for ( size_t j=0; j<m; j++ )
   {
      for ( size_t i=0; i<n; i++ )
         bx[j] = std::max ( bx[j], heights[i][j] );

      std::cerr << bx[j] << " ";
   }
   std::cerr << std::endl;

   for ( size_t i=0; i<n; i++ )
      for ( size_t j=0; j<m; j++ )
      {
         if ( heights[i][j] >= ax[i] )
            continue;

         if ( heights[i][j] >= bx[j] )
            continue;

         return "NO";
      }

   return "YES";
}

int main ( int argc, char *argv[] )
{
   if ( argc < 2 )
   {
      std::cerr << "Usage: " << argv[0] << " <test-set>" << std::endl;
      return 1;
   }

   std::ifstream is ( argv[1] );
   //char line [256] = { 0 };
   int tests = 0;
   is >> tests;

   for ( int k=0; k<tests; k++ )
   {
      int n = 0, m = 0;
      is >> n >> m;
      //is.getline ( line, 255 );

      std::vector<std::vector<int> > v (n);

      for ( int i=0; i<n; i++ )
      {
         v[i].resize (m);

         for ( int j=0; j<m; j++ )
            is >> v[i][j];
      }

      std::cout << "Case #" << k+1 << ": " << Lawnmower ( v ) << std::endl;
   }
}
