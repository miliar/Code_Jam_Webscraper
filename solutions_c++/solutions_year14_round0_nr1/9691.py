#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <iostream>
#include <climits>
#include <string>
#include <cmath>
#include <assert.h>
#include <unordered_map>
#include <sstream>
#include <stack>
#include <unordered_set>
#include <bitset>
#include <time.h>
#include <cstring>
#include <set>
#include <list>

using namespace std;

vector<int> overlap (const vector<int> &A, const vector<int> &B) {
    vector<int> result;
    result.clear();
    unordered_set<int> dict;
    for(int i = 0; i < A.size(); i++) {
        dict.insert(A[i]);
    }
    for(int i = 0; i < B.size(); i++) {
        if(dict.find(B[i]) != dict.end())
            result.push_back(B[i]);
    }
    return result;
}

int main() {
  //freopen ("C:\\Users\\Case\\Desktop\\A-small-attempt0.in", "r", stdin);
  //freopen ("C:\\Users\\Case\\Desktop\\A-small-attempt0.out", "w", stdout);
  int N, index1, index2, var;
  cin >> N;
  vector<int> A, B;
  for(int round = 0; round < N; round++) {
      A.clear();
      B.clear();
      cin >> index1;
      for(int row = 0; row < 4; row++) {
            for(int col = 0; col < 4; col++) {
                cin >> var;
                if(row == index1 - 1)
                    A.push_back(var);
            }
      }
      cin >> index2;
      for(int row = 0; row < 4; row++) {
            for(int col = 0; col < 4; col++) {
                cin >> var;
                if(row == index2 - 1)
                    B.push_back(var);
            }
      }
      //now A and B holds the two rows
      vector<int> result = overlap(A, B);
      if(result.size() == 1)
        cout << "Case #" << (round + 1) << ": " << result[0] << endl;
      else if(result.size() == 0)
        cout << "Case #" << (round + 1) << ": Volunteer cheated!" << endl;
      else
        cout << "Case #" << (round + 1) << ": Bad magician!" << endl;
  }
  return 0;
}
