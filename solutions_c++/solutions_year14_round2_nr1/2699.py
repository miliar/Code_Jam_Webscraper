#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>
#include <math.h>
using namespace std;

struct num_letters
{
   char letter;
   unsigned int numRepetitions;
};


void splitLetterString(const string& str, vector<num_letters>& letterTally)
{
   if (!str.empty())
   {
      unsigned int numLettersIndex = 0;
      num_letters nl;
      nl.letter = str[0];
      nl.numRepetitions = 1;
      letterTally.push_back(nl);
      for (unsigned int i = 1; i < str.size(); i ++)
      {
         char curChar = str[i];
         if (curChar == letterTally[numLettersIndex].letter)
         {
            letterTally[numLettersIndex].numRepetitions++;
         }
         else
         {
            num_letters nl;
            nl.letter = curChar;
            nl.numRepetitions = 1;
            letterTally.push_back(nl);
            numLettersIndex++;
         }
      }
   }
}
void print(const vector<num_letters>& letterTally)
{
   for (unsigned int i = 0; i  < letterTally.size(); i++)
   {
      cout << "(" << letterTally[i].letter << "," << letterTally[i].numRepetitions << ")";
   }
}

int main()
{
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
               std::cout << "Failed to read test case parameters" << endl;
            }
            else if ((n < 1) ||
                     (n > 10))
            {
               std::cout << "Invalid n: " << n << endl;
            }
            else
            {
               bool feglaWon = false;
               char c;
               input.read( &c, 1); // Read off the new line from the last input >>
               vector<vector<num_letters> > letterLists;
               for (unsigned int i = 0; i < n; i++)
               {
                  string str;
                  input >> str;
                  vector<num_letters> splitString;
                  splitLetterString(str, splitString);
                  letterLists.push_back(splitString);
                  print(splitString);
                  std::cout << " " << str << " ";
               }
               std::cout << endl;

               unsigned int numLetters = letterLists[0].size();
               for (unsigned int i = 1; i < letterLists.size(); i++)
               {
                  if (letterLists[i].size() != numLetters)
                  {
                     feglaWon = true;
                     break;
                  }
               }

               unsigned int numActions = 0;
               for (unsigned int i = 0; !feglaWon && (i < letterLists[0].size()); i++)
               {
                  num_letters curLetter = letterLists[0][i];
                  unsigned int totalrepetitions = curLetter.numRepetitions;
                  for (unsigned int j = 1; j < letterLists.size(); j++)
                  {
                     if (curLetter.letter != letterLists[j][i].letter)
                     {
                        feglaWon = true;
                        break;
                     }
                     else
                     {
                        totalrepetitions += letterLists[j][i].numRepetitions;
                     }
                  }
                  unsigned int averageRepetitions = totalrepetitions / letterLists.size();
                  numActions += (averageRepetitions > curLetter.numRepetitions) ? (averageRepetitions - curLetter.numRepetitions) : (curLetter.numRepetitions - averageRepetitions);
                  for (unsigned int j = 1; !feglaWon && (j < letterLists.size()); j++)
                  {
                     numActions += (averageRepetitions > letterLists[j][i].numRepetitions) ? (averageRepetitions - letterLists[j][i].numRepetitions) : (letterLists[j][i].numRepetitions - averageRepetitions);
                  }
               }

               if (feglaWon)
               {
                  cout << "Case #" << currentTestCaseIndex << ": Fegla Won" << endl;
                  output << "Case #" << currentTestCaseIndex << ": Fegla Won" << endl;

               }
               else
               {
                  cout << "Case #" << currentTestCaseIndex << ": " << numActions << endl;
                  output << "Case #" << currentTestCaseIndex << ": " << numActions << endl;
               }
            }
         }
      }
      output.close();
      input.close();
   }
   return 0;
}

