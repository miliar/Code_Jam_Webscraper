#include <iostream>
#include <string>
#include <vector> 

using namespace std;

int thisPossible(vector<vector<int> > lawn, int rows, int cols, int y, int x) {
  int i;

  for (i=0; i<cols; i++) 
    if (lawn[y][i] > lawn[y][x])
      break;

  if (i == cols)
    return true;

  for (i=0; i<rows; i++) 
    if (lawn[i][x] > lawn[y][x])
      break;

  if (i == rows)
    return true;

  return false;
}

int main() {
  int cases;

  cin >> cases;
  for (int i=0; i<cases; i++) {
    // I posit that the answer is YES if and only if each entry lives in either a ROW
    // or a COL where its height is >= all others.
    int rows;
    int cols;

    cin >> rows >> cols;

    vector<vector<int> > lawn(rows, vector<int>(cols));

    for (int j=0; j<rows; j++)
      for (int k=0; k<cols; k++)
        cin >> lawn[j][k];

    bool possible = true;

    for (int j=0; j<rows; j++)
      for (int k=0; k<cols; k++) 
        possible = possible && thisPossible(lawn, rows, cols, j, k);

    cout << "Case #" << (i + 1) << ": ";

    if (possible)
      cout << "YES\n";
    else 
      cout << "NO\n";    
  }

  return 0;
}
