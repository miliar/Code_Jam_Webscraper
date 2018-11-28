#include <iostream>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int npeople, friends = 0, shysum = 0, f;
    string audience;
    cin >> npeople >> audience;
    for (int i = 0; i <= npeople; i++) {
      f = max(i - shysum, 0);
      shysum += audience[i]-'0' + f;
      friends += f;
    }
    cout << "Case #" << t << ": " << friends << endl;
  }
  return 0;
}