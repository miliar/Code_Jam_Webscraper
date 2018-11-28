#include <iostream>
#include <algorithm>    // std::min

using std::cout;
using std::cin;
using std::endl;
using std::min;

const double DEFAULT_RATE = 2.0f;
double do_test_case()
{
   double C,F,X;
   cin >> C >> F >> X;

   // start time
   double time = 0;
   //default start cookie per/second rate
   double rate = DEFAULT_RATE;
   // time to target
   double t1 = time + X / rate;
   // time to factory and then to target
   double t2 = time + (C / rate) + (X / (rate + F));

   while (t2 < t1)
   {
      t1 = t2;

      time += (C / rate);
      rate += F;

      t2 = time + (C / rate) + (X / (rate + F));

   }

   return t1;
}

int main()
{
   int T = 0;
   cin >> T;

   cout.precision(7);
   for (int test_case = 1; test_case <= T; ++test_case)
   {
      cout << "Case #" << test_case << ": " << std::fixed << (double)do_test_case() << endl;
   }

   return 0;
}
