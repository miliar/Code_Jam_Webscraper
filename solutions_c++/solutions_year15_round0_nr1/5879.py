#include <iostream>
using namespace std;

int main() {

  int t;
  cin >> t;
  cerr << "Tests: " << t << endl;
  for (int i = 0 ; i < t ; ++i) {
    int smax;
    cin >> smax;
    cerr << "Smax: " << smax << endl;
    int sum = 0;
    int need = 0;
    for (int j = 0 ; j <= smax ; ++j) {
      char c;
      cin >> c;
      cerr << "'" << c << "'";
      int p = (c - '0');
      sum += p;
      if (sum + need <= j) need += j + 1 - sum - need;
    }
    cout << "Case #" << (i + 1) << ": " << need << endl;
  }
  return 0;
}

