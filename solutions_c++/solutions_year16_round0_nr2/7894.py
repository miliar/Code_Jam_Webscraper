#include <iostream>
#include <string>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  
  long n;
  cin >> n;
  for (long i = 0; i < n; ++i) {
    string in;
    cin >> in;
    bool start = 1, chain = 0;
    long tot = 0;
    for (char c : in) {
      bool v = c == '+';
      if (!v) {
        if (!chain) {
          tot += 2 - start;
          chain = 1;
        }
      } else { chain = 0; }
      start = 0;
    }
    cout << "Case #" << i+1 << ": " << tot << "\n";
  }
  
}
