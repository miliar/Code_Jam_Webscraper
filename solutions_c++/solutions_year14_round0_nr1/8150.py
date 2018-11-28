#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

size_t array1[4][4];
size_t array2[4][4];
size_t ans1, ans2;
size_t num;

char* result[2] = {
  "Bad magician!",
  "Volunteer cheated!"
};

size_t get_result()
{
  size_t *res1 = array1[ans1-1];
  size_t *res2 = array2[ans2-1];
  int same_cnt = 0;
  for (size_t i = 0; i < 4; ++i) {
    size_t anchor = res1[i];
    for(size_t j = 0; j < 4; ++j) {
      if (anchor == res2[j]) {
        ++same_cnt;
        num = anchor;
      }
    }
  }
  return(same_cnt == 1)? 1:
    (same_cnt > 1)? 2:
    (same_cnt == 0)? 3: 4;
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
    ss.clear();
    ss.str(s);
    ss >> ans1;
    for (size_t j = 0; j < 4; ++j) {
      getline(inFile, s);
      ss.clear();
      ss.str(s);
      ss >> array1[j][0] >> array1[j][1] >> array1[j][2] >> array1[j][3];
    }
    getline(inFile, s);
    ss.clear();
    ss.str(s);
    ss >> ans2;
    for (size_t j = 0; j < 4; ++j) {
      getline(inFile, s);
      ss.clear();
      ss.str(s);
      ss >> array2[j][0] >> array2[j][1] >> array2[j][2] >> array2[j][3];
    }

    size_t res = get_result();
    assert(res != 4);
    if (res == 1)
      cout << "Case #" << (i+1) << ": " << num << '\n';
    else
      cout << "Case #" << (i+1) << ": " << result[res-2] << '\n';
  }
  return 0;
}

