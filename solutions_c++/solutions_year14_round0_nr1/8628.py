#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int mas1[5][5], mas2[5][5];
int main()
{
  int i, j, n, m, k, t;
  ifstream cin ("input.in");
  ofstream cout ("output.txt");
  cin >> t;
  for (k = 0; k < t; k++)
  {
    int row1, row2;

    cin >> row1;
    for (j = 1; j < 5; j++)
    {
      for (i = 1; i < 5; i++)
        cin >> mas1[j][i];
    }
    cin >> row2;
    for (j = 1; j < 5; j++)
    {
      for (i = 1; i < 5; i++)
        cin >> mas2[j][i];
    }
    int same = 0, num;
    for (j = 1; j < 5; j++)
    {
      for (i = 1; i < 5; i++)
      {
        if (mas1[row1][j] == mas2[row2][i])
        {
          same++;
          num = mas1[row1][j];
        }
      }
    }
    cout << "Case #" << k + 1 << ": ";
    if (same == 1)
    {
      cout << num << endl;
    }
    else if (same > 1)
    {
      cout << "Bad magician!\n";
    }
    else
    {
      cout << "Volunteer cheated!\n";
    }
  }
}
