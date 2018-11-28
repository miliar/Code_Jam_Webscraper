#include <iostream>
#include <cstring>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <cmath>
#include <map>
#include <cassert>
#include "windows.h"
using namespace std;

bool compute_result(size_t row, size_t col, size_t** data)
{
  for (size_t j = 0; j < row; ++j) {
    for (size_t k = 0; k < col; ++k) {
      size_t val = data[j][k];
      bool row_yes = true;
      for (size_t l = 0; l < col; ++l){
        if (data[j][l] > val) {
          row_yes = false;
          break;
        }
      }
      if (!row_yes) {
        for (size_t l = 0; l < row; ++l){
          if (data[l][k] > val) {
            return false;
          }
        }
      }
    }
  }
  return true;
}

int main(int argc, char* argv[])
{
  if (argc < 2) exit(1);
  string s;
  ifstream inFile(argv[1], ios::in);
  getline(inFile, s);
  istringstream ss(s);
  size_t count;
  ss >> count;
  for (size_t i = 0; i < count; ++i) {
    getline(inFile, s);
    size_t k, n;
    ss.clear();
    ss.str(s);
    ss >> k >> n;
    size_t **data = new size_t* [k];
    for (size_t j = 0; j < k; ++j) {
      data[j] = new size_t[n];
      getline(inFile, s);
      ss.clear();
      ss.str(s);
      for (size_t k = 0; k < n; ++k)
        ss >> data[j][k];
    }
    /*
    cout << "k = " << k << " n = " << n << '\n';
    for (size_t j = 0; j < k; ++j)
      for (size_t k = 0; k < n; ++k) {
        cout << "data["<<j<<"]["<<k<<"] = " << data[j][k] << '\n';
      }
      */
    bool res = compute_result(k, n, data);
    if (res)
      cout << "Case #" << (i+1) << ": " << "YES" << '\n';
    else
      cout << "Case #" << (i+1) << ": " << "NO" << '\n';
  }
  return 0;
}
