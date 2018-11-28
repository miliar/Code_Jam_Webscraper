
#include <iostream>

using namespace std;


void readMatrix(int matrix[4][4], int &answer)
{
  cin >> answer;
  for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
      cin >> matrix[i][j];
}

void findCommon(int matrix1[4][4], int answer1, int matrix2[4][4], int answer2)
{
  int matchCount = 0;
  int matchNumber = 0;
  for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
      if(matrix1[answer1][i] == matrix2[answer2][j]) {
	matchCount++;
	matchNumber = matrix1[answer1][i];
      }

  if(matchCount == 0)
    cout << "Volunteer cheated!";
  else if(matchCount > 1)
    cout << "Bad magician!";
  else
    cout << matchNumber;
}

int main(int argc, char **argv)
{

  int testCount = 0;
  cin >> testCount;
  
  int matrix1[4][4],
    matrix2[4][4],
    answer1,
    answer2;
  for(int testCounter=0; testCounter<testCount; testCounter++) {
    readMatrix(matrix1, answer1);
    readMatrix(matrix2, answer2);
    cout << "Case #" << (testCounter + 1) << ": ";
    findCommon(matrix1, answer1-1, matrix2, answer2-1);
    cout << endl;
  }
}

