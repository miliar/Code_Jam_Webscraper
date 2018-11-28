#include <algorithm>
#include <iostream>
#include <list>
#include <set>
#include <vector>

using namespace std;

vector<int> splitNumber(int number) {
  vector<int> v;
  if (0 == number) {
    v.push_back(0);
  } else {
    while (number != 0) {
      int last = number % 10;
      v.push_back(last);
      number = (number - last) / 10;
    }
  }
  return v;
}

int main() {
  int t, n, i = 1, aux;
  int lastN;
  bool b = false;
  vector<int> v;
  set<int> s;
  cin >> t;
  while (i <= t) {
    cin >> n;
    if (n == 0) {
      cout << "Case #" << i << ": INSOMNIA" << endl;
      i++;
    } else {
      b = false;
      aux = 1;
      while (s.size() < 10) {
        lastN = n * aux;
        v = splitNumber(lastN);
        for (int x : v) {
          s.insert(x);
        }
        aux++;
        if (aux > 100000) {
          b = true;
          break;
        }
      }
      if (b) {
        cout << "Case #" << i << ": INSOMNIA" << endl;
      } else {
        cout << "Case #" << i << ": " << lastN << endl;
      }
      s.clear();
      i++;
    }
  }
}
