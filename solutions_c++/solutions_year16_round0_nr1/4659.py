#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void mark(const string &n, vector<bool> &seen)
{
  for (int i = 0; i < (int) n.length(); ++i)
  {
    seen[ n[i] - '0' ] = true;
  }
}

string a;

bool seen_all_digits(vector<bool> &seen)
{
  for (int i = 0; i < (int) seen.size(); ++i)
    if ( !seen[i] ) return false;

  // cerr << "seen returning true for " << a << endl;
  return true;
}

string next(const string &input)
{
  string num = input;
  reverse(num.begin(), num.end());

  int n = num.length();
  int m = a.length();

  string res = "";
  int sum = 0;
  int carry = 0;
  for (int i = 0; i < m; ++i)
  {
    sum = carry + a[i] - '0' + num[i] - '0';
    carry = sum / 10;
    sum = sum % 10;

    res = (char)(sum + '0') + res;
  }

  for (int i = m; i < n; ++i)
  {
    sum = carry + num[i] - '0';
    carry = sum / 10;
    sum = sum % 10;

    res = (char)(sum + '0') + res;
  }

  if (carry > 0) res = (char)(carry + '0') + res;

  return res;
}

int main(int argc, char ** argv)
{
  int tests; cin >> tests;

  for (int tc = 0; tc < tests; ++tc)
  {
    vector<bool> seen(10, false);

    string n; cin >> n;
    a = n;
    reverse(a.begin(), a.end());

    cout << "Case #" << (1 + tc) << ": ";

    if (n == "0")
    {
      cout << "INSOMNIA" << endl;
      continue;
    }

    while (true)
    {
      mark(n, seen);

      // cerr << "checking " << n << endl;

      if (seen_all_digits(seen))
        break;

      n = next(n);
    };

    cout << n << endl;
  }

  return 0;
}
