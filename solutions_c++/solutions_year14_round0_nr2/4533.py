#include <set>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

std::string answer() {
   double C, F, X;
   std::cin >> C >> F >> X;
   double minTime, goalTime = X/2, curTime = 0;
   int farms = 0;
   do {
      minTime = curTime + goalTime;

      curTime += C/(farms*F+2);
      farms++;
      goalTime = X/(farms*F+2);
   } while (curTime + goalTime < minTime);
   return std::to_string(minTime);
}

int main() {
   int cases;
   std::cin >> cases;
   for (int i = 1; i <= cases; i++) {
      printf("Case #%d: %s\n", i, answer().c_str());
   }
}
