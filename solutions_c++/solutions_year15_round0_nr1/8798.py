#include <iostream>
#include <string>

using namespace std;

int char2int(char ch) {
  return (int)(ch - '0');
}

int solve(int digit, string str)
{
  int total = char2int(str[0]);
  int dif = 0;
  int val;

  for(int i = 1; i <= digit; i += 1) {
    if(i > total) {
      val = i - total;
      dif += val;
      total += val;
    }

    total += char2int(str[i]);
  }

  return dif;
}

int main()
{
  int tc;
  cin >> tc;

  int digit;
  string str;
  for(int i = 1; i <= tc; i+=1) {
    cin >> digit >> str;
    cout << "Case #" << i << ": " << solve(digit, str) << endl;
  }

  return 0;
}
