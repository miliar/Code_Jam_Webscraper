#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <queue>
using namespace std;


int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    string s;
    cin >> s;
    s.push_back('+');
    int a = 0;
    for (int j = 0; j < s.length()-1; ++j)
      if (s[j] != s[j+1])
        a++;
    cout << "Case #" << i << ": " << a << endl;
  }
}
