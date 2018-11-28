#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <bitset>

std::map<std::string, std::vector<int> >answer;

// return divisor
unsigned long long isprime (long long x) {
   if (x % 2 == 0) return 2;
   if (x % 3 == 0) return 3;
   int i = 5;
   while (i * i  <= x) {
      if (x % i == 0) {
         return i;
      }
      if (x % (i + 2) == 0) {
         return (i+2);
      }
      i = i + 6;
   }
   return 1;
}

int main (void) {

   int n;
   scanf("%d\n", &n);
   int length, numJams;
   scanf("%d %d\n", &length, &numJams);
   // produce numJams of jamcoins of length 'length'
   int numProduced = 0;
   std::string s;
   for (int j = 0; j < length; ++j) s += "1";
   unsigned long long max = pow (2, length);
   unsigned long long start = pow(2, length-1) +1;
   while (start != max) {
      std::bitset<32> foo(start);
      //std::cout << "testing: " << foo.to_string() << std::endl;
      std::vector<int> divisors;
      for (int base = 2; base <= 10; ++base) {
         //std::cout << "calculating for base.. " << base << std::endl;
         //std::cout << "oh.. " << std::stoll(foo.to_string(), 0, base) << std::endl;
         unsigned long long result = isprime(std::stoull(foo.to_string(), 0, base));
         if (result == 1) break;
         //if (result == 1) std::cout << "what?" << std::endl;
         divisors.push_back(result);
      }
      if (divisors.size() == 9) {
         answer[foo.to_string()] = divisors;
         numProduced++;
         //std::cout << "produced: " << numProduced << std::endl;
         if (numProduced == numJams) break;
      }
      start += 2;
   }
   
   
   std::cout << "Case #1:\n";
   for (auto it = answer.begin(); it != answer.end(); ++it) {
      std::cout << it->first.substr(it->first.find("1")) << " ";
      for (auto it2 = it->second.begin(); it2 != it->second.end(); ++it2) {
         std::cout << *it2;
         if (it2 != it->second.end()-1) std::cout << " ";
      }
      std::cout << "\n";
   }
}
