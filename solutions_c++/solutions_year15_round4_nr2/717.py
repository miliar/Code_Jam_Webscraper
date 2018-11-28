#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

double solve ( double r0, double r1, double c0, double c1, double t, double v )
{
   double v1overv0 = ( t -  c0 ) / ( c1 - t );

   double v0 = v / (1 + v1overv0);
   double v1 = v - v0;

   double t0 = v0 / r0;
   double t1 = v1 / r1;

   if ( t0 > t1 )
      return t0;
   else
      return t1;
}

int main()
{
   std::ifstream in ("two.in", std::ifstream::in);
   std::ofstream out ("two.out", std::ofstream::out);

   out.precision(12);
   out << std::fixed;
   long count;

   in >> count;
   for (long i = 1; i <= count; ++i) {
      int n;
      double r0, r1, c0, c1, t, v;
      in >> n >> v >> t;

      if ( n == 1 ) {
         in >> r0 >> c0;

         if (c0 - t > 0.00001)
            out << "Case #" << i << ": IMPOSSIBLE" << endl;
         else
            out << "Case #" << i << ": " << ( v / r0 ) << endl;
      } else {
         in >> r0 >> c0 >> r1 >> c1;
         if ( std::abs(c0 - t) < 0.00001 && std::abs(c1 - t) < 0.00001) {
            double r = r0 + r1;
            out << "Case #" << i << ": " << ( v / r ) << endl;
         } else if ( std::abs(c0 - t) < 0.00001 ) {
            out << "Case #" << i << ": " << ( v / r0 ) << endl;
         } else if ( std::abs(c1 - t) < 0.00001 ) {
            out << "Case #" << i << ": " << ( v / r1 ) << endl;
         } else if (( c0 >= t && c1 >= t ) || ( c0 <= t && c1 <= t ))
            out << "Case #" << i << ": IMPOSSIBLE" << endl;
         else {
            double r = solve( r0, r1, c0, c1, t, v );
            out << "Case #" << i << ": " << r << endl;
         }
      }
   }
   return 0;
}
