#include <iostream>
#include <string>

using namespace std;

int countFlips(string pancakes) {
  // pancakes are top to bottom
  // + signifies happy side, - signifies sad side  
  int N = pancakes.length();
  int flips = 0;
  for (int i = 1; i < N; ++i) {
    if (pancakes[i] != pancakes[i-1]) ++flips;
  }
  if (pancakes.back() == '-') ++flips;
  return flips;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);
  int T; cin >> T;
  for (int t = 0; t < T; ++t) {
    string pancakes; cin >> pancakes;
    cout << "Case #" << (t+1) << ": "
         << countFlips(pancakes)
         << '\n';
  }
  cout << flush;
  return 0;
}
