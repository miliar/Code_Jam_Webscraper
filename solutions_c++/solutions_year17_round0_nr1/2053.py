#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

int OversizedPancakeFlipper ( const string& s, int k )
{
   const size_t n = s.length ();
   vector<int> v;
   v.push_back ( s[0] == '+' ? 0 : 1 );
   for ( size_t i=0; i<n-1; ++i )
      v.push_back ( s[i] == s[i+1] ? 0 : 1 );
   v.push_back ( s[n-1] == '+' ? 0 : 1 );

#if 0
   for ( auto x : v )
      std::cout << x;
   std::cout << std::endl;
#endif

   int y = 0;

   for ( int i=0; i<k; ++i )
   {
      //cout << i << ": ";
      int m0 = 0;
      int m1 = 0;
      for ( size_t j=i; j<v.size(); j+=k )
      {
         //cout << v[j];
         if ( v[j] == 1 )
            ++m1;
         else if ( m1 % 2 == 1 )
            ++m0;
      }
      //cout << ": " << m0 << "," << m1 << endl;

      if ( m1 % 2 == 1 ) return -1;

      y += m0 + m1/2;
   }

   return y;
}

int main ( int argc, char* argv[] )
{
   if ( argc < 2 )
   {
      std::cerr << "usage: " << argv[0] << " <dataset>" << std::endl;
      return 1;
   }

   std::ifstream is ( argv[1] );
   int n;
   is >> n;

   for ( int i = 0; i < n; ++i )
   {
      std::string s;
      int k;
      is >> s >> k;

      int result = OversizedPancakeFlipper ( s, k );

      std::cout << "Case #" << i+1 << ": ";

      if ( result >= 0 )
         std::cout << result;
      else
         std::cout << "IMPOSSIBLE";

      std::cout << std::endl;
   }
}
