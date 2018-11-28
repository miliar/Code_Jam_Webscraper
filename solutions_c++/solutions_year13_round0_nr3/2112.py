#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
typedef vector<long long> VLL;

string to_string(int i) {
  string result;
  while (i) {
    result = (char)( (i % 10) + '0') + result;
    i /= 10;
  }
  return result;
}

long long to_ll(string s) {
  long long result = 0;
  for (int i = 0; i < s.length(); ++i) {
    result *= 10;
    result += (s[i] - '0');
  }
  return result;
}

string complete_palindrome(string x, bool odd) {
  string result = "";
  for (int i = x.length() - 1; i >= 0; --i) {
    result += x[i];
  }
  for (int i = (odd ? 1 : 0); i < x.length(); ++i) {
    result += x[i];
  }
  return result;
}

bool ispalindrome(string x) {
  return (x.length() == 1 || x.length() == 0 ||
          (x[0] == x[x.length()-1] && ispalindrome(x.substr(1, x.length()-2))));
}

int main() {
  // up to four digits -> 7 total
  VLL fairnsquare;
  for (long long i = 1; i < 10000; ++i) {
    long long guess = to_ll(complete_palindrome(to_string(i), true));
    if (ispalindrome(to_string(guess*guess))) {
      fairnsquare.push_back(guess*guess);
    }
  }

  // up to three digits -> 6 total
  for (long long i = 1; i < 1000; ++i) {
    long long guess = to_ll(complete_palindrome(to_string(i), false));
    if (ispalindrome(to_string(guess*guess))) {
      fairnsquare.push_back(guess*guess);
    }
  }

  sort(fairnsquare.begin(), fairnsquare.end());

  int t; cin >> t;
  for (int test = 1; test <= t; ++test) {
    long long a, b; cin >> a >> b; // fix for large
    VLL::iterator low, high;
    low = lower_bound(fairnsquare.begin(), fairnsquare.end(), a);
    high = upper_bound(fairnsquare.begin(), fairnsquare.end(), b);
    cout << "Case #" << test << ": " << (high - low) << endl;
  }
  return 0;
}