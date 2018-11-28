#include <iostream>
#include <fstream>
#include <iomanip>

int main()
{
   std::ifstream in("B-large.in");
   std::ofstream out("output.txt");
   int t;
   in >> t;
   for (int q = 1; q <= t; ++q)
   {
      double c, f, x;
      in >> c >> f >> x;
      double time = 0;
      double speed = 2;
      while (true)
      {
         if (x / speed < c / speed + x / (speed + f))
         {
            out << std::fixed << std::setprecision(8) << "Case #" << q << ": " << time + x / speed << std::endl;
            break;
         }
         time += c / speed;
         speed += f;
      }
   }
   return 0;
}

