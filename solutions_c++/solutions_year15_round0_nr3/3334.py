#include <string>
#include <iostream>
#include <cmath>
using namespace std;


int a[4][4] = {
  {1,  2,  3,  4},
  {2, -1,  4, -3},
  {3, -4, -1,  2},
  {4,  3, -2, -1},
};

int convert2(int num1, int num2) {
  int anum1 = fabs(num1);
  int anum2 = fabs(num2);
  return (anum1 / num1) * (anum2 / num2) * a[anum1-1][anum2-1];
}



int convert(int anum, char b) {
  int num = fabs(anum);
  switch (b) {
    case 'i':
      return (num / anum) * a[num - 1][1];
      break;
    case 'j':
      return (num / anum) * a[num - 1][2];
      break;
    case 'k':
      return (num / anum) * a[num - 1][3];
      break;
  }
  return -1;
}


bool get(const string &str, int x) {
  string res;
  for (int i = 0; i < min(x, 8); i++) {
    res += str;
  }
  int i = 0, value = 1;
  for (; i < res.length(); i++) {
    value = convert(value, res[i]);
    if (value == 2) break;
  }
  value = 1; i++;
  for (; i < res.length(); i++) {
    value = convert(value, res[i]);
    if (value == 3) return true;
  }
  return false;
}


int total(const string &str, int x) {
  int value = 1;
  for (int i = 0; i < str.length(); i++) {
    value = convert(value, str[i]);
  }
  x %= 4;
  int avalue = 1;
  while (x--) avalue = convert2(avalue, value);
  return avalue;
}


int main() {
  int testCases;
  cin >> testCases;
  for (int testCase = 1; testCase <= testCases; testCase++) {
    int l, x;
    cin >> l >> x;
    string str;
    cin >> str;
    cout << "Case #" << testCase << ": ";
    if (get(str, x) && total(str, x) == -1) {
      cout << "YES\n";
    } else {
      cout << "NO\n";
    }
  }
  return 0;
}
