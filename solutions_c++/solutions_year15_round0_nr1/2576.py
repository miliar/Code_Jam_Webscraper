#include <iostream>
#include <vector>

using namespace std;

int solve(int smax, const vector<int> &ss) {
  int invited = 0;
  int standing = 0;

  for(int i = 0; i < ss.size(); i++) {
    if(standing < i) {
      int required = i - standing;
      invited += required;
      standing += required;
    }
    standing += ss[i];
  }

  return invited;
}

int main() {
  int T;
  cin >> T;

  for(int i = 1; i <= T; i++) {
    int smax;
    string ss_str;
    vector<int> ss;

    cin >> smax;
    cin >> ss_str;

    for(char si : ss_str) {
      ss.push_back(si - '0');
    }

    int sol = solve(smax, ss);

    cout << "Case #" << i << ": " << sol << endl;
  }

  return 0;
}
