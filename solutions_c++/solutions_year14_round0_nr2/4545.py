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
   input.open("B-large.in");
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
            double c = 0.0;
            double f = 0.0;
            double x = 0.0;
            input >> c;
            input >> f;
            input >> x;
            if (!input.good())
            {
               std::cout << "Failed to test case parameters" << endl;
            }
            else if ((c < 1.0) ||
                     (c > 10000.0))
            {
               std::cout << "Invalid c: " << c << endl;
            }
            else if ((f < 1.0) ||
                     (f > 100.0))
            {
               std::cout << "Invalid f: " << f << endl;
            }
            else if ((x < 1.0) ||
                     (x > 100000.0))
            {
               std::cout << "Invalid x: " << x << endl;
            }
            else
            {
               double timeSpentBuildingFarms = 0.0;
               double rate = 2.0; // Cookies per second
               double timeToMakeXCookies = x / rate;
               double timeToMakeAnotherFarm = c / rate;
               double timeToMakeAnotherFarmPlusXCookies = (timeToMakeAnotherFarm + (x / (rate + f)));
               while (timeToMakeXCookies > timeToMakeAnotherFarmPlusXCookies)
               {
                  // Make another farm
                  rate += f;
                  timeSpentBuildingFarms += timeToMakeAnotherFarm;

                  // Update projection
                  timeToMakeXCookies = x / rate;
                  timeToMakeAnotherFarm = c / rate;
                  timeToMakeAnotherFarmPlusXCookies = (timeToMakeAnotherFarm + (x / (rate + f)));
               }
               output << "Case #" << currentTestCaseIndex << ": " << (timeToMakeXCookies + timeSpentBuildingFarms) << endl;
            }
         }
      }
      output.close();
      input.close();
   }
   return 0;
}
