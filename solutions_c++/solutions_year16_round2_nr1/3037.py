#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

string solve(string s) {
  int size = s.size();

  string ans = "";

  int r[10] = { 0 }; 

  int found = -1;
  // check zero
  while ((found = s.find("Z")) != -1) {
    ++r[0];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("E"));
    s.erase(s.begin() + s.find("R"));
    s.erase(s.begin() + s.find("O"));
  }
  
  // check two
  while ((found = s.find("W")) != -1) {
    ++r[2];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("T"));
    s.erase(s.begin() + s.find("O"));
  }

  // check four
  while ((found = s.find("U")) != -1) {
    ++r[4];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("F"));
    s.erase(s.begin() + s.find("O"));
    s.erase(s.begin() + s.find("R"));
  }

  // check six
  while ((found = s.find("X")) != -1) {
    ++r[6];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("S"));
    s.erase(s.begin() + s.find("I"));
  }

  // check eight
  while ((found = s.find("G")) != -1) {
    ++r[8];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("E"));
    s.erase(s.begin() + s.find("I"));
    s.erase(s.begin() + s.find("H"));
    s.erase(s.begin() + s.find("T"));
  }

  // check one
  while ((found = s.find("O")) != -1) {
    ++r[1];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("N"));
    s.erase(s.begin() + s.find("E"));
  }

  // check three
  while ((found = s.find("T")) != -1) {
    ++r[3];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("H"));
    s.erase(s.begin() + s.find("R"));
    s.erase(s.begin() + s.find("E"));
    s.erase(s.begin() + s.find("E"));
  }

  // check five
  while ((found = s.find("F")) != -1) {
    ++r[5];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("I"));
    s.erase(s.begin() + s.find("V"));
    s.erase(s.begin() + s.find("E"));
  }

  // check seven
  while ((found = s.find("S")) != -1) {
    ++r[7];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("E"));
    s.erase(s.begin() + s.find("V"));
    s.erase(s.begin() + s.find("E"));
    s.erase(s.begin() + s.find("N"));
  }

  // check nine
  while ((found = s.find("N")) != -1) {
    ++r[9];
    s.erase(s.begin() + found);
    s.erase(s.begin() + s.find("I"));
    s.erase(s.begin() + s.find("N"));
    s.erase(s.begin() + s.find("E"));
  }

  for (int i = 0; i < 10; ++i) {
    for (int j = 0; j < r[i]; ++j) {
      ans = ans + to_string(i);
    }
  }

  return ans;
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; ++i) {
    string s;
    cin >> s;
    string ans = solve(s);

    cout << "Case #" << i + 1 << ": " << ans << "\n";
  }
}