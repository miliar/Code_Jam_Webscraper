// CodeJam_Lawnmower.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int> IntVect;
typedef vector<IntVect> TwoDimArray;
string answers[2] = {"NO", "YES"};

string processTestCase(const TwoDimArray& testCaseData, int N, int M)
{
   vector<int> horizontalMaximums(N);
   vector<int> verticalMaximums(M);
   for (int i = 0; i < N; ++i)
   {
      horizontalMaximums[i] = *max_element(testCaseData[i].begin(), testCaseData[i].end());
   }
   for (int j = 0; j < M; ++j)
   {
      int verticalMax = 0;
      for (int i = 0; i < N; ++i)
      {
         if (verticalMax < testCaseData[i][j])
            verticalMax = testCaseData[i][j];
      }
      verticalMaximums[j] = verticalMax;
   }
   bool isItPossibleToCutLawn = true;
   for (int i = 0; i < N; ++i)
   {
      for (int j = 0; j < M; ++j)
      {
         isItPossibleToCutLawn &= (testCaseData[i][j] >= horizontalMaximums[i]) ||
                                  (testCaseData[i][j] >= verticalMaximums[j]);
      }
   }
   return answers[isItPossibleToCutLawn];
}

int _tmain(int argc, _TCHAR* argv[])
{
   if (argc != 3)
   {
      cerr << "Usage: CodeJam_Lawnmower inputFileName outputFileName";
      return -1;
   }

   string line;
   fstream inputFile(argv[1], fstream::in);
   fstream outputFile(argv[2], fstream::out);
   getline(inputFile, line);
   int testCasesQty = atoi(line.c_str());
   int testCasesProcessed = 0;
   while (testCasesProcessed != testCasesQty)
   {
      int N = 0, M = 0;
      inputFile >> N >> M;
      TwoDimArray testCaseData(N);
      int Aij = 0;
      for (int i = 0; i < N; ++i)
      {
         for (int j = 0; j < M; ++j)
         {
            inputFile >> Aij;
            testCaseData[i].push_back(Aij);
         }
      }

      outputFile << "Case #" << ++testCasesProcessed << ": " << processTestCase(testCaseData, N, M);

      if (testCasesProcessed != testCasesQty)
         outputFile << '\n';
      else
         break;
   }
   return 0;
}

