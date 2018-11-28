#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <vector>

using namespace std;

int main() {
  int ncases;
  cin >> ncases;
  
  for (int c = 0; c < ncases; ++c) {
    cout << "Case #" << c + 1 << ": ";
    int A, B, K;
    cin >> A >> B >> K;
    int ncomb = 0;
    for (int i = 0; i < A; ++i) {
      for (int j = 0; j < B; ++j) {
        if ((i & j) < K) {
          //cout << i << " " << j << endl;
          ++ncomb;
        } 
      }
    }
    cout << ncomb << endl;
  }
  return 0;
}

