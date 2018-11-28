#include <iostream>
#include <string>

using namespace std;

string solve(const string &word) {
  if (word.length() <= 1) {
    return word;
  }

  // find latest letter
  // if more than one, pick last index
  char c = 'A';
  int index = 0;

  for (int i = 0; i < word.length(); i++) {
    if (word[i] >= c) {
      c = word[i];
      index = i;
    }
  }

  // last letter + solve(word up to last letter) + letters after last
  return string(1, c) + solve(word.substr(0, index)) + word.substr(index + 1);
}

int main() {
  int n;
  cin >> n;

  for (int i = 1; i <= n; i++) {
    string word;
    cin >> word;
    cout << "Case #" << i << ": " << solve(word) << "\n";
  }
}
