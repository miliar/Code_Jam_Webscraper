#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <map>
#include <sstream>
#include <string>
using namespace std;

unsigned long minFlips(string stack) {
  unsigned long nTransitions = 0;
  for (int i = 0; i < stack.size() - 1; i++) {
    if (stack[i] != stack[i + 1]) {
      nTransitions++;
    }
  }

  if (nTransitions == 0) return (stack[0] == '+' ? 0 : 1);

  if (stack[stack.size() - 1] == '-') {
    return nTransitions + 1;
  }

  return nTransitions;
}

int main() {
  int t;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; i++) {
    string stack;
    cin >> stack;

    cout << "Case #" << i << ": " << minFlips(stack) << endl;
  }
}
