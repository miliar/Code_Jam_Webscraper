#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> counts(2600, 0);

void calc(string &s) {
    string res;
    vector<int> digits(10, 0);
    for (char c : s) {
       counts[c]++;
    }
    
   int tmp;
  //ZERO
  tmp = counts['Z'];
  counts['Z'] = 0;
  counts['E'] -= tmp; counts['R'] -= tmp; counts['O'] -= tmp; 
  digits[0] += tmp;

  //TWO
  tmp = counts['W'];
  counts['W'] = 0;
  counts['T'] -= tmp; counts['O'] -= tmp; digits[2] += tmp;

  //FOUR
  tmp = counts['U'];
  counts['U'] = 0;
  counts['F'] -= tmp; counts['O'] -= tmp; counts['R'] -= tmp;
  digits[4] = tmp;

  //SIX
  tmp = counts['X'];
  digits[6] = tmp;

  //EIGHT
  tmp = counts['G'];
  counts['H'] -= tmp;
  digits[8] = tmp;

  //THREE
  digits[3] = counts['R'];

  //ONE
  tmp = counts['O'];
  counts['N'] -= tmp;
  digits[1] = tmp;

  //FIVE
  digits[5] = counts['F'];
  counts['V'] -= digits[5];

  //SEVEN
  digits[7] = counts['V'];
  counts['N'] -= digits[7];

  //NINE
  digits[9] = counts['N'] / 2;

  unsigned sum = 4 * digits[0] + 3 * digits[2] + 4 * digits[4] + 3 * digits[6]
      + 5 * digits[8] + 5 * digits[3] + 3 * digits[1] + 4 * digits[5] + 5 * digits[7]
      + 4 * digits[9];
  if (sum != s.size()) {
     cout << s << " ";
  } 
  for (int num = 0; num < 10; num++) {
      for (int i = 0; i < digits[num]; i++) {
         cout << num;
      }
  } 
}

int main() {
    int testCases;
    string s; 
    cin >> testCases;

    for (int i = 1; i <= testCases; i++) {
        cin >> s;
        cout << "Case #" << i << ": ";
        calc(s);
        cout << endl;
        for (unsigned k = 0; k < counts.size(); k++) {
            counts[k] = 0;
        }
    }

    return 0;
}
