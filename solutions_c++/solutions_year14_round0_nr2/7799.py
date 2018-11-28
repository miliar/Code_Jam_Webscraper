#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t < T; ++t) {
    double C, F, X;
    cin >> C >> F >> X;
    // first farm
    cout << setprecision(7) << fixed;
    vector<double> s(100001, 0.0);
    s[0] = 0;
    for (int i = 1; i <= ceil(X); ++i) {
      s[i] = C/(2.0+(i-1)*F) + s[i-1]; 
    }
    vector<double> pt(100001, X);
    for (int i = 1; i <= ceil(X); ++i) {
      pt[i] = X/(2.0+(i-1)*F) + s[i-1]; 
    }
    
    cout << "Case #" << t+1 << ": " << 
      *min_element(pt.begin(), pt.end()) << endl;
  }

  return 0;
}
