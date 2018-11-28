#include <iostream>

using namespace std;

void extract(string const &word, unsigned int count[256]) {
  unsigned int u, word_count[256] = { 0 };

  for(unsigned char c : word) {
    ++word_count[c];
  }

  for(u = 0; u < 256; ++u) {
    count[u] -= word_count[u];
  }
}

void task() {
  string s;
  unsigned int u, count[256] = { 0 };
  unsigned int digits[10] = { 0 };

  cin >> s;

  for(unsigned char c : s) {
    ++count[c];
  }

  while(count['Z'] > 0) {
    extract("ZERO", count);
    ++digits[0];
  }

  while(count['W'] > 0) {
    extract("TWO", count);
    ++digits[2];
  }

  while(count['U'] > 0) {
    extract("FOUR", count);
    ++digits[4];
  }

  while(count['R'] > 0) {
    extract("THREE", count);
    ++digits[3];
  }

  while(count['X'] > 0) {
    extract("SIX", count);
    ++digits[6];
  }

  while(count['G'] > 0) {
    extract("EIGHT", count);
    ++digits[8];
  }

  while(count['O'] > 0) {
    extract("ONE", count);
    ++digits[1];
  }

  while(count['F'] > 0) {
    extract("FIVE", count);
    ++digits[5];
  }

  while(count['V'] > 0) {
    extract("SEVEN", count);
    ++digits[7];
  }

  digits[9] = count['I'];

  for(unsigned u = 0; u < 10; ++u) {
    while(digits[u] > 0) {
      --digits[u];
      cout << u;
    }
  }
}

int main(int argc, char **argv) {
  unsigned int u, T;

  cin >> T;

  for(u = 1; u <= T; ++u) {
    cout << "Case #" << u << ": ";
    task();
    cout << endl;
  }

  return 0;
}
