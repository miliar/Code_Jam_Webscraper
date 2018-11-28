#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int t = 0;
long long p = 0, q = 0;

int PartElf() {
  int qq = q;

  while (qq % 2 == 0) {
    qq /= 2;
  }

  if (qq != 1) {
    return -1;
  }

  int result = 1;

  while (true) {
    if (2 * p >= q) {
      return result;
    }

    if (q % 2 == 1) {
      break;
    }

    q /= 2;
    result++;

    if (result > 40) {
      break;
    }
  }

  return -1;
}

int main() {
  cin >> t;

  for (int caseNum = 1; caseNum <= t; ++caseNum) {
    string part;

    cin >> part;

    stringstream partStream(part);
    string pStr, qStr;

    getline(partStream, pStr, '/');
    getline(partStream, qStr, '/');

    p = atoll(pStr.c_str());
    q = atoll(qStr.c_str());

    int result = PartElf();

    cout << "Case #" << caseNum << ": ";

    if (result > 0) {
      cout << result;
    } else {
      cout << "impossible";
    }

    cout << endl;
  }

  return 0;
}

