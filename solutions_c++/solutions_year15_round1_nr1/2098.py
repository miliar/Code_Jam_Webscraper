#include <stdio.h>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;

int main(void) {
  int numCases;
  cin >> numCases;

  for (int cases = 0; cases < numCases; cases++) {
    int N;
    cin >> N;

    vector<int> table;
    for (int i = 0; i < N; i++) {
      int temp;
      cin >> temp;
      table.push_back(temp);
    }
    int max = 0;
    for (int i = 1; i < N; i++) {
      max = table[i-1] - table[i] > max ? table[i-1] - table[i] : max;
    }

    int acm1 = 0, acm2 = 0;
    for (int i = 0; i < N-1; i++) {
      acm1 += table[i] > table[i+1] ? table[i] - table[i+1] : 0;
      acm2 += table[i] < max ? table[i] : max;
    }

    printf("Case #%d: %d %d\n", cases+1, acm1, acm2);
  }

  return 0;
};
