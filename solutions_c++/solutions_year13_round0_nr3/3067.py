// CodeJam_FairAndSquare.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <xutility>
#include <string>
#include <vector>
#include <complex>
#include <set>
#include <fstream>
#include <iostream>

using namespace std;

//bool isPalindrome(const string& str)
//{
//   return equal(str.begin(), str.begin() + str.size()/2, str.rbegin());
//}
//
//string convertInt(int number)
//{
//   stringstream ss;
//   ss << number;
//   return ss.str();
//}

bool isPalindrome(int orig)
{
   int reversed = 0, n = orig;

   while (n > 0)
   {
      reversed = reversed * 10 + n % 10;
      n /= 10;
   }

   return orig == reversed;
}


set<int> generateListOfPalindromes(int upperLimit)
{
   set<int> palindromes;
   for (int i = 0; i <= upperLimit; ++i)
   {
      if (isPalindrome(i))
         palindromes.insert(i);
   }
   return palindromes;
}

int processTestCase(int A, int B, const set<int>& palindromes)
{
   int fairAndSquareQty = 0;
   for (int i = A; i <= B; ++i)
   {
      if (palindromes.find(i) != palindromes.end())
      {
         double square = pow(i, 0.5);
         if ((int(square) * int(square) == i) && palindromes.find(square) != palindromes.end())
         {
            ++fairAndSquareQty;
         }
      }
   }
   return fairAndSquareQty;
}

int _tmain(int argc, _TCHAR* argv[])
{
   if (argc != 3)
   {
      cerr << "Usage: CodeJam_Lawnmower inputFileName outputFileName";
      return -1;
   }

   set<int> palindromes = generateListOfPalindromes(1000);
   fstream inputFile(argv[1], fstream::in);
   fstream outputFile(argv[2], fstream::out);
   string line;
   getline(inputFile, line);
   int testCasesQty = atoi(line.c_str());
   int testCasesProcessed = 0;
   while (testCasesProcessed != testCasesQty)
   {
      int A = 0, B = 0;
      inputFile >> A >> B;

      outputFile << "Case #" << ++testCasesProcessed << ": " << processTestCase(A,B,palindromes);

      if (testCasesProcessed != testCasesQty)
         outputFile << '\n';
      else
         break;
   }


   return 0;
}

