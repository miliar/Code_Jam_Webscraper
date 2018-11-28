#include <exception>
#include <iostream>
#include <string>
#include <vector>

#include <boost/dynamic_bitset.hpp>

using namespace std;

class no_solution_exception : logic_error {
  using logic_error::logic_error;
};

int minimizeFlips(const boost::dynamic_bitset<> &pancakes, int K) {
  boost::dynamic_bitset<> targetFlip = ~pancakes;
  int N = pancakes.size();
  int M = N - K + 1;            // # of possible flips
  vector<boost::dynamic_bitset<>> possibleFlips;
  possibleFlips.reserve(M);
  for (int i = 0; i < M; ++i) {
    boost::dynamic_bitset<> possibleFlip(N);
    for (int j = i; j < i + K; ++j) possibleFlip[j] = 1;
    possibleFlips.push_back(std::move(possibleFlip));
  }
  boost::dynamic_bitset<> currentFlip(N);
  int flips = 0;
  for (int i = 0; i < N; ++i) {
    if (targetFlip[i] != currentFlip[i]) {
      if (i >= M) throw no_solution_exception("No solution.");
      currentFlip ^= possibleFlips[i];
      ++flips;
    }
  }
  return flips;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    string S; cin >> S;
    boost::dynamic_bitset<> pancakes(S.length());
    for (int i = 0; i < S.length(); ++i) {
      if (S[i] == '+') pancakes[i] = 1;
    }
    int K; cin >> K;
    cout << "Case #" << t << ": ";
    try {
      cout << minimizeFlips(pancakes, K);
    } catch (no_solution_exception e) {
      cout << "IMPOSSIBLE";
    }
    cout << '\n';
  }
  cout << flush;
  return 0;
}
