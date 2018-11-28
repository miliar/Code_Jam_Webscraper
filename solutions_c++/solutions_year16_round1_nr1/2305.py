#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

int main (void) {
   int t;
   scanf("%d\n", &t);
   char c;
   //std::vector<std::string> vector(1);
   for (int i = 0; i < t; ++i) {
      std::vector<std::string> vector(1);
      scanf("%c", &c);
      while (c != '\n') {
         std::vector<std::string> toAdd;
         for (auto it = vector.begin(); it != vector.end(); ++it) {
            toAdd.push_back(*it + c);
            toAdd.push_back(c + *it);
            vector.erase(it--);
         }
         vector.insert(vector.end(), toAdd.begin(), toAdd.end());
         scanf("%c", &c);
      }
      std::sort(vector.begin(), vector.end());
      std::cout << "Case #" << i+1 << ": " << *(vector.end()-1) << std::endl;
   }
}