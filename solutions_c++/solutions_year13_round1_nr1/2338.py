
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <map>
#include <math.h>

using namespace std;


unsigned int CalculateResult(unsigned long long r, unsigned long long t)
{
   unsigned int iNumRounds = 0;
   unsigned long long l_2r = (2 * r);
   unsigned long long delta  = 1;
   unsigned long long nextArea = l_2r + delta;
   
   while ( t >= nextArea ) {
      t -= nextArea;
      ++iNumRounds;
      delta = iNumRounds * 4 + 1;
      nextArea = l_2r + delta;
   }

   return iNumRounds;
}

int main()
{
   
   //string l_inFileName = "./A-Sample.in";
   //string l_outFileName = "./A-Sample.out";
   string l_inFileName = "./A-small-attempt0.in";
   string l_outFileName = "./A-small-attempt0.out";
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
            unsigned long long r;
            unsigned long long t;
            string strLineRead;
            
            getline(l_inFilesStream, strLineRead);
            stringstream strStream(strLineRead);

            strStream >> r >> t;

            unsigned int iMaxDrawnRings = CalculateResult(r, t);

            l_outFileStream << "Case #" << (l_itest+1) << ": " << iMaxDrawnRings << endl;
            cout << "Case #" << (l_itest+1) << ": " << iMaxDrawnRings << endl;
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
