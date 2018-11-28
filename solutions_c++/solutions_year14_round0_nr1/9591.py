#include <iostream>
#include <iterator>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>

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
   istream_iterator<int> it(cin);
   const size_t N = *it++;

   for (size_t k = 1; k <= N; ++k)
   {
      int line1 = *it++ - 1;

      IntV A;
      A.reserve(4);

      for (size_t i = 0; i < 4; ++i)
      {
         for (size_t j = 0; j < 4; ++j)
         {
            size_t currentA = *it++;
            if (i == line1)
            {
               A.push_back(currentA);
            }
         }
      }

      IntV B;
      B.reserve(4);

      line1 = *it++ - 1;

      for (size_t i = 0; i < 4; ++i)
      {
         for (size_t j = 0; j < 4; ++j)
         {
            size_t currentA = *it++;
            if (i == line1)
            {
               B.push_back(currentA);
            }
         }
      }
      
      sort(A.begin(), A.end());
      sort(B.begin(), B.end());

      IntV R;
      set_intersection(A.begin(),A.end(),B.begin(),B.end(),back_inserter(R));

      if (R.size() == 1)
      {
         cout << "Case #" << k <<": " << R[0] << "\n";
      } else if (R.size() == 0)
      {
         cout << "Case #" << k <<": Volunteer cheated!\n";
      }
      else
      {     
         cout << "Case #" << k <<": Bad magician!\n";
      }
   }

   return 0;
}