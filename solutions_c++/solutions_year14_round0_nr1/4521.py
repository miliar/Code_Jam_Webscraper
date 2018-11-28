#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

static const unsigned int NUM_COLUMNS = 4;

void skipRows(ifstream& input, unsigned int numRowsToSkip);

int main()
{
   static const unsigned int NUM_ROWS = 4;
   ifstream input;
   input.open("A-small-attempt0.in");
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
            unsigned int firstAnswer = 0;
            input >> firstAnswer;
            if (!input.good())
            {
               std::cout << "Failed to read first answer" << endl;
            }
            else if ((firstAnswer < 1) ||
                     (firstAnswer > 4))
            {
               std::cout << "Invalid first answer: " << firstAnswer << endl;
            }
            else
            {
               skipRows(input, firstAnswer - 1);
               vector<unsigned int> possibilities;
               for (unsigned int column = 0; column < NUM_COLUMNS; column++)
               {
                  unsigned int possibility = 0;
                  input >> possibility;
                  possibilities.push_back(possibility);
               }
               skipRows(input, NUM_ROWS - firstAnswer);

               unsigned int secondAnswer= 0;
               input >> secondAnswer;
               if (!input.good())
               {
                  std::cout << "Failed to read second answer" << endl;
               }
               else if ((secondAnswer < 1) ||
                        (secondAnswer > 4))
               {
                  std::cout << "Invalid second answer: " << secondAnswer << endl;
               }
               else
               {
                  skipRows(input, secondAnswer - 1);
                  vector<unsigned int> answers;
                  for (unsigned int column = 0; column < NUM_COLUMNS; column++)
                  {
                     unsigned int possibility = 0;
                     input >> possibility;
                     if (find(possibilities.begin(), possibilities.end(), possibility) != possibilities.end())
                     {
                        answers.push_back(possibility);
                     }
                  }
                  skipRows(input, NUM_ROWS - secondAnswer);

                  output << "Case #" << currentTestCaseIndex << ": ";

                  size_t numAnswers = answers.size();
                  if (numAnswers == 0)
                  {
                     output << "Volunteer cheated!";
                  }
                  else if (numAnswers == 1)
                  {
                     output << answers.at(0);
                  }
                  else if (numAnswers > 1)
                  {
                     output << "Bad magician!";
                  }
                  else
                  {
                     std::cout << "Size of answer set was negative?! " << numAnswers << endl;
                  }

                   output << endl;
               }
            }
         }
      }
      output.close();
      input.close();
   }
   return 0;
}

void skipRows(ifstream& input, unsigned int numRowsToSkip)
{
   unsigned int numCardsToSkip = numRowsToSkip * NUM_COLUMNS;
   unsigned int unused;
   for (unsigned int i = 0; i < numCardsToSkip; i++)
   {
      input >> unused;
   }
}
