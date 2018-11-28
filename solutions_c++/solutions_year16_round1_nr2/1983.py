#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {

  if (argc != 3) {
    cout << "Useage: a.out file_in file_out" << endl;
    return -1;
  }


  ifstream file_in;
  ofstream file_out;
  file_in.open(argv[1]);
  file_out.open(argv[2]);

  int T;
  int N;

  int min;
  int min_count;
  int min_1, min_2;
  int max;

  file_in >> T;

  for (int t = 1; t <= T; t++) {
    file_in >> N;
    vector<vector<int>> lists(2 * N - 1, vector<int>(N, 0));
    vector<vector<int>> matrix(N, vector<int>(N, 0));
    vector<int> result;
    min = 2501;
    min_count = 0;
    max = 0;

    for (int i = 0; i < 2 * N - 1; i++) {
      for (int j = 0; j < N; j++) {
        file_in >> lists[i][j];
      }
    }

    int index = -1;
    while (min_count != 1) {
      cout << "Here" << endl;
      index++;
      min = 2501;
      for (int j = 0; j < 2 * N - 1; j++) {
        if (min > lists[j][index] && lists[j][index] > max) {
          min = lists[j][index];
          min_count = 1;
          min_1 = j;
        }
        else if (min == lists[j][index]){
          min_count ++;
          min_2 = j;
        }
      }

      if (index == N-1) {
        break;
      }
      if (min_count == 1) {
        break;
      }
      if (max < lists[min_1][index+1])
        max = lists[min_1][index+1];
      
      if (max < lists[min_2][index+1])
        max = lists[min_2][index+1];
         

    }
    cout << "index = " << index << endl;
    // This must be true;
    if (min_count == 1) {
      for (int i = 0; i < 2 * N - 1; i++) {
        result.push_back(lists[i][index]);
      }
      sort(result.begin(), result.end());

      int j = 0;
      for (int i = 0; i < N; i++) {
        while (lists[min_1][i] > result[j]) {
          j++;
        }
        if (lists[min_1][i] == result[j]) {
          cout << "Erase" << *(result.begin() + j) << endl;
          result.erase(result.begin()+j);
        }
      }

      cout << "Case #" << t << ": ";
      file_out << "Case #" << t << ": ";

      for (int i = 0; i < index; i++) {
        cout << result[i] << " ";
        file_out << result[i] << " ";
      }
      cout << min << " ";
      file_out << min << " ";
      for (int i = index; i < N-1; i++) {
        cout << result[i] << " ";
        file_out << result[i] << " ";
      }
      cout << endl;
      file_out << endl;
    }


  }

  file_in.close();
  file_out.close();
  return 0;
}
