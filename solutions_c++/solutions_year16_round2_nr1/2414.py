#include <bits/stdc++.h>

using namespace std;
int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large-att0.out", "w", stdout);
  int T;
  cin >> T;

  for(int t = 1; t <= T; ++t) {
    string s;
    string ans;
    cin >> s;
    //zero
     //it = find(s.begin(), s.end(), "Z");
    while(s.find("Z") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'Z'));
      s.erase(find(s.begin(), s.end(), 'E'));
      s.erase(find(s.begin(), s.end(), 'R'));
      s.erase(find(s.begin(), s.end(), 'O'));
      ans += "0";
    }

    //two
    while(s.find("W") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'T'));
      s.erase(find(s.begin(), s.end(), 'W'));
      s.erase(find(s.begin(), s.end(), 'O'));
      ans += "2";
    }

    //four
    while(s.find("U") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'F'));
      s.erase(find(s.begin(), s.end(), 'O'));
      s.erase(find(s.begin(), s.end(), 'U'));
      s.erase(find(s.begin(), s.end(), 'R'));
      ans += "4";
    }

    while(s.find("X") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'S'));
      s.erase(find(s.begin(), s.end(), 'I'));
      s.erase(find(s.begin(), s.end(), 'X'));
      ans += "6";
    }

    while(s.find("G") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'E'));
      s.erase(find(s.begin(), s.end(), 'I'));
      s.erase(find(s.begin(), s.end(), 'G'));
      s.erase(find(s.begin(), s.end(), 'H'));
      s.erase(find(s.begin(), s.end(), 'T'));
      ans += "8";
    }
    //one
    while(s.find("O") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'O'));
      s.erase(find(s.begin(), s.end(), 'N'));
      s.erase(find(s.begin(), s.end(), 'E'));
      ans += "1";
    }

    //three
    while(s.find("R") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'T'));
      s.erase(find(s.begin(), s.end(), 'H'));
      s.erase(find(s.begin(), s.end(), 'R'));
      s.erase(find(s.begin(), s.end(), 'E'));
      s.erase(find(s.begin(), s.end(), 'E'));
      ans += "3";
    }
    //five
    while(s.find("F") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'F'));
      s.erase(find(s.begin(), s.end(), 'I'));
      s.erase(find(s.begin(), s.end(), 'V'));
      s.erase(find(s.begin(), s.end(), 'E'));
      ans += "5";
    }
    //seven
    while(s.find("S") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'S'));
      s.erase(find(s.begin(), s.end(), 'E'));
      s.erase(find(s.begin(), s.end(), 'V'));
      s.erase(find(s.begin(), s.end(), 'E'));
      s.erase(find(s.begin(), s.end(), 'N'));
      ans += "7";
    }
    while(s.find("N") != string::npos) {
      s.erase(find(s.begin(), s.end(), 'N'));
      s.erase(find(s.begin(), s.end(), 'I'));
      s.erase(find(s.begin(), s.end(), 'N'));
      s.erase(find(s.begin(), s.end(), 'E'));
      ans += "9";
    }
    sort(ans.begin(), ans.end());
    cout << "Case #"<<t<<": " << ans<<'\n';
  }
}
