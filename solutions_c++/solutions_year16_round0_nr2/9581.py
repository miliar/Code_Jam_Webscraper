#include <iostream>
#include <string>

using namespace std;

int solve(string s)
{
  int count = 0;

  if(s.back() == '-') {
    count += 1;
  }

  for(int i = 0; i < s.size() -1; i += 1) {
    if(s[i] == s[i+1]) {
      continue;
    }

    count += 1;
  }

  return count;
}

int main()
{
  int tc;
  cin >> tc;

  string s;
  for(int i =1; i <= tc; i += 1) {
    cin >> s;
    cout << "Case #" << i << ": " << solve(s) << endl;
  }

  return 0;
}
