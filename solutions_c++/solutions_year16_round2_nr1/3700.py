#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <stdlib.h>


using namespace std;

#define PI acos(-1.)
#define EPS 1e-7
#define LL long long
#define U unsigned int
#define LU long unsigned
#define LLU long long unsigned



string digits[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string nums[10] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

bool check(string digit, map<char, int> &chars) {
  for (int i = 0; i < digit.size(); i++) {
    if (chars.find(digit[i]) == chars.end()) {
      return false;
    }
  }
  return true;
}

bool next_digit(int pos, map<char, int> &chars, string &res) {
  if (chars.size() == 0) return true;
  if (pos >= 10) {
    return false;
  }
  
  for (int j = pos; j < 10; j++) {
    if (!check(digits[j], chars)) continue;
    
    for (int i = 0; i < digits[j].size(); i++) {
      chars[digits[j][i]]--;
      if (chars[digits[j][i]] == 0) {
        chars.erase(digits[j][i]);
      }
    }
    if (next_digit(j, chars, res)) {
      res += nums[j];
      return true;
    } else {
      for (int i = 0; i < digits[j].size(); i++) {
        chars[digits[j][i]]++;
      }
      continue;
    }
  }
  return false;
}

int main() {
  // Declare members
  int num_case;
  cin >> num_case;
  
  string S;
  
  for (int nc = 1; nc <= num_case; ++nc) {
    // Init members
    cin >> S;
  
    map<char, int> chars;
    for (int i = 0; i < S.size(); i++) {
      chars[S[i]]++; 
    }
    string res = "";
    next_digit(0, chars, res);
    
    for (int i = 0; i < res.size() - i - 1; i++) {
      swap(res[i], res[res.size() - i - 1]);
    }

    // Print output for case j
    cout << "Case #" << nc << ": " << res << endl;
  }


  return 0;
}
