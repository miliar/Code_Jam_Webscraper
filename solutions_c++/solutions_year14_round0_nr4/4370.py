#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <iterator>

std::string answer() {
   int n, a = 0, b = 0;
   double tmp;
   std::cin >> n;
   std::vector<double> naomi, ken;
   for (int i = 0; i < n; i++) {
      std::cin >> tmp;
      naomi.push_back(tmp);
   }
   for (int i = 0; i < n; i++) {
      std::cin >> tmp;
      ken.push_back(tmp);
   }
   std::sort(naomi.begin(), naomi.end());
   std::sort(ken.begin(), ken.end());

   // Regular war
   for (int i = 0, k = 0; k < n; k++) {
      if (naomi[i] > ken[k]) {
         b++;
      } else {
         i++;
      }
   }

   // Decitful war
   for (int i = 0, k = 0; k < n; k++) {
      if (ken[i] < naomi[k]) {
         a++;
         i++;
      }
   }

   return std::to_string(a)+" "+std::to_string(b);
}

int main() {
   int cases;
   std::cin >> cases;
   for (int i = 1; i <= cases; i++) {
      printf("Case #%d: %s\n", i, answer().c_str());
   }
}
