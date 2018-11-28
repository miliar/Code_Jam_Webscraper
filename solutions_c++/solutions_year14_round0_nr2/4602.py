#include <iostream>
#include <iomanip>

using namespace std;

double solve( double c, double f, double x )
{
   double sum = 0;
   double rate = 2;
   while (true) {
      double just_wait = x / rate;
      double til_farm = c / rate;
      double buy_one = til_farm + (x / (rate + f));

      if (buy_one > just_wait)
         return just_wait + sum;
      else {
         rate = rate + f;
         sum += til_farm;
      }
   }
}

int main()
{
   int games;
   cin >> games;
   int num = 1;
   cout << fixed << setprecision(7);
   while (num <= games) {
      double c, f, x;
      cin >> c >> f >> x;

      cout << "Case #" << num << ": " << solve( c, f, x ) << endl;
      
      ++num;
   }
   return 0;
}

