#include <iostream>
#include <iterator>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>
#include <iomanip>

using namespace std;
typedef vector<int> IntV;

template<typename InputIt, typename Size, typename OutputIt>
OutputIt my_copy_n(InputIt &first /*dirty hack reference - we're adjusting input iterator*/, Size count, OutputIt result)
{
   while (count-- > 0)
   {
      *result++ = *first++;
   }
   return result;
}

template<typename AllLsType>
struct Printer
{
   size_t current;
   const AllLsType &allLs;

   explicit Printer(const AllLsType &i_allLs)
      : current(0U),
        allLs(i_allLs)
   {

   }

   void operator()(const int& i)
   {
      cout << (current ? "\n" : "") << allLs[i - 1];
      ++current;
   }
};

template<typename AllLsType>
Printer<AllLsType> make_printer(const AllLsType& l)
{
   return Printer<AllLsType>(l);
}

int main(int, char*[])
{
   istream_iterator<double> it(cin);
   const unsigned T = (unsigned)*it++;

   for (unsigned k = 1; k <= T; k++)
   {
      const double C = *it++;
      const double F = *it++;
      const double X = *it++;

      double minSeconds = X / 2.0;

      for (unsigned i = 1; i < 10000; ++i)
      {
         double seconds = C / 2.0;

         for (unsigned j = 1; j < i; ++j)
         {
            seconds += C / (2.0 + j * F);
         }

         seconds += X / (2 + i * F);

         if (minSeconds > seconds)
         {
            minSeconds = seconds;
         }
         else
         {
            break;
         }
      }

      cout << "Case #" << k << ": " << setprecision(20) << minSeconds << "\n";

   }

   return 0;
}