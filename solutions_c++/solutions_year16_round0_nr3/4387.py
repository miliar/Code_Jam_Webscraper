#include <cassert>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

typedef unsigned long long ull;

struct Res {
  string num;
  ull divs[11];
};
typedef vector<Res> Ress;

void outputRes(ofstream & ofs, Res const & res) {
  ofs << res.num;
  for (int i = 2; i <= 10; ++i) {
    ofs << " " << res.divs[i];
  }
  ofs << endl;
}

void outputRess(ofstream & ofs, Ress const & ress) {
  for (int i = 0, n = ress.size(); i < n; ++i) {
    outputRes(ofs, ress[i]);
  }
}

string getStartNumStr(int n) {
  string numStr(n, '0');
  numStr[0] = '1';
  numStr[numStr.size() - 1] = '1';
  return numStr;
}

ull getNumInBase(string const & numStr, int base) {
  ull res = 0;
  ull mult = 1;
  for (int i = numStr.size() - 1; 0 <= i; --i) {
    if ('1' == numStr[i]) {
      res += mult;
    }
    mult *= base;
  }
  return res;
}

string getNextNum(string const & cur) {
  string next = cur;
  int i = cur.size() - 2;
  while (0 < i) {
    if ('0' == cur[i]) {
      next[i] = '1';
      return next;
    }
    next[i] = '0';
    --i;
  }
  return next;
}

void testGetNextNum() {
  assert("111" == getNextNum("101"));
  assert("1101" == getNextNum("1011"));
  assert("1011" == getNextNum("1001"));
  assert("11001" == getNextNum("10111"));
}

bool isPrime(ull const & num, ull * div) {
  for (ull i = 3, upper = num / i; i <= upper; ++i, upper = num / i) {
    if (0 == (num % i)) {
      *div = i;
      return false;
    }
  }
  return true;
}

bool isJamCoin(string const & numStr, Ress * ress) {
  Res res;
  for (int base = 2; base <= 10; ++base) {
    ull num = getNumInBase(numStr, base);
    ull div;
    if (isPrime(num, &div)) {
      cout << numStr << " is prime in base " << base
           << "(" << num << ")" << endl;
      return false;
    }
    res.divs[base] = div;
  }
  res.num = numStr;
  ress->push_back(res);
  return true;
}

void getJamCoins(int n, int j, Ress * ress) {
  string numStr = getStartNumStr(n);
  int found = 0;
  while (found < j) {
    if (isJamCoin(numStr, ress)) {
      ++found;
      cout << numStr << " is a jam coin. found " << found << endl;
    }
    numStr = getNextNum(numStr);
  }
}

void checkRes(Res const & res) {
  string const numStr = res.num;
  //cout << "checkRes num " << numStr << endl;
  for (int base = 2; base <= 10; ++base) {
    ull num = getNumInBase(numStr, base);
    ull div = res.divs[base];
    //cout << "base " << base << " num " << num << " div " << div << endl;
    assert(0 == (num % div));
  }
}

void checkRess(Ress const & ress) {
  for (int i = 0, n = ress.size(); i < n; ++i) {
    checkRes(ress[i]);
  }
}

int main(int argc, char * argv[]) {
  testGetNextNum();
  ifstream ifs(argv[1]);
  ofstream ofs((string(argv[1]) + ".out").c_str());
  int t;
  ifs >> t;
  for (int i = 0; i < t; ++i) {
    int n, j;
    ifs >> n >> j;
    Ress ress;
    getJamCoins(n, j, &ress);
    checkRess(ress);
    ofs << "Case #" << (i + 1) << ":" << endl;
    outputRess(ofs, ress);
  }
  return 0;
}
