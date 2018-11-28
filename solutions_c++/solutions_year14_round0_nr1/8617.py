#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

void PrintAnswer(int case_num, string answer) {
  cout << "Case #" << case_num << ": " << answer << endl;
}

string MagicTrick(ifstream &ifs) {
  stringstream answer;

  // read probrem
  int ansA;
  ifs >> ansA;

  int rowA[4][4];
  for (int i = 0; i < 4; i++)
    ifs >> rowA[i][0] >> rowA[i][1] >> rowA[i][2] >> rowA[i][3];

  int ansB;
  ifs >> ansB;

  int rowB[4][4];
  for (int i = 0; i < 4; i++)
    ifs >> rowB[i][0] >> rowB[i][1] >> rowB[i][2] >> rowB[i][3];

#if 0
  // debug
  cout << ansA << endl;

  for (int i = 0; i < 4; i++)
    cout << rowA[i][0] << " " << rowA[i][1] << " " << rowA[i][2] << " " << rowA[i][3] << endl;

  cout << ansB << endl;

  for (int i = 0; i < 4; i++)
    cout << rowB[i][0] << " " << rowB[i][1] << " " << rowB[i][2] << " " << rowB[i][3] << endl;
#endif


  // answer
  int count = 0;
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      if (rowA[ansA-1][i] == rowB[ansB-1][j]) {
        answer << rowA[ansA-1][i];
        count++;
      }

  if (count == 0)
    return "Volunteer cheated!";
  else if (count == 1)
    return answer.str();

  return "Bad magician!";
}

int main(int argc, char *argv[]) {
  ifstream ifs(argv[1]);
  int case_sum = 0;

  ifs >> case_sum;

  for (int i = 1; i <= case_sum; i++) {
    PrintAnswer(i, MagicTrick(ifs));
  }
}
