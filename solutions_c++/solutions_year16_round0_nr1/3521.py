#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const char IN_FILE[] = "input.txt";
const char OUT_FILE[] = "output.txt";
const int MAX_N = 1000000;

int LastSeen[MAX_N + 1];

inline int solve(const int n) {
  vector<bool> seen = vector<bool>(10, 0);
  int seenCount = 0, steps = 0;
  while (seenCount < 10) {
    ++steps;
    for (int x = n * steps; x > 0; x /= 10) {
      if (!seen[x % 10]) {
        seen[x % 10] = true;
        ++seenCount;
      }
    }
  }
  return steps * n;
}

void preprocess() {
  LastSeen[0] = -1;
  for (int n = 1; n <= MAX_N; ++n)
    LastSeen[n] = solve(n);
}

int main() {
  preprocess();

  ifstream cin(IN_FILE);
  ofstream cout(OUT_FILE);

  int testCount;
  cin >> testCount;
  for (int test = 1; test <= testCount; ++test) {
    int n;
    cin >> n;
    cout << "Case #" << test << ": ";
    if (LastSeen[n] == -1)
      cout << "INSOMNIA\n";
    else
      cout << LastSeen[n] << "\n";
  }

  cin.close();
  cout.close();
  return 0;
}
