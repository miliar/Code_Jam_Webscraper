#include <iostream>
#include <string>
using namespace std;
char S[2001];

int main() {
  int T, j = 1;
  cin >> T;
  while (T--) {
    int start = 1000, end = 1000;
    string s;
    cin >> s;
    S[start] = s[0];
    end++;
    for (int i = 1; i < s.length(); i++) {
      if (s[i] >= S[start]) {
        S[--start] = s[i];
      } else {
        S[end++] = s[i];
      }
    }
    cout << "Case #" << j++ << ": "; 
    for (int i = start; i < end; i++)
      cout << S[i];
    cout << endl;
  }

  return 0;
}

