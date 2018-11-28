#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <time.h>
#include <cassert>
#include <algorithm>
using namespace std;

vector<int> getIntArray(ifstream& fin, int nNonEmpty);
void print(const vector<int>& arr);
void getArrayStatus(const vector<int>& arr, int &maximum, int &secondMax, int &nMaximum);

int gogo(vector<int> &arr, int level, int max_step);

inline int max(int x, int y, int z) {
  return max(max(x, y), z);
}

int main(int argc, char* argv[]) {
  if (argc != 2) {
    printf("Usage: %s input-file\n", argv[0]);
    return -1;
  }

  ifstream fin(argv[1]);

  int nCases;
  fin >> nCases;

  for (int i=0; i<nCases; ++i) {
    int nNonEmpty;
    fin >> nNonEmpty;

    vector<int> arr = getIntArray(fin, nNonEmpty);
#ifdef DEBUG
    printf("\n===== Case #%d =====\n      ", i);
#endif
    print(arr);
    
    // int steps = 0;
    int maximum, secondMax, nMaximum;
    getArrayStatus(arr, maximum, secondMax, nMaximum);
    
    int MM = maximum;
    int steps = gogo(arr, 0, maximum);

    assert(steps <= MM);
#ifdef DEBUG
    printf("\33[36mCase #%d: %d\33[0m\n", i + 1, steps);
#else
    printf("Case #%d: %d\n", i + 1, steps);
#endif
  }

  return 0;
}

int gogo(vector<int> &arr, int level, int max_step) {

  int max_idx = std::max_element(arr.begin(), arr.end()) - arr.begin();
  int maximum = arr[max_idx];

  int best_step = maximum;

  for (int i=ceil(double(maximum) / 2); i>=2 ; --i) {

    auto backup = arr;
    arr[max_idx] = i;
    arr.push_back(maximum - i);

    int step;

    if (level < max_step)
      step = gogo(arr, level + 1, max_step) + 1;
    else
      step = *max_element(arr.begin(), arr.end()) + level;

    if (step < best_step)
      best_step = step;

    arr = backup;
  }

  return best_step;
}

void print(const vector<int>& arr) {
#ifdef DEBUG
  printf("\33[33m[ %d", arr[0]);
  for (int i=1; i<arr.size(); ++i)
    printf(" %d", arr[i]);
  printf(" ]\33[0m: ");
#endif
}

void getArrayStatus(const vector<int>& arr, int &maximum, int &secondMax, int &nMaximum) {
  maximum = arr[0];
  nMaximum = 1;
  secondMax = -1;

  for (int i=1; i<arr.size(); ++i) {
    if (arr[i] > maximum) {
      secondMax = maximum;
      maximum = arr[i];
      nMaximum = 1;
    }
    else if (arr[i] == maximum)
      ++nMaximum;
    else if (arr[i] > secondMax)
      secondMax = arr[i];
  }
#ifdef DEBUG
  printf("maximum = \33[36m%d\33[0m, secondMax = \33[36m%d\33[0m, nMaximum = \33[36m%d\33[0m\n", maximum, secondMax, nMaximum);
#endif
}

vector<int> getIntArray(ifstream& fin, int nNonEmpty) {
  vector<int> arr;
  int p;
  for (int i=0; i<nNonEmpty; ++i) { 
    fin >> p;
    arr.push_back(p);
  }
  return arr;
}

void find_max_and_how_many_max(const vector<int> &arr, int &maximum, int &nMaximum) {
}
