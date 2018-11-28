#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int N;
string x[100];
string y[100];
vector<int> z[100];

int main() {
  int T;
  cin >> T;
  for (int times = 1; times <= T; ++times) {
    int A, B, K;
    cin >> A >> B >> K;
    int nb = 0;
    if((K >= A) && (K >= B)) {
      nb = A*B;
    } else if((K < A) && (K >= B)) {
      nb = A*B;
    } else if((K >= A) && (K < B)) {
      nb = A*B;
    } else {
      // K < A, K < B
      nb += A*K;
      nb += K*(B - K);
      for(int i = K; i < A; ++i) {
        for(int j = K; j < B; ++j) {
          if((i&j) < K) ++nb;
        }
      }
    }
    cout << "Case #" << times << ": " << nb << endl;
  }
  return 0;
}
