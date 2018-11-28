#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    int K,C,S;
    cin >> K >> C >> S;
    string s = "";
    for (int i = 1; i <= K; i++) {
      s = s + " " + to_string(i);
    }
    cout << "Case #" << i << ": " << s << endl;
  }
}
