#include <iostream>
#include <vector>
#include <cmath>

typedef unsigned long long ull;
using namespace std;


int main() {
  ull T; cin >> T;
  for (ull i = 1; i <= T; ++i) {
    ull K, C, S;
    cin >> K >> C >> S;
    cout << "Case #" << i << ":";
    ull step = pow(K,C-1);
    for (ull i = 1; i <= S; ++i) {
      cout << " " << (i * step) - (step-1); 
    }
    cout << "\n";
  }
}
