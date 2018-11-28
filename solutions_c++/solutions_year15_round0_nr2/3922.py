#include <stdlib.h>
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int> num)
{
  if (num.empty()) {
    return 0;
  }

  sort(num.begin(), num.end(), greater<int>());
  if (num[0] <= 3) {
    return num[0];
  }

  vector<int> a;
  for (size_t i = 0; i < num.size(); i++) {
    if (num[i] > 1) {
      a.push_back(num[i] - 1);
    }
  }
  //cout << "a:\t";
  //for (size_t i = 0; i < a.size(); i++) {
  //  cout << a[i] << "\t";
  //}
  //cout << "\n";

  int ans = solve(a) + 1;

  for (int i = 4; i <= 9; i++) {
    for (size_t j = 0; j < num.size(); j++) {
      if (num[j] == i) {
        vector<int> b = num;
        b.erase(b.begin() + j);
        if (i == 4) {
          b.push_back(2);
          b.push_back(2);
        }
        if (i == 5) {
          b.push_back(2);
          b.push_back(3);
        }
        if (i == 6) {
          b.push_back(3);
          b.push_back(3);
        }
        if (i == 7) {
          b.push_back(3);
          b.push_back(4);
        }
        if (i == 8) {
          b.push_back(4);
          b.push_back(4);
        }
        if (i == 9) {
          b.push_back(3);
          b.push_back(6);
        }
        //if ((num[j] + 1) / 2 > 0) {
        //  b.push_back((num[j] + 1) / 2);
        //}
        //if (num[j] / 2 > 0) {
        //  b.push_back(num[j] / 2);
        //}
  
        //cout << "b:\t";
        //for (size_t i = 0; i < b.size(); i++) {
        //  cout << b[i] << "\t";
        //}
        //cout << "\n\n";
  
        ans = min(ans, solve(b) + 1);
        break;
      }
    }
  }

  return ans;
}

int main()
{
  int T;
  cin >> T;
  for (int count = 1; count <= T; count++) {
    int D;
    cin >> D;
    vector<int> num;
    for (int i = 0; i < D; i++) {
      int input;
      cin >> input;
      num.push_back(input);
    }
    cout << "Case #" << count << ": " << solve(num) << "\n";
  }
}

