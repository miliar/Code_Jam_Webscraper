#include <iostream>

using std::cin;      using std::cout;


int main()
{
   unsigned long long r, t, ink, rings;
   int T, c = 1;

   cin >> T;

   while( c <= T )
   {
      cin >> r;
      cin >> t;

      rings = 0;
      for( unsigned long long i = 1; ; i += 4 )
      {
         ink = 2 * r + i;  //mm of ink for next circle

         if( ink > t )
            break;

         ++rings;
         t -= ink;
      }

      cout << "Case #" << c << ": " << rings << std::endl;
      ++c;
   }

return 0;
}
