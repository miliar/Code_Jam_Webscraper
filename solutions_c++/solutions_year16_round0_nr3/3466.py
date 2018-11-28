#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <cstdlib>
#include <math.h>
#include <inttypes.h>

using namespace std;
int64_t divisorUsed = 0;
int64_t* successDivisors = new int64_t[9];

int64_t convertBase (int64_t num, int oldbase, int newbase) {
   int64_t result = 0;
   for (int i = 0; num > 0; i++) {
      result = pow(oldbase, i)*(num % newbase) + result;
      num /= newbase;
   }
   return result;
}

bool isPrime (int64_t num)
{
    if (num <=1)
        return false;
    else if (num == 2)
        return true;
    else if (num % 2 == 0) {
       divisorUsed = 2;
        return false;
    }
    else
    {
        bool prime = true;
        int64_t divisor = 3;
        double num_d = static_cast<double>(num);
        int64_t upperLimit = static_cast<int64_t>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0) {
                divisorUsed = divisor;
                prime = false;
                return false;
            }
            divisor +=2;
        }
        return prime;
    }
}

bool checkJamcoin (int64_t num) {
   int64_t* divisors = new int64_t[9];
   for (int i = 2; i <= 10; i++) {
      if (isPrime(convertBase(num, i, 10)))
         return false;
      divisors[i-2] = divisorUsed;
   }
   successDivisors = divisors;
   return true;
}

int main() {
   string line;
   ifstream iFile("input.txt");
   if (!iFile.is_open()) {
      cout << "Input file not found." << endl;
      return 1;
   }
   getline(iFile, line);
   int numCases = strtol(line.c_str(),0,10);
   for (int i = 0; i < numCases; i++) {
      getline(iFile, line);
      istringstream iss(line);
      vector<string> tokens;
      copy(istream_iterator<string>(iss),
           istream_iterator<string>(),
           back_inserter(tokens));
      int n = strtol(tokens[0].c_str(),0,10);
      int j = strtol(tokens[1].c_str(),0,10);
      cout << "Case #" << i+1 << ":" << endl;
      int numFound = 0;
      int64_t jamcoin = pow(10.0, n-1) + 1;
      while (numFound < j) {
         bool isJamcoin = false;
         while (!isJamcoin) {
            if (jamcoin > pow(10.0, n))
               return 0;
            if (checkJamcoin(jamcoin)) {
               cout << jamcoin << " ";
               for (int i = 0; i < 8; i++) {
                  cout << successDivisors[i] << " ";
               }
               cout << successDivisors[8] << endl;
               isJamcoin = true;
               numFound++;
            }
            jamcoin = convertBase(convertBase(jamcoin, 2, 10) + 2, 10, 2);
         }
      }
   }
   iFile.close();
   return 0;
}