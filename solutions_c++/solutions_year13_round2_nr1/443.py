#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void osmos(int& a, std::vector<int>& ms)
{
   while (!ms.empty())
   {
      int m = ms.back();
      if (m >= a)
         break;
      a += m;
      ms.pop_back();
   }
}

int numToRemove(int numToAdd, int a, std::vector<int> ms) // Yes, copy the vector
{
   sort(ms.begin(), ms.end(), greater<int>());
   osmos(a, ms);
   for (int i = 0; i < numToAdd; ++i)
   {
      a += a-1;
      osmos(a, ms);
      if (ms.empty())
         return 0;
   }
   // Now, the rest has to be removed.
   return (int)ms.size();
}

int main()
{
   int T;
   cin >> T;
   for (int t = 0; t < T; ++t)
   {
      int a, n;
      cin >> a >> n;
      std::vector<int> ms(n);
      for (int i = 0; i < n; ++i)
         cin >> ms[i];
      sort(ms.begin(), ms.end(), greater<int>());
      osmos(a, ms);
      int ret = 123;
      for (int i = 0; i < ret; ++i)
      {
         int subret = numToRemove(i, a, ms);
         subret += i;
         if (subret < ret)
            ret = subret;
      }
      cout << "Case #" << (t+1) << ": " << ret << endl;
   }
   return 0;
}
