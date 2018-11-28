#include <set>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

std::string answer() {
   int pick, a,b,c,d;
   std::set<int> s1, s2;
   char buffer[4];

   std::cin >> pick;
   for (int i = 1; i <= 4; i++) {
      std::cin >> a >> b >> c >> d;
      if (i == pick) {
         s1 = {a,b,c,d};
      }
   }

   std::cin >> pick;
   for (int i = 1; i <= 4; i++) {
      std::cin >> a >> b >> c >> d;
      if (i == pick) {
         for (int ch : {a,b,c,d}) {
            if (s1.count(ch) >= 1) {
               s2.insert(ch);
            }
         }
      }
   }
   if (s2.size() > 1) {
      return "Bad magician!";
   } else if (s2.size() < 1) {
      return "Volunteer cheated!";
   } else {
      return std::to_string(*s2.begin());
   }
}

int main() {
   int cases;
   std::cin >> cases;
   for (int i = 1; i <= cases; i++) {
      printf("Case #%d: %s\n", i, answer().c_str());
   }
}

