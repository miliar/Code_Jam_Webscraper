#include <iostream>
#include <sstream>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <unordered_map>
#include <fstream>
#include <stdexcept>
#include <limits>
#include <memory> // note: i will use memory leaks, if its easier
#include "BigIntegerProject.cpp"

using namespace std;

BigInteger ten = 10;
BigInteger one = 1;
BigInteger zero = 0;

struct TestCase {
   BigInteger min;
   BigInteger max;
};

bool isBetween(const BigInteger& left, const BigInteger& right, const BigInteger& test) {
   return BigInteger::abscmp(test, left) >= 0 && BigInteger::abscmp(right, test) >= 0;
}

bool isPalindrom(const BigInteger& in) {
   // Not the core problem of this test .. got the idea here:
   // http://stackoverflow.com/questions/199184/how-do-i-check-if-a-number-is-a-palindrome
   BigInteger num = in;
   BigInteger rev = 0;
   while (BigInteger::abscmp(num, zero) != 0)
   {
      BigInteger dig = num % ten;
      rev = rev * ten;
      rev = rev + dig;
      num = num / ten;
   }

   return BigInteger::abscmp(in, rev) == 0;
}

uint64_t countAllPalims(int digits) {

   // Special case
   if(digits % 2 == 0) return 0;
   if(digits == 1) return 3;
   if(digits == 3) return 2;

   uint32_t rootDigits = (digits+1) / 2;
   uint32_t varying = rootDigits / 2 - 1;
   if(rootDigits % 2 == 0) {
      // even
      return (1ull<<varying) + 1ull;
   } else {
      // odd
      return (1ull<<varying) * 2ull + (varying + 1ull) + 2ull;
   }
}

BigInteger minBigInteger(uint32_t digits) {
   BigInteger num;
   string s(digits, '0');
   s[0] = '1';
   istringstream is(s);
   is >> num;
   return num;
}

uint64_t countLimitPalims(int digitToCheck, TestCase& test, const string& minStr, const string& maxStr) {
   int digitsOfMin = minStr.size();
   int digitsOfMax = maxStr.size();

   // Reject simple
   if(digitToCheck % 2 == 0)
      return 0;

   // Brute force small cases
   if(digitToCheck == 1 || digitToCheck == 3) {

      BigInteger min;
      if(digitToCheck == digitsOfMin)
         min = test.min; else
         min = minBigInteger(digitToCheck);

      BigInteger max;
      if(digitToCheck == digitsOfMax)
         max = test.max + one; else
         max = minBigInteger(digitToCheck + 1);

      uint32_t count = 0;

      for(BigInteger i = min; BigInteger::abscmp(i,max) != 0; i = i + one) {
         BigInteger s = i.sqrt();
         if(isPalindrom(i) && isPalindrom(s) && (s*s).abscmp(i) == 0)
            count++;
      }
      return count;
   }

   // Early reject special cases
   if(digitsOfMin != digitsOfMax) {
      if(maxStr[0] >= '5')
         return countAllPalims(digitsOfMax);
      if(maxStr[0] == '2' && maxStr[0] == '3')
         return countAllPalims(digitsOfMax) - (((digitsOfMax+1) / 2 % 2)==0 ? 1 : 2);
   }
   if(digitsOfMin == digitsOfMax) {
      if(maxStr[0] >= '5' && minStr[0] >= '5')
         return 0;
   }

   // Brute force all palindromes between min and max
   BigInteger min;
   if(digitToCheck == digitsOfMin)
      min = test.min; else
      min = minBigInteger(digitToCheck);

   BigInteger max;
   if(digitToCheck == digitsOfMax)
      max = test.max + one; else
      max = minBigInteger(digitToCheck + 1);

   uint32_t count = 0;
   for(BigInteger i = min; BigInteger::abscmp(i,max) != 0; i = i + one) {
      BigInteger s = i.sqrt();
      if(isPalindrom(i) && isPalindrom(s) && (s*s).abscmp(i) == 0)
         count++;
   }

   return count;
}

int main(int argc, char** argv) {
   // Read input
   if(argc != 2)
      throw invalid_argument("no input: ./a.out [filename]");
   string str(argv[1]);
   ifstream in(str);
   if(!in.good() || !in.is_open())
      throw invalid_argument("file not found");

   int numCases;
   in >> numCases;

   vector<TestCase> tests;

   for(int c=1; c<=numCases; c++) {
      TestCase test;

      string minStr;
      in >> minStr;
      string maxStr;
      in >> maxStr;

      ostringstream os;
      os << minStr << " " << maxStr;
      istringstream in2(os.str());
      in2 >> test.min >> test.max;

      int minDigits = minStr.size();
      int maxDigits = maxStr.size();

      uint64_t count = 0;
      if(BigInteger::abscmp(test.min, zero) == 0)
         count = 1;

      count += countLimitPalims(minDigits, test, minStr, maxStr);

      for(int i=minDigits + 1; i<maxDigits; i++)
         count += countAllPalims(i);

      if(minDigits != maxDigits)
         count += countLimitPalims(maxDigits, test, minStr, maxStr);

      cout << "Case #" << c << ": " << count << endl;
   }

   return 0;
}
