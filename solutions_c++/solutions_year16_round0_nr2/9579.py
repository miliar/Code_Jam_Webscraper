#include <iostream>
#include <string>
using namespace std;

// Find the minimum flips for the top n pancakes.
int solve(std::bitset<128> s, int n) {
  if(n == 1) {
    // If there's only one pancake we must flip if it's not happy.
    return s[0] ? 0 : 1;
  }
  int cost = solve(s, n-1);
  // If we see a blank pancake following a happy one then we must make at least
  // two flips before all pancakes are happy.
  if(s[n-2] && !s[n-1]) {
    cost += 2;
  }
  return cost;
}

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for(int ca=0; ca<T; ++ca) {
    string S;
    cin >> S;
    int n = S.length();

    std::bitset<128> s;
    for(int i=0; i<S.length(); i++) {
      s[i] = (S[i] == '+');
    }

    cout << "Case #" << (ca+1) << ": " << solve(s,n) << "\n";
  }

  return 0;
}
