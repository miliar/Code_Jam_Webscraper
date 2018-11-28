#include <iostream.h>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
using namespace std;


int main()
{
      unsigned int T, tCase;
      double C, F, X, curRate, minTime, timeWNofarm, timeWfarm;
      ifstream inFile;
      ofstream outFile;
      inFile.open("C:\\Users\\IBM_ADMIN\\Desktop\\B-large.in");
      outFile.open("C:\\Users\\IBM_ADMIN\\Desktop\\B-large-out.txt");
      //ofstream::cout << ofstream::fixed;
      inFile >> T;
     
      for (tCase=1; tCase <= T; tCase++)
      {
          inFile >> C >> F >> X;
          if (X > C)
          {     
                curRate = 2;
                minTime = 0;
                while (1)
                {
                      timeWNofarm = X/curRate; 
                      timeWfarm = (C/curRate)+(X/(curRate+F));
                      if (timeWNofarm < timeWfarm)
                      {
                         minTime += timeWNofarm;
                         break;
                      }
                      else
                      {
                          minTime += C/curRate;
                          curRate += F;
                          
                      }
                }
          }
          else
              minTime = X/2;
          
          outFile << std::fixed;
          outFile << setprecision(7);
	      outFile << "Case #" << tCase << ": "  << minTime << "\n";
      }
      
}
