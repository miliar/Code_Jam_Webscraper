#include <iostream>
#include <string.h>

#include <fstream>
#include <iostream>
#include <stdlib.h>
 #include <sstream>
#include <vector>
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

int main()
{
   int aRowchoose[5] = {0};
   int uTotalNumberOfTestcase = 0;
   int FirstTimeRowSelect = 0;
   int SecondTimesRowSelect = 0;   
   int uMatchCount = 0;
   int matchNumber = 0;
   string line;
   vector < string > vStr;
   int iTotalTestCases = 0;
   double dTotalNoOfSec = 0.0;

   ofstream outfile;
   ifstream infile;

   // open a file in read mode.
   infile.open("A.in");

   // open a file in write mode.
   outfile.open("A.out");

   if (infile.is_open())
   {
      getline (infile,line);
      uTotalNumberOfTestcase = atoi(line.c_str());

      for(int l = 1; l <= uTotalNumberOfTestcase; l++)
      {
         int row1[5] = {0};
         int row2[5] = {0};
         int row3[5] = {0};
         int row4[5] = {0};
         int aRowchoose[5] = {0};
         int aSecondRowchoose[5] = {0};

         //get the first choice
         getline (infile,line);
         FirstTimeRowSelect = atoi(line.c_str());

         //get next 4 line inputs
         for(int i=1; i <= 4; i++)
         {
            getline (infile,line);
            vStr.clear();
            split(line, vStr, ' ');
            if(vStr.size() == 4)
            {
               switch(i)
               {
                  case 1:
                  {
                     row1[1] = atoi(vStr[0].c_str());
                     row1[2] = atoi(vStr[1].c_str());
                     row1[3] = atoi(vStr[2].c_str());
                     row1[4] = atoi(vStr[3].c_str());
                     if(FirstTimeRowSelect == 1)
                     {
                        aRowchoose[1] = row1[1];
                        aRowchoose[2] = row1[2];
                        aRowchoose[3] = row1[3];
                        aRowchoose[4] = row1[4];
                     }
                  }
                  break;
                  case 2:
                  {
                     row2[1] = atoi(vStr[0].c_str());
                     row2[2] = atoi(vStr[1].c_str());
                     row2[3] = atoi(vStr[2].c_str());
                     row2[4] = atoi(vStr[3].c_str());
                     if(FirstTimeRowSelect == 2)
                     {
                        aRowchoose[1] = row2[1];
                        aRowchoose[2] = row2[2];
                        aRowchoose[3] = row2[3];
                        aRowchoose[4] = row2[4];
                     }
                  }
                  break;
                  case 3:
                  {
                     row3[1] = atoi(vStr[0].c_str());
                     row3[2] = atoi(vStr[1].c_str());
                     row3[3] = atoi(vStr[2].c_str());
                     row3[4] = atoi(vStr[3].c_str());
                     if(FirstTimeRowSelect == 3)
                     {
                        aRowchoose[1] = row3[1];
                        aRowchoose[2] = row3[2];
                        aRowchoose[3] = row3[3];
                        aRowchoose[4] = row3[4];
                     }
                  }
                  break;
                  case 4:
                  {
                     row4[1] = atoi(vStr[0].c_str());
                     row4[2] = atoi(vStr[1].c_str());
                     row4[3] = atoi(vStr[2].c_str());
                     row4[4] = atoi(vStr[3].c_str());
                     if(FirstTimeRowSelect == 4)
                     {
                        aRowchoose[1] = row4[1];
                        aRowchoose[2] = row4[2];
                        aRowchoose[3] = row4[3];
                        aRowchoose[4] = row4[4];
                     }
                  }
                  break;
               }
            }
         }


         //get the second choice
         getline (infile,line);
         SecondTimesRowSelect = atoi(line.c_str());

         //get next 4 line inputs
         for(int i=1; i <= 4; i++)
         {
            getline (infile,line);
            vStr.clear();
            split(line, vStr, ' ');
            if(vStr.size() == 4)
            {
               switch(i)
               {
                  case 1:
                  {
                     row1[1] = atoi(vStr[0].c_str());
                     row1[2] = atoi(vStr[1].c_str());
                     row1[3] = atoi(vStr[2].c_str());
                     row1[4] = atoi(vStr[3].c_str());
                     if(SecondTimesRowSelect == 1)
                     {
                        aSecondRowchoose[1] = row1[1];
                        aSecondRowchoose[2] = row1[2];
                        aSecondRowchoose[3] = row1[3];
                        aSecondRowchoose[4] = row1[4];
                     }
                  }
                  break;
                  case 2:
                  {
                     row2[1] = atoi(vStr[0].c_str());
                     row2[2] = atoi(vStr[1].c_str());
                     row2[3] = atoi(vStr[2].c_str());
                     row2[4] = atoi(vStr[3].c_str());
                     if(SecondTimesRowSelect == 2)
                     {
                        aSecondRowchoose[1] = row2[1];
                        aSecondRowchoose[2] = row2[2];
                        aSecondRowchoose[3] = row2[3];
                        aSecondRowchoose[4] = row2[4];
                     }
                  }
                  break;
                  case 3:
                  {
                     row3[1] = atoi(vStr[0].c_str());
                     row3[2] = atoi(vStr[1].c_str());
                     row3[3] = atoi(vStr[2].c_str());
                     row3[4] = atoi(vStr[3].c_str());
                     if(SecondTimesRowSelect == 3)
                     {
                        aSecondRowchoose[1] = row3[1];
                        aSecondRowchoose[2] = row3[2];
                        aSecondRowchoose[3] = row3[3];
                        aSecondRowchoose[4] = row3[4];
                     }
                  }
                  break;
                  case 4:
                  {
                     row4[1] = atoi(vStr[0].c_str());
                     row4[2] = atoi(vStr[1].c_str());
                     row4[3] = atoi(vStr[2].c_str());
                     row4[4] = atoi(vStr[3].c_str());
                     if(SecondTimesRowSelect == 4)
                     {
                        aSecondRowchoose[1] = row4[1];
                        aSecondRowchoose[2] = row4[2];
                        aSecondRowchoose[3] = row4[3];
                        aSecondRowchoose[4] = row4[4];
                     }
                  }
                  break;
               }
            }
         }

         uMatchCount = 0;
         matchNumber = 0;
         for(int i = 1; i <= 4; i++)
         {
            for(int j = 1; j <= 4; j++)
            {
               if(aRowchoose[i] == aSecondRowchoose[j])
               {
                  matchNumber = aRowchoose[i];
                  uMatchCount = uMatchCount + 1;
               }
            }
         }

         if(uMatchCount == 1)
         {
            outfile << "Case #" << l << ": " << matchNumber << std::endl;
         }
         if(uMatchCount > 1)
         {
            outfile << "Case #" << l << ": " << "Bad magician!" << std::endl;
         }
         else if(uMatchCount == 0)
         {
            outfile << "Case #" << l << ": " << "Volunteer cheated!" << std::endl;
         }
      }
   }

   infile.close();
   outfile.close();

   return 0;
}
