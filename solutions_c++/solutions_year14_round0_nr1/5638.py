#include <iostream>
#include <fstream>
#include <cstdlib>
#include <map>
#include <vector>
#include <stack>

using namespace std;

int solve(int guess1, int guess2, int *grid1, int *grid2)
{
  int result = -2;
  int i, j;

  for (i = 0; i < 4; i++)
  {
    for (j = 0; j < 4; j++)
    {
      if (grid1[4 * (guess1 - 1) + i] == grid2[4 * (guess2 - 1) + j])
      {
        if (result > 0)
          return -1;
        result = grid1[4 * (guess1 - 1) + i];
      }
    }
  }
  return result;
}

int main()
{
  ifstream infile;
  ofstream outfile;

  infile.open("magic_trick.in", fstream::in);
  outfile.open("magic_trick.out", fstream::out);

  int T, n, i; // Number of test cases.
  int grid1[16];
  int grid2[16];
  int guess1, guess2;
  int result;

  infile >> T;

  for (n = 1; n <= T; n++)
  {
    infile >> guess1;
    for (i = 0; i < 16; i++)
      infile >> grid1[i];
    infile >> guess2;
    for (i = 0; i < 16; i++)
      infile >> grid2[i];
    result = solve(guess1, guess2, grid1, grid2);

    outfile << "Case #" << n << ": ";
    if (result == -1)
      outfile << "Bad magician!\n";
    else if (result == -2)
      outfile << "Volunteer cheated!\n";
    else
      outfile << result << "\n";
  }

  infile.close();
  outfile.close();
  return 0;
}
