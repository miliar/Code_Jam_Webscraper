#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main()
{
   std::ifstream in("D-large.in");
   std::ofstream out("output.txt");
   int t;
   in >> t;
   for (int q = 1; q <= t; ++q)
   {
      size_t n;
      in >> n;
      std::vector<double> naomi(n);
      for (size_t i = 0; i < n; ++i)
         in >> naomi[i];
      std::vector<double> ken(n);
      for (size_t i = 0; i < n; ++i)
         in >> ken[i];
      std::sort(naomi.begin(), naomi.end());
      std::sort(ken.begin(), ken.end());
      int war_pts = 0;
      std::vector<bool> used(n, false);
      for (size_t i = 0; i < n; ++i)
      {
         bool f = false;
         for (size_t j = 0; j < n; ++j)
         {
            if (!used[j] && ken[j] > naomi[i])
            {
               f = true;
               used[j] = true;
               break;
            }
         }
         if (!f)
            ++war_pts;
      }
      int dwar_pts = 0;
      std::vector<bool> used_naomi(n, false);
      std::vector<bool> used_ken(n, false);
      for (int i = n - 1; i >= 0; --i)
         for (int j = n - 1; j >= 0; --j)
            if (!used_ken[j] && ken[j] < naomi[i] && dwar_pts < n - 1)
            {
               used_ken[j] = true;
               used_naomi[i] = true;
               ++dwar_pts;
               break;
            }
      std::vector<double> new_naomi;
      std::vector<double> new_ken;
      for (size_t i = 0; i < n; ++i)
      {
         if (!used_naomi[i])
            new_naomi.push_back(naomi[i]);
         if (!used_ken[i])
            new_ken.push_back(ken[i]);
      }
      for (size_t i = 0; i < new_naomi.size(); ++i)
         if (new_ken[new_naomi.size() - 1 - i] < new_naomi[i])
            ++dwar_pts;
      out << "Case #" << q << ": " << dwar_pts << " " << war_pts << std::endl;
   }
   return 0;
}

