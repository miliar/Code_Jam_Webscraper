#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);

  for(int cases = 1; cases <= T; cases++) {
    int smax;
    int res = 0;
    string shyness;
    cin >> smax >> shyness;
    int stood_so_far = 0;
    // at ith shyness, there should be atleast i people.
    for (int i = 0; i < shyness.size(); i++) {
      int num_added = 0;
      if (stood_so_far < i) {
        // Add these people to make the ith guy stand up.
        num_added = i - stood_so_far;
      }

      stood_so_far += shyness[i] - '0' + num_added;
      res += num_added;
    }
    printf("Case #%d: %d\n", cases, res);
  }

  return 0;
}
