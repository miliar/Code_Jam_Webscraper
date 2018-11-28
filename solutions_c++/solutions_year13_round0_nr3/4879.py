// Google Codejam 2013 Qualification
// C. Fair and Square
// Author: Paul Cuthbert

#include <iostream>
#include <string>
#include <fstream>
#include <ostream>
#include <sstream>

const std::string inputFilename = "input.in";
const std::string outputFilename = "output.txt";

bool isPalindrome(int number)
{
  std::string temp = "";
  std::string tempCompare = "";
  std::stringstream buffer;
  buffer << number;
  temp = buffer.str();
  tempCompare = std::string(temp.rbegin(), temp.rend());

  return temp == tempCompare;
}

int main()
{
  int testNumber        = 0;
  int startNumber       = 0;
  int endNumber         = 0;
  int numberOfTests     = 0;
  int currentTest       = 0;
  int counter           = 0;
  double remainderTest  = 1.0;

  std::ofstream outputFile;
  std::ifstream inputFile;

  inputFile.open(inputFilename);                    // Open input file
  outputFile.open(outputFilename, std::ios::app);   // Open output file

  if(inputFile.is_open())
  {
    inputFile >> numberOfTests; // Get number of tests in file
  }

  if(inputFile.is_open()) 
  {
    while(inputFile.good() && currentTest < numberOfTests)
    {
      inputFile >> startNumber;
      inputFile >> endNumber;
     
      if(!inputFile.eof()) // If not the end of file
      {
        currentTest++;
        for(int i = startNumber; i <= endNumber; i++)
        {
          if(isPalindrome(i))
          {
            if(modf(sqrt(i), &remainderTest) == 0)
            {
              if(isPalindrome(sqrt(i)))
              {
                counter++;
              }
            }
          }
        }
      }
      outputFile << "Case #" << currentTest << ": " << counter << std::endl;
      counter = 0;
    }
  }

  inputFile.close();
  outputFile.close();

  return 0;
}