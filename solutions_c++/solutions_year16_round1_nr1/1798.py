#include <iostream>
#include <string>

using namespace std;

string solve(string str) {
  string result = "";
  result += str[0];

  for(int i = 1; i < str.size(); i += 1) {
    if(result[0] > str[i]) {
      result += str[i];
    } else {
      result = str[i] + result;
    }
  }

  return result;
}

int main()
{
  int n;
  cin >> n;

  string str;
  for(int i = 1; i <= n; i += 1) {
    cin >> str;
    cout << "Case #" << i << ": " << solve(str) << endl;
  }

  return 0;
}
