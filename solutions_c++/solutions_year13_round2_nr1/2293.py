#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iterator>
using namespace std;

int main()
{
   freopen("a1.in", "r", stdin);
   freopen("a1.out", "w", stdout);

   int t2;
   cin >> t2;
   for (int t1 = 1; t1 <= t2; ++t1) {
      std::cout << "Case #" << t1 << ": ";
      int A, N;
      cin >> A >> N;
      std::vector<int> moteSizes;
      for (int i = 0; i < N; ++i)
      {
         int moteSize;
         cin >> moteSize;
         moteSizes.push_back(moteSize);
      }
      std::sort(moteSizes.begin(), moteSizes.end());
      std::vector<int> notEatenMotes;
      int answer = 0;
      while (true)
      {
         if (A == 1)
         {
            answer = moteSizes.size();
            break;
         }
         bool wasEatenAny = false;
         for (vector<int>::iterator iter = moteSizes.begin(); iter != moteSizes.end(); ++iter)
         {
            if (A > *iter)
            {
               wasEatenAny = true;
               A+= *iter;
            }
            else
            {
               std::copy(iter, moteSizes.end(), back_inserter(notEatenMotes));
               break;
            }
         }
         if (notEatenMotes.empty())
         {
            break;
         }

         if (!wasEatenAny)
         {
            int q = int(double(log(double(notEatenMotes.front() - 1)/(A - 1))) / log(2.0)) + 1;
            if (q < notEatenMotes.size())
            {
               answer += q;
               A = int(pow(2.0, q) * A - pow(2.0,q) + 1);
            }
            else
            {
               answer += notEatenMotes.size();
               break;
            }
         }
         moteSizes = notEatenMotes;
         notEatenMotes.clear();
      }
      if (t1 != t2)
         cout << answer << std::endl;
      else
         cout << answer;
   }

   return 0;
}
