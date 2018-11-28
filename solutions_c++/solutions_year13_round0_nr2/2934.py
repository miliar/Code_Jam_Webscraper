#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
  ifstream inFile(argv[1]);

  if (inFile.good())
  {
    int T;
    inFile >> T;
    for (int t = 0; t < T; t++)
    {
      bool bGood = true;
      int N, M;
      int lawn[102][102];
      inFile >> N >> M;
      for (int n = 0; n <= N + 1; n++)
      {
        for (int m = 0; m <= M + 1; m++)
        {
          lawn[n][m] = 0;
        }
      }
      for (int n = 1; n <= N; n++)
      {
        for (int m = 1; m <= M; m++)
        {
          inFile >> lawn[n][m];
        }
      }
      for (int r = 1; bGood && r < N + 1; r++)
      {
        for (int c = 1; bGood && c < M + 1; c++)
        {
          bGood = false;
          if (!bGood)
          {
            bGood = true;
            for (int y = r - 1; y >= 0; y--)
            {
              if (lawn[r][c] < lawn[y][c])
              {
                bGood = false;
              }
            }
            for (int y = r + 1; y <= N + 1; y++)
            {
              if (lawn[r][c] < lawn[y][c])
              {
                bGood = false;
              }
            }
          }
          if (!bGood)
          {
            bGood = true;
            for (int x = c - 1; x >= 0; x--)
            {
              if (lawn[r][c] < lawn[r][x])
              {
                bGood = false;
              }
            }
            for (int x = c + 1; x <= M + 1; x++)
            {
              if (lawn[r][c] < lawn[r][x])
              {
                bGood = false;
              }
            }
          }
        }
      }
      cout << "Case #" << (t + 1) << ": " << ((bGood)?"YES":"NO") << endl;
    }
  }
  inFile.close();

  return 0;
}
