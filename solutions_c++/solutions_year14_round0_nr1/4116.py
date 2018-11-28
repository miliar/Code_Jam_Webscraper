#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

void readMatrix(int mat[4][4], int rows, int cols){
  int n;
  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      cin >> n;
      mat[i][j] = n;
    }
  }
}
void solveCase(int n){
  int rowA, rowB, answer;
  int mat[4][4];
  set<int> A, B, choices;

  cin >> rowA;
  readMatrix(mat, 4, 4);
  for(int i = 0; i<4; i++) A.insert(mat[rowA-1][i]);

  cin >> rowB;
  readMatrix(mat, 4, 4);
  for(int i = 0; i<4; i++) B.insert(mat[rowB-1][i]);

  std::set_intersection(A.begin(), A.end(), B.begin(), B.end(),
          std::inserter(choices, choices.end()));

  switch(choices.size()){
    case 0: answer = -1; break; // Volunteer cheated
    case 1: answer = *choices.begin(); break; // ANSWER
    default: answer = 0; break;
  }

  cout << "Case #" << n << ": ";
  if(answer > 0) cout << answer << endl;
  else if(answer == 0) cout << "Bad magician!" << endl;
  else cout << "Volunteer cheated!" << endl;
}

int main(int argc, char** argv){
  int T;
  cin >> T;
  for(int i=0; i<T; i++){
    solveCase(i+1);
  }
  return 0;
}
