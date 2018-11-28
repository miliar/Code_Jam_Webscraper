#include <iostream>
#include <sstream>
#include <string> 

using namespace std;

void case_(int n, string answer) {
  cout << "Case #" << n << ":" << " " << answer << endl; 
}

void readMatrix(int (&matrix)[4][4]) {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) { 
      cin >> matrix[i][j];  
    }
  }
}

int readCase(int n) {
  int row1,row2;
  int matrix1[4][4], matrix2[4][4];
  int numbers[17] = {0};  
  int found = 0, number = 0;

  cin >> row1;
  row1--;
  readMatrix(matrix1);
  cin >> row2;
  row2--;
  readMatrix(matrix2);
  
  for (int i = 0; i < 4; i++) {
    int num1 = matrix1[row1][i];
    int num2 = matrix2[row2][i];
    numbers[num1]++;
    numbers[num2]++;
    
    if (numbers[num1] > 1 && number != num1) {
      found++;
      number = num1;
    }
    if (numbers[num2] > 1 && number != num2) {
      found++;
      number = num2;
    }
  }
  
  string result;
  ostringstream convert;
  convert << number;    
  result = convert.str();  

  if (found == 1) {
    case_(n, result);
  } else if (found == 0) {
    case_(n, string("Volunteer cheated!"));
  } else if (found > 1) {
    case_(n, string("Bad magician!"));
  }
}

int main() {
  int cases;
  cin >> cases;
  for (int i = 0; i < cases; i++) {
    readCase(i+1);
  }
}
