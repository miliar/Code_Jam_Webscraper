#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

void clean_counts(bool counts[]) {
  for (int i=0; i<10; i++) {
    counts[i] = false;
  }
}

bool all_seen(bool counts[]) {
  for (int i=0; i<10; i++) {
    if (!counts[i]) return false;
  }
  return true;
}

int main() {
  int cases = 0, seed = 0;
  long long current = 0, temp = 0;
  cin >> cases;

  bool counts[10] = {false};

  for (int i=1; i<=cases; i++) {
    clean_counts(counts);

    cin >> seed;

    if (seed == 0) {
      cout << "Case #" << i << ": INSOMNIA" << endl;
    } else {
      current = 0;

      while (!all_seen(counts)) {
        current += seed;
        temp = current;

        while (temp > 0) {
          counts[temp % 10] = true;
          temp /= 10;
        }
      }
      cout << "Case #" << i << ": " << current << endl;
    }
  }
}
