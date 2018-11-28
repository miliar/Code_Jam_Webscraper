#include <iostream>
#include <fstream>

using namespace std;

inline toInt(char val) { return val - 48; }

int main() {
  int T;
  cin >> T;

  ofstream ofs("solution.out");
  if (ofs.fail()) {
    cout << "Fail to open file" << endl;
    return -1;
  }
  
  
  for (int i = 0; i < T; i++) {
    int SMax;
    cin >> SMax;
    string S;
    cin >> S;
    int friends_to_invide = 0;
    int people_clapping = 0;
    cout << "Case #" << i + 1 << endl;
    for (int j = 0; j <= SMax; j++) {
      if (people_clapping < j || (j == 0 && toInt(S[j]) == 0)) {
        friends_to_invide++;
        people_clapping++;
        cout << "Inviting friend i=" << j << " and Si=" << S[j] << endl;
      }
      people_clapping += toInt(S[j]);
    }
    cout << "----------------------------------------" << endl;
    ofs << "Case #" << i + 1 << ": " << friends_to_invide << "\n";
  }
  
  ofs.flush();
  ofs.close();

  return 0;
}