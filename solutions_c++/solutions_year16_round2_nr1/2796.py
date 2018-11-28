#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm> 
using namespace std;
typedef long long ll;

int main() {
  int n;
  cin >> n;
  for (int j = 1; j <= n; j++) {
  
  string s;
  cin >> s;
  map<char, int> countmap;
  for (int i = 0; i < s.length(); i++) {
    countmap[s[i]]++;
  }

  vector<string> num = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
  vector<int> order = { 0, 6, 4, 7, 2, 8, 5, 9, 1, 3};

  string phone;
  int i = 0;
  while (true) {
    string number = num[order[i]];
    bool possible = true;
    map<char, int> countc = countmap;
    for (auto ch : number) {
      if (countc[ch] == 0) {
        possible = false;
      }
      countc[ch]--;
    }
    if (possible) {
      for (auto ch : number) {
        countmap[ch]--;
      }
      phone.push_back(order[i] + '0');
    } else {
      i++;
      if (i == 10) {
        break;
      }
    }
  }
  sort(phone.begin(), phone.end());
  cout << "Case #" << j << ": " << phone << endl;
  }

  return 0;
}
