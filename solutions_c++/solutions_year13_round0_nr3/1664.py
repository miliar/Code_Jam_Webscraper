#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

std::vector<long long> c;
std::vector<int> d (100);

bool IsPalindrome ( long long x )
{
   int i=0;
   for ( long long xx = x; xx > 0; xx /= 10, ++i )
      d[i] = xx % 10;

   long long y = 0;
   for ( int j=0; j<i; j++ )
   {
      y *= 10;
      y += d[j];
   }

   return x == y;
}

#if 0
long long FairAndSquare ( long long a, long long b )
{
   long long ax = std::sqrt (a), bx = std::sqrt (b) + 1;

   std::cerr << a << ", " << b << std::endl;
   std::cerr << ax << ", " << bx << std::endl;

   long long y = 0;

   for ( long long i=ax; i<=bx; i++ )
   {
      long long ii = i*i;

      if ( ii < a || ii > b ) continue;

      if ( !IsPalindrome (i) ) continue;
      if ( !IsPalindrome (ii) ) continue;

      std::cerr << i << "-" << ii << std::endl;
      ++y;
   }

   return y;
}
#endif

int FairAndSquare ( long long a, long long b )
{
   std::cerr << a << ", " << b << std::endl;

   const size_t n = c.size ();
   int y = 0;

   for ( size_t i=0; i<n; i++ )
   {
      long long cc = c[i]*c[i];

      if ( cc >= a && cc <= b )
      {
         std::cerr << c[i] << " ";
         ++y;
      }
   }
   std::cerr << std::endl;

   return y;
}

void Prepare ()
{
   for ( long long i=1; i<=10000000LL; i++ )
   {
      if ( !IsPalindrome (i) ) continue;
      if ( !IsPalindrome (i*i) ) continue;

      std::cerr << i << "-" << i*i << std::endl;
      c.push_back (i);
   }
}

int main ( int argc, char *argv[] )
{
   if ( argc < 2 )
   {
      std::cerr << "Usage: " << argv[0] << " <test-set>" << std::endl;
      return 1;
   }

   Prepare ();

   std::ifstream is ( argv[1] );
   //char line [256] = { 0 };
   int tests = 0;
   is >> tests;

   for ( int k=0; k<tests; k++ )
   {
      // string
      long long a = 0, b = 0;
      is >> a >> b;
      //is.getline ( line, 255 );

      std::cout << "Case #" << k+1 << ": " << FairAndSquare ( a, b ) << std::endl;
   }
}
