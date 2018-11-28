#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void generate_count(long n) {
  if (n == 0) {
    cout << "INSOMNIA";
    return;
  }

  bool observedDigits[10] = { false };
  bool finished = false;
  long current = n;

  while (!finished) {

    long temp = current;
    while (temp > 0) {
      observedDigits[temp % 10] = true;
      temp /= 10;
    }

    finished = observedDigits[0];
    for (int i = 1; i < 10; i++) {
      finished = finished && observedDigits[i];
    }

    if (!finished) {
      current += n;
    }
  }

  cout << current;
}

int main() {
  string line;

  int cases;
  cin >> cases;

  for (int i = 0; i < cases; i++) {
    long n;
    cin >> n;
    cout << "Case #" << (i + 1) << ": ";
    generate_count(n);
    cout << "\n";
  }
}
