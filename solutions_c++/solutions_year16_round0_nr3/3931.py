#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int check_prime(string num)
{
  // cerr << "checking " << num << " for primality" << endl;

  int n = num.length();
  long long ret = 0;
  for (int i = 0; i < n; ++i)
  {
    ret *= 10;
    ret += (num[i] - '0');
  }

  for (int i = 2; i <= sqrt(ret); ++i)
  {
    if (ret % i == 0) return i;
  }

  // cerr << num << " is a prime" << endl;

  return -1;
}

string convert_to(int base, string num)
{
  string res = "";
  int n = num.length();

  long long ret = 0;
  for (int i = 0 ; i < n; ++i)
  {
    ret *= base;
    ret += (num[i] - '0');
  }

  while (ret > 0)
  {
    res = (char)((ret % 10) + '0') + res;
    ret /= 10;
  }

  return res;
}

vector<int> factorize(string num)
{
  vector<int> ret(10 - 2 + 1);

  for (int base = 2; base <= 10; ++base)
  {
    string candidate = convert_to(base, num);

    // cerr << num << " in base " << base << " is " << candidate << endl;

    int rc = check_prime(candidate);

    if (rc == -1) return vector<int>(0);

    ret[base - 2] = rc;
  }

  return ret;
}

string _next(string num)
{
  // cerr << "looking for next number after: " << num << endl;

  reverse(num.begin(), num.end());
  int n = num.length();

  string res= "";
  int sum = 0;
  int carry = 1;

  for (int i = 0; i < n; ++i)
  {
    sum = carry + num[i] - '0';
    carry = sum / 2;
    sum = sum % 2;

    res = (char)(sum + '0') + res;
  }

  if (carry > 0) res = (char)(carry + '0') + res;

  return res;
}

string next(string num)
{
  num = _next(num);
  while (num[num.length() - 1] != '1') num = _next(num);
  return num;
}

void solve(int n, int j)
{
  string num = "1";
  for (int i = 0; i < n - 1; ++i)
  {
    num += '0';
  }

  num = next(num);
  while (((int)num.length() < n + 1) && j)
  {
    // cerr << "checking for: " << num << endl;
    vector<int> factors = factorize(num);

    if (factors.size() != 0)
    {
      cout << num;
      for (int i = 0; i < (int) factors.size(); ++i)
      {
        cout << " " << factors[i];
      }
      cout << endl;

      --j;
    }
    else
    {
      // cerr << num << " is prime" << endl;
    }

    num = next(num);
  }
}

int main(int argc, char ** argv)
{
  int tests; cin >> tests;

  for (int tc = 0; tc < tests; ++tc)
  {
    int n, j; cin >> n >> j;

    cout << "Case #" << (1 + tc) << ":" << endl;
    solve(n, j);
  }

  return 0;
}