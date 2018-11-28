#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    string s; cin >> s;

    map<char, int> freq;
    stringstream ss(s);

    char c;
    while (ss >> c) {
      if (!freq[c]) {
        freq[c] = 1;
      } else {
        freq[c]++;
      }
    }

    vector<int> num;
    while (freq['Z'] && freq['Z'] > 0) {
      num.push_back(0);
      freq['Z']--;
      freq['E']--;
      freq['R']--;
      freq['O']--;
    }

    while (freq['X'] && freq['X'] > 0) {
      num.push_back(6);
      freq['X']--;
      freq['S']--;
      freq['I']--;
    }

    while (freq['S'] && freq['S'] > 0) {
      num.push_back(7);
      freq['S']--;
      freq['E']--;
      freq['V']--;
      freq['E']--;
      freq['N']--;
    }

    while (freq['V'] && freq['V'] > 0) {
      num.push_back(5);
      freq['F']--;
      freq['I']--;
      freq['V']--;
      freq['E']--;
    }

    while (freq['F'] && freq['F'] > 0) {
      num.push_back(4);
      freq['F']--;
      freq['O']--;
      freq['U']--;
      freq['R']--;
    }

    while (freq['R'] && freq['R'] > 0) {
      num.push_back(3);
      freq['T']--;
      freq['H']--;
      freq['R']--;
      freq['E']--;
      freq['E']--;
    }

    while (freq['G'] && freq['G'] > 0) {
      num.push_back(8);
      freq['E']--;
      freq['I']--;
      freq['G']--;
      freq['H']--;
      freq['T']--;
    }

    while (freq['I'] && freq['I'] > 0) {
      num.push_back(9);
      freq['N']--;
      freq['I']--;
      freq['N']--;
      freq['E']--;
    }

    while (freq['N'] && freq['N'] > 0) {
      num.push_back(1);
      freq['O']--;
      freq['N']--;
      freq['E']--;
    }

    while (freq['T'] && freq['T'] > 0) {
      num.push_back(2);
      freq['T']--;
      freq['W']--;
      freq['O']--;
    }

    map<int, int> num_freq;
    for (int i = 0; i < 10; i++) {
      num_freq[i] = 0;
    }

    for (auto i : num) {
      num_freq[i]++;
    }

    for (int i = 0; i < 10; i++) {
      for (int n = 0; n < num_freq[i]; n++) {
        cout << i;
      }
    }

    cout << endl;
  }
  return 0;
}
