#include <iostream>
#include <list>
using namespace std;

char multiply(char c1, char c2)
{
  if (c1 < 0) {
    return -multiply(-c1, c2);
  }
  if (c2 < 0) {
    return -multiply(c1, -c2);
  }
  if (c1 > c2) {
    return -multiply(c2, c1);
  }
  if (c1 == 1) {
    return c2;
  }
  if (c1 == c2) {
    return -1;
  }
  if (c1 == 'i') {
    if (c2 == 'j') {
      return 'k';
    }
    if (c2 == 'k') {
      return char(-int('j'));
    }
  }
  if (c1 == 'j') {
    if (c2 == 'k') {
      return 'i';
    }
  }
  return 0;
}


int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int x;
    cin >> x >> x;
    string s;
    cin >> s;
    char targets[4] = {'i', 'j', 'k', 1};
    char n = 0;
    // char tgt = targets[n];
    char curt = 1;
    for (int j = 0; j < x; ++j) {
      for (int k = 0; k < s.size(); ++k) {
        curt = multiply(curt, s[k]);
        if (curt == targets[n]) {
          curt = 1;
          if (n < 3) {
            ++n;
          }
        }
      }
    }

    cout << "Case #" << i+1 << ": ";
    if (curt == 1 && n == 3) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
