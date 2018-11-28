#include <iostream>
#include <fstream>
#include <algorithm>
#include <list>

int count(std::list<int> m, size_t i, int a, int res, bool add, bool rem)
{
   if (i >= m.size() || m.size() == 0)
   {
      return res;
   }
   auto it = m.begin();
   for (size_t j = 0; j < i; ++j)
   {
      it++;
   }
   if (add)
   {
      m.insert(it, a - 1);
      --it;
      ++res;
   }
   if (rem)
   {
      m.erase(it);
      ++res;
   }
   //std::cout << (*it) << "";
   while (i < m.size() && a > (*it))
   {
      a += (*it);
      //std::cout << "*";
      ++it;
      ++i;
   }
   if (i >= m.size())
   {
      return res;
   }
   return std::min(count(m, i, a, res, true, false), count(m, i, a, res, false, true));
   //return 1;
}

int main()
{
   std::ifstream in("A-small-attempt0.in");
   std::ofstream out("res.txt");
   int t;
   in >> t;
   int a;
   std::list<int> m;
   int n;
   int tmp;
   for (int i_t = 1; i_t <= t; ++i_t)
   {
      out << "Case #" << i_t << ": ";
      in >> a >> n;
      m.clear();
      for (int i = 0; i < n; ++i)
      {
         in >> tmp;
         m.push_back(tmp);
      }
      m.sort();
      //std::cout << (*m.begin()) << std::endl;
      if (a == 1)
      {
         out << n << std::endl;
         continue;
      }
      out << count(m, 0, a, 0, false, false) << std::endl;
   }
   return 0;
}
