#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
  ifstream inFile(argv[1]);

  if (inFile.good())
  {
    int T;
    inFile >> T;
    for (int x = 0; x < T; x++)
    {
      double A, B;
      int y = 0;
      inFile >> A >> B;
      for (double d = A; d <= B; d++)
      {
        double s = sqrt(d);
        if (floor(s) == s)
        {
          bool bMatch[2] = {true, true};
          string strN[2];
          stringstream ssD, ssS;
          ssD << d;
          strN[0] = ssD.str();
          ssS << s;
          strN[1] = ssS.str();
          for (int i = 0; i < 2; i++)
          {
            int nSize = strN[i].size(), nHalf = (nSize - (nSize % 2)) / 2;
            for (int j = 0; bMatch[i] && j < nHalf; j++)
            {
              if (strN[i][j] != strN[i][nSize - (j + 1)])
              {
                bMatch[i] = false;
              }
            }
          }
          if (bMatch[0] && bMatch[1])
          {
            y++;
          }
        }
      }
      cout << "Case #" << (x + 1) << ": " << y << endl;
    }
  }
  inFile.close();

  return 0;
}
