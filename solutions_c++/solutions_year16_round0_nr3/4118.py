#include <iostream>
#include <typeinfo>
#include <string>
#include <unistd.h>
#include <array>
#include <vector>
#include <sstream>
#include <cassert>
#include <iomanip>
#include <math.h>

using namespace std;

string solveCase(uint64_t n, uint64_t j);

int main()
{
   int count;
   cin >> count;
   assert(count == 1);

   for (int i = 0; i<count; ++i) {
      uint64_t n, j;
      cin >> n >> j;
      string result = solveCase(n, j);
      cout << "Case #" << (i + 1) << ":" << endl << result;
   }

   return 0;
}

void printBinary(ostream &os, uint32_t value)
{
   bool started = false;
   uint32_t mask = 1 << 31;
   while (value != 0) {
      started |= (value & mask);
      if (started)
         os << ((value & mask) ? '1' : '0');
      value = value & ~mask;
      mask = (mask >> 1) | mask;
   }
}

uint64_t getDivisor(uint64_t num)
{
   if (num % 2 == 0) {
      return 2;
   }

   for (int i = 3; i<sqrt(num) + 1 & i < 1000000; i += 2) { // coins are never even .. lol
      if (num % i == 0) {
         return i;
      }
   }
   return 0;
}

uint64_t interpretBinaryAs(uint32_t coin, uint32_t base)
{
   uint64_t result = 0;
   uint64_t power = 1;
   while (coin != 0) {
      result += (coin & 1) * power;
      power = power * base;
      coin = coin >> 1;
   }
   return result;
}

string solveCase(uint64_t n, uint64_t j)
{
   uint32_t coin = (1 << (n - 1)) | 1;
   array<uint64_t, 11> divisors;
   ostringstream result;

   while (j>0) {
      for (int base = 2; base<=10; ++base) {
         uint64_t interpreted = interpretBinaryAs(coin, base);
         divisors[base] = getDivisor(interpreted);
         if (divisors[base] == 0) {
            goto fail;
         }
      }

      printBinary(result, coin);
      for (int base = 2; base<=10; ++base) {
         result << " " << divisors[base];
      }
      result << endl;
      j--;

      fail:
      coin = coin + 2;
   }

   return result.str();
}
