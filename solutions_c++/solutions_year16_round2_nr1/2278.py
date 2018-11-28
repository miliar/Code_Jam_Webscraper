#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int main() {
  int data_size = 0;
  in >> data_size;
  for (int i = 0; i < data_size; ++i) {
    string number("");
    vector<int> answer(10, 0);
    in >> number;
    for (int j = 0; j < number.length(); ++j) {
      switch (number[j]) {
        case 'Z':
          ++answer[0];
          break;
        case 'O':
          ++answer[1];
          break;
        case 'W':
          ++answer[2];
          break;
        case 'H':
          ++answer[3];
          break;
        case 'R':
          ++answer[4];
          break;
        case 'V':
          ++answer[5];
          break;
        case 'X':
          ++answer[6];
          break;
        case 'S':
          ++answer[7];
          break;
        case 'G':
          ++answer[8];
          break;
        case 'I':
          ++answer[9];
          break;
        default:
          break;
      }
    }
//    cout << "\n" << i << ":";
//    for (int j = 0; j < 10; ++j) {
//      cout << answer[j];
//    }
//    cout << "\n";
    answer[3] -= answer[8];
    answer[4] -= (answer[0] + answer[3]);
    answer[1] -= (answer[4] + answer[2] + answer[0]);
    answer[7] -= answer[6];
    answer[5] -= answer[7];
    answer[9] -= (answer[8] + answer[6] + answer[5]);
    out << "Case #" << i + 1 << ": ";
    for (int j = 0; j < answer.size(); ++j) {
      if (answer[j] > 0) {
        for (int k = 0; k < answer[j]; ++k) {
          out << j;
        }
      }
    }
    out << "\n";
  }
  return 0;
}
