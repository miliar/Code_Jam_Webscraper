///////////////////////////////////////////////////////////////////////////////////////////////////
//
// Problem: E:\WorkArea\CodeJam\2013\B_Lawnmower
//
// 

// Case #1: YES
// Case #2: NO
//
///////////////////////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <map>
#include <math.h>

using namespace std;

const int MAX_ROWS = 100;
const int MAX_COLS = 100;

int CalculateMaximumInRow(int p_arrGrassHeightDesired[MAX_ROWS][MAX_COLS], int p_iNumCols, int p_iNumRow)
{
   int iMax = -1;

   for (int iCtrCol = 0; iCtrCol < p_iNumCols; ++iCtrCol) {
      if (iMax < p_arrGrassHeightDesired[p_iNumRow][iCtrCol]) {
         iMax = p_arrGrassHeightDesired[p_iNumRow][iCtrCol];
      }
   }

   return iMax;
}

int CalculateMaximumInCol(int p_arrGrassHeightDesired[MAX_ROWS][MAX_COLS], int p_iNumRows, int p_iNumCol)
{
   int iMax = -1;

   for (int iCtrRow = 0; iCtrRow < p_iNumRows; ++iCtrRow) {
      if (iMax < p_arrGrassHeightDesired[iCtrRow][p_iNumCol]) {
         iMax = p_arrGrassHeightDesired[iCtrRow][p_iNumCol];
      }
   }

   return iMax;
}

bool CompareMatrix(int p_arrGrassHeightDesired[MAX_ROWS][MAX_COLS], int arrGrassHeight[MAX_ROWS][MAX_COLS],
                   int p_iNumRows, int p_iNumCols)
{
   for (int iCtrRow = 0; iCtrRow < p_iNumRows; ++iCtrRow) {
      for (int iCtrCol = 0; iCtrCol < p_iNumCols; ++iCtrCol) {
         if (p_arrGrassHeightDesired[iCtrRow][iCtrCol] != arrGrassHeight[iCtrRow][iCtrCol]) {
            return false;
         }
      }
   }

   return true;
}

bool CalculateResult(int p_arrGrassHeightDesired[MAX_ROWS][MAX_COLS], int p_iNumRows, int p_iNumCols)
{
   int arrGrassHeight[MAX_ROWS][MAX_COLS];

   for (int iCtrRow = 0; iCtrRow < p_iNumRows; ++iCtrRow) {
      for (int iCtrCol = 0; iCtrCol < p_iNumCols; ++iCtrCol) {
         arrGrassHeight[iCtrRow][iCtrCol] = 100;
      }
   }

   for (int iCtrRow = 0; iCtrRow < p_iNumRows; ++iCtrRow) {
      // Calculate maximum value from row number iCtrRow of input array of grass height desired
      int iMax = CalculateMaximumInRow(p_arrGrassHeightDesired, p_iNumCols, iCtrRow);

      // Most Important Step:
      // Reset the value of each element of iCtrRow row of output array to max value calculated above only if 
      // it is greater; othewise now
      for (int iCtrCol = 0; iCtrCol < p_iNumCols; ++iCtrCol) {
         if (arrGrassHeight[iCtrRow][iCtrCol] > iMax)
            arrGrassHeight[iCtrRow][iCtrCol] = iMax;
      }
   }

   for (int iCtrCol = 0; iCtrCol < p_iNumCols; ++iCtrCol) {
      // Calculate maximum value from col number iCtrCol of input array of grass height desired
      int iMax = CalculateMaximumInCol(p_arrGrassHeightDesired, p_iNumRows, iCtrCol);

      // Most Important Step:
      // Reset the value of each element of iCtrCol col of output array to max value calculated above only if 
      // it is greater; othewise now
      for (int iCtrRow = 0; iCtrRow < p_iNumRows; ++iCtrRow) {
         if (arrGrassHeight[iCtrRow][iCtrCol] > iMax)
            arrGrassHeight[iCtrRow][iCtrCol] = iMax;
      }
   }

   // Compare two matrix for equality
   // Return true if equal; false otherwise
   bool bIsEqual = CompareMatrix(p_arrGrassHeightDesired, arrGrassHeight, p_iNumRows, p_iNumCols);

   return bIsEqual;
}

int main()
{
   string l_inFileName = "./B-large.in";
   string l_outFileName = "./B-large.out";
   ifstream l_inFilesStream;
   ofstream l_outFileStream;

   l_inFilesStream.open(l_inFileName.c_str());
   l_outFileStream.open(l_outFileName.c_str());

   if (l_inFilesStream && l_outFileStream)
   {
      if (!l_inFilesStream.eof())
      {
         string l_strNumTestCases;
         int l_numTestCases = -1;

         getline(l_inFilesStream, l_strNumTestCases);

         l_numTestCases = atoi(l_strNumTestCases.c_str());

         // Run each test case
         for (int l_itest = 0; l_itest < l_numTestCases; ++l_itest)
         {
            //3 3
            //2 1 2
            //1 1 1
            //2 1 2
            int arrGrassHeightDesired[MAX_ROWS][MAX_COLS];
            string strLineRead;
            
            getline(l_inFilesStream, strLineRead);
            stringstream strStream(strLineRead);

            int iNumRows = -1;
            int iNumCols = -1;
            string l_tokenString;

            getline(strStream, l_tokenString, ' ');
            iNumRows = atoi(l_tokenString.c_str());

            getline(strStream, l_tokenString, ' ');
            iNumCols = atoi(l_tokenString.c_str());


            for (int iCtrRow = 0; iCtrRow < iNumRows; ++iCtrRow) {
               getline(l_inFilesStream, strLineRead);
               stringstream strStreamGrassHeightDesired(strLineRead);
               
               for (int iCtrCol = 0; iCtrCol < iNumCols; ++iCtrCol) {
                  getline(strStreamGrassHeightDesired, l_tokenString, ' ');
                  arrGrassHeightDesired[iCtrRow][iCtrCol] = atoi(l_tokenString.c_str());
               }
            }

            bool result = CalculateResult(arrGrassHeightDesired, iNumRows, iNumCols);

            l_outFileStream << "Case #" << (l_itest+1) << ": " << (result ? "YES" : "NO") << endl;
            cout << "Case #" << (l_itest+1) << ": " << (result ? "YES" : "NO") << endl;
         }
      }
      else
      {
         cout << "File is empty" << endl;
      }
   }
   else
   {
      if (!l_inFilesStream)
         cout << "Input file couldn't be opened" << endl;
      else
         cout << "Output file couldn't be opened" << endl;

      return -1;
   }

   return 0;
}
