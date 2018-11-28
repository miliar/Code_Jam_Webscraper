#include <iostream>
#include <cmath>
#include <string>
#include <cstdlib>
#include <fstream>
#include <vector>

using namespace std;

bool test(char (*matrix)[4], int i, int j, const int &a, const int &b)
{
  if ((i+a == 4) || (j+b == 4))
    return true;

  //if ((matrix[i][j] == matrix[i+a][j+b]) || (matrix[i+a][j+b] == 'T') && (matrix[i+a][j+b] != '.'))
  if ((matrix[i+a][j+b] != '.') && ((matrix[i][j] == matrix[i+a][j+b]) || (matrix[i+a][j+b] == 'T')))
    return test(matrix, i+a, j+b, a, b);
  else
    return false;
}

int main(int argc, char *argv[])
{
  ifstream input("A-small-attempt0.in");
  //ifstream input("teste.txt");
  ofstream output("output.txt");

  int t, i, j, k;
  char matrix[4][4];
  char temp, win = 'Y';
  bool draw_pos;
  string result;

  input >> t;
  for (i = 0; i < t; ++i)
  {
    win = 'Y';
    draw_pos = true;
    for (j = 0; j < 4; ++j)
      for (k = 0; k < 4; ++k)
      {
        input >> matrix[j][k];
        if (matrix[j][k] == '.')
          draw_pos = false;
      }


    //line test
    for (j = 0; j < 4; ++j)
      if (test(matrix, j, 0, 0, 1))
      {
        win = matrix[j][0];
        //result = matrix[j][0] + " won";
        goto end;
        //break;
      }

    //column test
    for (j = 0; j < 4; ++j)
      if (test(matrix, 0, j, 1, 0))
      {
        win = matrix[0][j];
        //result = matrix[0][j] + " won";
        goto end;
        //break;
      }

    //diagonal 1 test
    if (test(matrix, 0, 0, 1, 1))
      win = matrix[0][0];
      //result = matrix[0][0] + " won";
    //diagonal 2 test
    else if (test(matrix, 0, 3, 1, -1))
      win = matrix[0][3];
      //result = matrix[0][3] + " won";



end:
    if ((win == 'Y') && (draw_pos))
      //cout << "Case #" << i + 1 << ": " <<  "Draw" << endl;
      output << "Case #" << i + 1 << ": " <<  "Draw" << endl;
    else if ((win == 'Y') && (!draw_pos))
      //cout << "Case #" << i + 1 << ": " <<  "Game has not completed" << endl;
      output << "Case #" << i + 1 << ": " <<  "Game has not completed" << endl;
    else
      //cout << "Case #" << i + 1 << ": " << win << " won" << endl;
      output << "Case #" << i + 1 << ": " << win << " won" << endl;


    //cout << win;

    input.ignore();
  }

  //cout << "Case #" << i + 1 << ": " << matrix[0][0] << ".0000"<< endl;
  //getchar();
  //output << "Case #" << i + 1 << ": " << hits << ".000000" << endl;



  output.close();
  input.close();

}
