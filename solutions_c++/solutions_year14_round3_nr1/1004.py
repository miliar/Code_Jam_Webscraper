// mars.ma
#include <iostream>
#include <sstream>

using namespace std;

long long gcd(long long a, long long b) { return (!b ? a : gcd (b, a % b)); }

int main(void)
{
  int testcase;  cin >> testcase;
  string line;
  getline(cin, line);
  for (int tc = 1; tc <= testcase; ++tc) {
    getline(cin, line);
    string::size_type pos = line.find('/');
    line[pos] = ' ';
    istringstream iss(line);
    long long p, q;  iss >> p >> q;
    cout << "Case #" << tc << ": ";
    long long common = gcd(p, q);
    p /= common;
    q /= common;
    int result = 0;
    while (0 == q%2) {
      if (p < q) {
        result++;
      }
      q /= 2;
    }

    if (1 == q) {
      cout << result << endl;
    } else {
      cout << "impossible\n";
    }
  }
  return 0;
}

