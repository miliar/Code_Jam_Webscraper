#include <iostream>

using namespace std;

const int maxRows = 4;
const int maxCols = 4;

int main()
{
  int firstArray[maxRows][maxCols];
  int secondArray[maxRows][maxCols];
  int firstPossibles[maxCols];
  int secondPossibles[maxCols];
  int firstRow;
  int secondRow;
  int totalTests;
  int totalFound=0;
  int match=-1;
  int currentTestcase=0;

  int i,j;

  cin >> totalTests;

  while (currentTestcase != totalTests) {
    currentTestcase++;

    cin >> firstRow;

    for(i=0;i<maxRows;i++)
      for(j=0;j<maxCols;j++)
	cin >> firstArray[i][j];

    cin >> secondRow;

    for(i=0;i<maxRows;i++)
      for(j=0;j<maxCols;j++)
	cin >> secondArray[i][j];

    for(j=0;j<maxCols;j++)
      firstPossibles[j] = firstArray[firstRow - 1][j];

    for(j=0;j<maxCols;j++)
      secondPossibles[j] = secondArray[secondRow - 1][j];

    totalFound = 0;
    match = -1;
    for(i=0;i<maxCols;i++) {
      for(j=0;j<maxCols;j++) {
	if (firstPossibles[j] == secondPossibles[i]) {
	  totalFound++;
	  match = firstPossibles[j];
	}
      }
    }

    if (totalFound == 1) {
      cout << "Case #" <<currentTestcase << ": " << match << endl;
    } else if (totalFound > 1) {
      cout << "Case #" <<currentTestcase << ": " << "Bad magician!" <<endl;
    } else if (totalFound == 0) {
	cout << "Case #" <<currentTestcase << ": " << "Volunteer cheated!" <<endl;
    } else {
	cout <<"something is wrong!"<<endl;
    }

  }

  return 0;
}
