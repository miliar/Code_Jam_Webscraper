#include <iostream>
#include <cstdio>
#include <vector>

int main (void) {

   int n;
   scanf("%d\n", &n);
   long long num;
   
   for (int i = 0; i < n; ++i) {
      scanf("%llu\n", &num);
      std::vector<bool> seen(10);
      int count = 0;
      int iterations = 1;
      while (true) {
         if (num*iterations == 0) {
            std::cout << "Case #" << i+1 << ": INSOMNIA" << std::endl;
            break;
         }
         std::string s = std::to_string((long long) num*iterations);
         for (unsigned int j = 0; j < seen.size(); ++j) {
            if (seen[j] == false) {
               if (s.find(std::to_string(j)) != std::string::npos) {
                  //std::cout << "working" << std::endl;
                  seen[j] = true;
                  count++;
               }
            }
         }
         if (count == 10) {
            std::cout << "Case #" << i+1 << ": " << (long long) num*iterations << std::endl;
            break;
         }
         iterations++;
      }
   }
}
