#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>

using namespace std;

template<typename T>
ostream& operator<<(ostream& ost, const vector<T> &vec)
{
  ost << "[";
  for (auto val : vec)
  {
    ost << val << ", ";
  }
  ost << "]";
  return ost;
}


int gcd(int x, int y)
{
  if (x == 0|| y == 0) return 1;

  if (x == y) return x;
  if (x > y) return gcd(x-y,y);
  if (x < y) return gcd(x, y-x);
}


int main ()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    int P, Q;
    char temp;
    cin >> P >> temp >> Q;

    int count = 0;
    int real_count = 0;

    cout << "Case #"<< i+1 << ": ";

    int gc = gcd(P,Q);
    P = P/gc;
    Q = Q/gc;

    bool ok = true;
    int T = Q;
    while (T != 1)
    {
      if (T%2 != 0)
      {
        ok = false;
        break;
      }
      T = T / 2;
    }

    if (ok)
    {
      int count = 0;
      while (P < Q) Q/=2, count++;
      cout << count << endl;
    } else {
      cout << "impossible" << endl;
    }

  }

  return 0;
}
