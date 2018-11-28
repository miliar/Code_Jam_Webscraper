#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

void find_erase(string& S, char c) {
  S.erase(std::find(S.begin(), S.end(),c));
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    int digits[10];
    memset(&digits, 0, 10*sizeof(int));
    string S;
    cin >> S;
    while (S.find('Z') != string::npos) {
      find_erase(S, 'Z');
      find_erase(S, 'E');
      find_erase(S, 'R');
      find_erase(S, 'O');
      digits[0]++;
    }
    while (S.find('W') != string::npos) {
      find_erase(S, 'W');
      find_erase(S, 'T');
      find_erase(S, 'O');
      digits[2]++;
    }
    while (S.find('U') != string::npos) {
      find_erase(S, 'F');
      find_erase(S, 'U');
      find_erase(S, 'O');
      find_erase(S, 'R');
      digits[4]++;
    }
    while (S.find('X') != string::npos) {
      find_erase(S, 'S');
      find_erase(S, 'I');
      find_erase(S, 'X');
      digits[6]++;
    }
    while (S.find('G') != string::npos) {
      find_erase(S, 'E');
      find_erase(S, 'I');
      find_erase(S, 'G');
      find_erase(S, 'H');
      find_erase(S, 'T');
      digits[8]++;
    }
    while (S.find('O') != string::npos) {
      find_erase(S, 'O');
      find_erase(S, 'N');
      find_erase(S, 'E');
      digits[1]++;
    }
    while (S.find('R') != string::npos) {
      find_erase(S, 'E');
      find_erase(S, 'R');
      find_erase(S, 'E');
      find_erase(S, 'H');
      find_erase(S, 'T');
      digits[3]++;
    }

    while (S.find('F') != string::npos) {
      find_erase(S, 'F');
      find_erase(S, 'I');
      find_erase(S, 'V');
      find_erase(S, 'E');
      digits[5]++;
    }
    while (S.find('S') != string::npos) {
      find_erase(S, 'S');
      find_erase(S, 'E');
      find_erase(S, 'V');
      find_erase(S, 'E');
      find_erase(S, 'N');
      digits[7]++;
    }
    if (!S.empty()) {
      digits[9] = S.size() / 4;
    }
    cout << "Case #" << i << ": ";
    for (int i = 0; i < 10; i++) {
      while (digits[i]--) {
        cout << i;
      }
    }
    cout << "\n";
  }

  return 0;
}

