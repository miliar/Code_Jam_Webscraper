#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>
using namespace std;

int main()
{
   ifstream input;
   input.open("D-large.in");
   ofstream output;
   output.open("output.txt", ios::trunc);

   if (!input.is_open())
   {
      printf("Failed to open input file!\n");
   }
   else if (!output.is_open())
   {
      printf("Failed to open output file!\n");
   }
   else
   {
      output << std::fixed << std::setprecision(7);

      unsigned int numTestCases = 0;
      input >> numTestCases;
      if (!input.good())
      {
         printf("Failed to read number of test cases\n");
      }
      else if ((numTestCases < 1) ||
               (numTestCases > 100))
      {
         printf("Invalid number of test cases: %u\n", numTestCases);
      }
      else
      {
         for (unsigned int currentTestCaseIndex = 1;
              currentTestCaseIndex <= numTestCases;
              currentTestCaseIndex++)
         {
            unsigned int n = 0;
            input >> n;
            if (!input.good())
            {
               std::cout << "Failed to test case parameters" << endl;
            }
            else if ((n < 1) ||
                     (n > 1000))
            {
               std::cout << "Invalid n: " << n << endl;
            }
            else
            {
               vector<double> nBlockMasses; //  kg
               vector<double> kBlockMasses; //  kg
               double mass;
               for (unsigned int i = 0; i < n; i++)
               {
                  input >> mass;
                  nBlockMasses.push_back(mass);
               }
               sort(nBlockMasses.begin(), nBlockMasses.end());

               for (unsigned int i = 0; i < n; i++)
               {
                  input >> mass;
                  kBlockMasses.push_back(mass);
               }
               sort(kBlockMasses.begin(), kBlockMasses.end());

               unsigned int nScoreDeceitful = 0;
               unsigned int kScoreDeceitful = 0;
               vector<double> nBMD = nBlockMasses;
               vector<double> kBMD = kBlockMasses;

               while (!kBMD.empty())
               {
                  double highestK = kBMD.back();
                  kBMD.pop_back();
                  double highestN = nBMD.back();
                  nBMD.pop_back();
                  if (highestK > highestN)
                  {
                     kScoreDeceitful++;
                     nBMD.push_back(highestN);
                  }
                  // else do nothing
               }
               nScoreDeceitful = n - kScoreDeceitful;

               // Normal War
               unsigned int nScoreLegit = 0;
               unsigned int kScoreLegit = 0;
               while (!nBlockMasses.empty())
               {
                  double highestN = nBlockMasses.back();
                  nBlockMasses.pop_back();
                  for (size_t i = 0; i < kBlockMasses.size(); i++)
                  {
                     if (kBlockMasses[i] > highestN)
                     {
                        kScoreLegit++;
                        kBlockMasses[i] = 0.0;
                        break;
                     }
                  }
               }
               nScoreLegit = n - kScoreLegit;

               output << "Case #" << currentTestCaseIndex << ": " << nScoreDeceitful << " " << nScoreLegit << endl;
            }
         }
      }
      output.close();
      input.close();
   }
   return 0;
}
