#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <map>

int main (void) {
   int t;
   scanf("%d\n", &t);
   std::string s;
   int n;
   for (int i = 0; i < t; ++i) {
      scanf("%d\n", &n);
      //std::vector<std::string> vector;
      std::map<int, int> map;
      int curr;
      for (int j = 0; j < n*2-1;++j) {
         for (int k = 0; k < n; ++k) {
            std::cin >> curr;
            map[curr]++;
         }
      }
      
      std::cout << "Case #" << i+1 << ": ";
      int bla = 0;
      for (auto it = map.begin(); it != map.end(); ++it) {
         if (it->second % 2 == 1) {
            std::cout << it->first;
            bla++;
            if (bla != n) std::cout << " ";
         }
      }
      std::cout << "\n";
   }
}