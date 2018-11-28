#include <iostream>
#include <vector>
using namespace std;

void doCase() {
  int row;
  cin >> row;
  row--;
  int x[4];
  int y[4];
  int temp;
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++) {
      cin >> temp;
      if (i == row)
	x[j] = temp;
    }
  int row2;
  cin >> row2;
  row2--;
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      cin >> y[j];
    }
    if (i == row2) {
      int count = 0;
      int first = 0;
      for (int j = 0; j < 4; j++)
	for (int k = 0; k < 4; k++)
	  if (x[j] == y[k]) {
	    first = x[j];
	    count++;
	  }
      if (count == 1) {
	cout << first << '\n';
      } else if (count > 1)
	cout << "Bad magician!\n";
      else
	cout << "Volunteer cheated!\n";
    }
  }
}


int main() {
  int numcases, credit, numPrices;
  cin >> numcases;
  for (int cases = 1; cases <= numcases; cases++) {
    cout << "Case #" << cases << ": ";
    doCase();
  }
}
