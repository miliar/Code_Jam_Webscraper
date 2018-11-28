#include <iostream>

using namespace std;

void solve(string pancakes, int K) {
  int c = 0;
  for(int i = 0; i < pancakes.size() - K + 1; ++i) {
    if(pancakes[i] == '-') {
      c++;
      for(int j = i; j < i + K; ++j) {
        pancakes[j] = pancakes[j] == '+' ? '-' : '+';
      }
    }
  }
  for(int i = 0; i < pancakes.size(); ++i) {
    if(pancakes[i] != '+') {
      cout << "IMPOSSIBLE";
      return;
    }
  }
  cout << c;
}

int main() {

  int T;
  cin >> T;

  for(int i = 0; i < T; ++i) {
    cout << "Case #" << (i+1) << ": ";
    string pancakes;
    int K;
    cin >> pancakes >> K;
    solve(pancakes, K);
    cout << endl;
  }

  return 0;
}
