#include <iostream>
#include <string>

using namespace std;


int digitsCount[10];

bool allSeen() {
  for (int i = 0; i < 10; ++i) {
    if (digitsCount[i] == 0) return false;
  }
  return true;
}

void noteDigits(int n) {
  if (n == 0) digitsCount[0]++;
  while (n > 0) {
    int d = n%10;
    digitsCount[d]++;
    n /= 10;
  }
}
int main(int argc, char** argv) {
  int T;
  cin >> T;
  int t = 0;
  for (int t = 1; t <= T; ++t) {
    for (int i = 0; i < 10; ++i) {
      digitsCount[i] = 0;
    }

    int N;
    cin >> N;

    bool success = false;
    int num;
    if (N > 0) {
      for (int i = 1; not success; ++i) {
        num = i*N;
        noteDigits(num);
        if (allSeen()) {
          success = true;
        }
      }
    }

    string s = "INSOMNIA";
    if (success) s = to_string(num);
    cout << "Case #" << t << ": " << s << endl;
  }
  return 0;
}