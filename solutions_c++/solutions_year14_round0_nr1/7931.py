#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
using namespace std;


int main()
{
      unsigned int T, Row, tCase, n1, n2, n3, n4, first[4], second[4],matchCount, match;
      int i, j;
      ifstream inFile;
      ofstream outFile;
      inFile.open("C:\\Users\\IBM_ADMIN\\Desktop\\A-small-attempt0.in");
      outFile.open("C:\\Users\\IBM_ADMIN\\Desktop\\A-small-out.txt");

      inFile >> T;
      for (tCase=1; tCase <= T; tCase++)
      {
          inFile >> Row;
          for (i=0; i<4; i++)
          {
              inFile >> n1 >> n2 >> n3 >> n4;
              if (i == Row-1)
              {
                    first[0] = n1;
                    first[1] = n2;
                    first[2] = n3;
                    first[3] = n4;
              }              
          }
          inFile >> Row;
          for (i=0; i<4; i++)
          {
              inFile >> n1 >> n2 >> n3 >> n4;
              if (i == Row-1)
              {
                    second[0] = n1;
                    second[1] = n2;
                    second[2] = n3;
                    second[3] = n4;
              }              
          }
          matchCount=0;
          for (i=0; i<4; i++)
          {
             for (j=0; j<4; j++)
             {
                 if (first[i] == second[j])
                 {
                    matchCount++;
                    match = first[i];
                 }
             } 
          }
          if (matchCount == 0)
             outFile << "Case #" << tCase << ": " << "Volunteer cheated!" << "\n";
          if (matchCount == 1)
             outFile << "Case #" << tCase << ": " << match << "\n";
          if (matchCount > 1)
             outFile << "Case #" << tCase << ": " << "Bad magician!" << "\n";
      }
      
}
