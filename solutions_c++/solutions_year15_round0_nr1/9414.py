#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
using namespace std;


int main()
{
      int T, tCase, shyMax, *sness, i;
      int *sdif, *scum, inv;
      char inChar;
      ifstream inFile;
      ofstream outFile;
      inFile.open("C:\\Users\\IBM_ADMIN\\Desktop\\A-large.in");
      outFile.open("C:\\Users\\IBM_ADMIN\\Desktop\\A-small-out.txt");

      inFile >> T;
      for (tCase=1; tCase <= T; tCase++)
      {
          inFile >> shyMax;
          sness = new int[shyMax+1];
          scum = new int[shyMax+1];
          sdif = new int[shyMax+1]; 
          inFile.get(inChar);
          for (i=0; i <= shyMax; i++)
          {
              inFile.get(inChar);
              sness[i] = inChar - '0';
          }
          scum[0] = 0;
          for (i=1; i <= shyMax; i++)
          {
              scum[i] = scum[i-1]+ sness[i-1];
          }
          for (i=0; i <= shyMax; i++)
          {
              sdif[i] = i-scum[i];
          }
          inv = 0;
          for (i=0; i <= shyMax; i++)
          {
              if (inv < sdif[i])
                 inv = sdif[i];
          }
          outFile << "Case #" << tCase << ": " << inv << "\n";
      }
      
}
