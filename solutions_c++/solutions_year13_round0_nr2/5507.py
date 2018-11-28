// Google Codejam 2013 Qualification
// B. Lawnmower
// Author: Paul Cuthbert

#include <iostream>
#include <string>
#include <fstream>
#include <ostream>

const int LAWNSIZEMAX     = 100;
const std::string inputFilename = "B-small-attempt1.in";
const std::string outputFilename = "output.txt";

std::string lawnResult(const int lawn[][LAWNSIZEMAX], int lawnN, int lawnM)
{
  std::string lawnResult = "";
  bool possible = true;

  if(possible && !(lawnN == 1 || lawnM == 1))
  {
    for(int i = 0; i < lawnN; i++) // iterate rows
    {
      for(int j = 0; j < lawnM; j++) // iterate cols
      {
        if(lawn[i][j] > lawn[i][j-1] && j-1 >= 0 && possible) // Checks area to left
        {
          for(int x = j-1; x >= 0; x--)
          {
            for(int k = 0; k < lawnN; k++)
            {
              if(! (lawn[i][x] >= lawn[k][x]) && possible) // Column check
              {
                possible = false;
              }
            }
          }
        }

        if(lawn[i][j] > lawn[i-1][j] && i-1 >= 0 && possible) // Checks area above
        {
          for(int x = i-1; x >= 0; x--)
          {
            for(int k = 0; k < lawnM; k++)
            {
              if(! (lawn[x][j] >= lawn[x][k]) && possible) // Row check
              {
                possible = false;
              }
            }
          }
        }

        if(lawn[i][j] > lawn[i][j+1] && j+1 < lawnM && possible) // Checks area to right
        {
          for(int x = j+1; x < lawnM; x++)
          {
            for(int k = 0; k < lawnN; k++)
            {
              if(! (lawn[i][x] >= lawn[k][x]) && possible) // Column check
              {
                possible = false;
              }
            }
          }
        }

        if(lawn[i][j] > lawn[i+1][j] && i+1 < lawnN && possible) // Checks area below
        {
          for(int x = i+1; x < lawnN; x++)
          {
            for(int k = 0; k < lawnM; k++)
            {
              if(!(lawn[x][j] >= lawn[x][k]) && possible) // Row check
              {
                possible = false;
              }
            }
          }
        }
      }
    }
  }

  if(possible)
  {
    lawnResult = "YES";
  }
  else
  {
    lawnResult = "NO";
  }

  return lawnResult;
}

int main()
{
  int lawn[LAWNSIZEMAX][LAWNSIZEMAX]; // 2D lawn array
  int lawnM = 0; // Columns
  int lawnN = 0; // Rows
  int numberOfInts = 0;
  int numberOfTests = 0;
  int currentTest = 0;

  std::string inputBuffer;
  std::string outputBuffer;

  std::ofstream outputFile;
  std::ifstream inputFile;

  for(int i = 0; i < LAWNSIZEMAX; i++) // Initialise board with 0's
  {
    for(int j = 0; j < LAWNSIZEMAX; j++)
    {
      lawn[i][j] = 0;
    }
  }

  inputFile.open(inputFilename);                   // Open input file
  outputFile.open(outputFilename, std::ios::app);  // Open output file
  
  if(inputFile.is_open())
  {
    inputFile >> numberOfTests; // Get number of tests in file
  }

  if(inputFile.is_open()) 
  {
    while(inputFile.good() && currentTest < numberOfTests)
    {
      inputFile >> lawnN;
      inputFile >> lawnM;

      numberOfInts = lawnN * lawnM;
      
      if(!inputFile.eof()) // If not the end of file
      {
        currentTest++;

        for(int i = 0; i < lawnN; i++) // populates array with values
        {
          for(int j = 0; j < lawnM; j++)
          {
            inputFile >> lawn[i][j];
          }
          
        }
      }
      outputBuffer.clear();
      outputBuffer = lawnResult(lawn, lawnN, lawnM);
      outputFile << "Case #" << currentTest << ": " << outputBuffer << std::endl;
    }
  }

  inputFile.close();
  outputFile.close();

  return 0;
}