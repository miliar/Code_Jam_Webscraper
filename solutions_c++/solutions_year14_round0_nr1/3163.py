#include <iostream>
#include <fstream>

using namespace std;

int CheckCommon(int array1[], int array2[], int size);

const char* INPUT_FILE = "A-small-attempt0.in";
const char* OUTPUT_FILE = "a.out";

int main() {
  int test_cases;
  ifstream fin(INPUT_FILE);
  ofstream fout(OUTPUT_FILE);

  fin >> test_cases;
  int array1[4];
  int array2[4];
  int temp[4];
  for (int ix = 1; ix <= test_cases; ix++) {
    int left, right;
    fin >> left;
    for (int row = 1; row <= 4; row++) {
      for (int col = 0; col < 4; col++) {
        fin >> temp[col];
      }
      if (row == left) {
        for (int col = 0; col < 4; col++) {
          array1[col] = temp[col];
        }
      }
    }
    fin >> right;
    for (int row = 1; row <= 4; row++) {
      for (int col = 0; col < 4; col++) {
        fin >> temp[col];
      }
      if (row == right) {
        for (int col = 0; col < 4; col++) {
          array2[col] = temp[col];
        }
      }
    }
    int result = CheckCommon(array1, array2, 4);
    fout << "Case #" << ix << ": ";
    if (result == -1) {
      fout << "Bad magician!";
    } else if (result == 0) {
      fout << "Volunteer cheated!";
    } else {
      fout << result;
    }
    fout << endl;
  }
  fin.close();
  fout.close();

  return 0;
}

int CheckCommon(int array1[], int array2[], int size) {
  int count = 0;
  int find = -1;
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      if (array1[i] == array2[j]) {
        find = array1[i];
        count++;
      }
    }
  }
  if (count == 0)
    return 0;
  if (count > 1)
    return -1;
  return find;
}
