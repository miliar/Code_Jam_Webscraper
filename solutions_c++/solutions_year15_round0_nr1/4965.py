#include <iostream>
#include <string>
using namespace std;

int main() {
  int testCases;
  cin >> testCases;
  for (int testCase = 1; testCase <= testCases; testCase++) {
    int n;
    string str;
    cin >> n >> str;
    int sum = 0, count = 0;
    for (int i = 0; i <= n; i++) {
      while (sum < i) {
        count++;
        sum++;
      }
      sum += str[i] - '0';
    }
    cout << "Case #" << testCase << ": " << count << "\n";
  }
  return 0;
}
