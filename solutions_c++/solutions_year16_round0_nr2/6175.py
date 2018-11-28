#include <iostream>

using namespace std;

int flip(string &str) {
  int count = 0;
  for (int i = 1; i < str.size(); i++)
  {
    if (str[i] != str[i-1])
      count ++;
  }
  if (str.back() == '-')
    count ++;

  return count;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    string S;
    cin >> S;
    int n = flip(S);
    cout << "Case #" << i << ": " << n << endl;
  }
}
