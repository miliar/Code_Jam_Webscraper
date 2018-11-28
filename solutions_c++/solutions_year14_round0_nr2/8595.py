#include <fstream>
#include <iostream>
#include <stdlib.h>
 #include <sstream>
#include <vector>
#include <iomanip>
using namespace std;

void split(const string &Str, vector<string> &tokens, char sep) 
{
  int start = 0, end = 0;
  while ((end = Str.find(sep, start)) != string::npos) {
    tokens.push_back(Str.substr(start, end - start));
    start = end + 1;
  }
  tokens.push_back(Str.substr(start));
}


int main ()
{
   ofstream outfile;
   ifstream infile;

   // open a file in read mode.
   infile.open("B-large.in");

   // open a file in write mode.
   outfile.open("B-large.out");

   string line;
   vector < string > vStr;
   int iTotalTestCases = 0;

   double totalCookiesPerSec = 2;
   if (infile.is_open())
   {
      //Get number of test cases
      getline (infile,line);
      iTotalTestCases = atoi(line.c_str());
      //cout << "iTotalTestCases:" << iTotalTestCases << std::endl;

      for(int i = 1; i <= iTotalTestCases; i++)
      {
         getline (infile,line);
         //cout << "i:" << i << endl;
         vStr.clear();
         split(line, vStr, ' ');
         if(vStr.size() == 3)
         {
            double C = atof(vStr[0].c_str());
            double F = atof(vStr[1].c_str());
            double X = atof(vStr[2].c_str());
            //cout << "C:" << C << "  F:" << F << "  X:" << X << std::endl;

            double prevTotalSecToReachPrize = 0;
            double TotalSecToReachPrize = 0;
            double iterTotalToReachPrize = 0;
            double M = 2;
            int iIterCount = 0; 
            double costOfFirm = 0;
            
            while(1)
            {
              iterTotalToReachPrize = ( (X) / (M + (iIterCount * F) ) );
              TotalSecToReachPrize = iterTotalToReachPrize + costOfFirm;

              if(prevTotalSecToReachPrize!=0 && TotalSecToReachPrize > prevTotalSecToReachPrize )
              {
                 char buffer[100] = {0};
                 sprintf( buffer , "%0.7f\n", prevTotalSecToReachPrize);
                 //cout << "------>prevTotalSecToReachPrize:" << setprecision(7) << prevTotalSecToReachPrize << endl;
                 //outfile << "Case #" << i << ": " << setprecision(12) << prevTotalSecToReachPrize << std::endl;
                 outfile << "Case #" << i << ": " << buffer;
                 break;
              }

              prevTotalSecToReachPrize = TotalSecToReachPrize;
              costOfFirm = costOfFirm + ( (C) / (M + (iIterCount * F) ) );
              iIterCount = iIterCount + 1;
            }
         }
      }
  }

   infile.close();
   outfile.close();

}
