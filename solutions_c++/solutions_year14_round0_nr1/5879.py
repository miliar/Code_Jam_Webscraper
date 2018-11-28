#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
  ifstream fin("A-small-attempt1.in");
  ofstream fout("a.txt");
  int T;
  fin >> T;

  int r1, r2, conf1[4][4], conf2[4][4];
  for (int t = 1; t <= T; ++t) {
    fin >> r1;
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j)
        fin >> conf1[i][j];

    fin >> r2;
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j)
        fin >> conf2[i][j];

    int same = 0;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        if (conf1[r1-1][i] == conf2[r2-1][j]) {
          if (same > 0) {
            same = -1;
            goto end;
          } else /* if (0 == same) */ {
            same = conf1[r1-1][i];
          }
        }
      }
    }

 end:
    fout << "Case #" << t << ": ";

    if (same < 0) fout << "Bad magician!" << endl;
    else if (0 == same) fout << "Volunteer cheated!" << endl;
    else fout << same << endl;
  }

  fin.close();
  fout.close();

  return 0;
}
