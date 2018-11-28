#include <algorithm>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <list>
#include <queue>

using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;
using li = list<int>;
using ll = long long;

#define rep(i, n) for (int i = 0; i < n; i++)
#define repa(i, s, e) for (int i = s; i <= e; i++)
#define repd(i, s, e) for (int i = s; i >= e; i--)

bool can_solve(int X, int R, int C)
{
  if (X == 1)
  {
    return true;
  }
  else
  {
    if (R == 1 && C == 1)
    {
      return false;
    }
    else if ((R == 2 && C == 1) || (R == 1 && C == 2))
    {
      return (X == 2);
    }
    else if ((R == 3 && C == 1) || (R == 1 && C == 3))
    {
      return false;
    }
    else if ((R == 4 && C == 1) || (R == 1 && C == 4))
    {
      return (X == 2);
    }
    else if (R == 2 && C == 2)
    {
      return (X == 2);
    }
    else if ((R == 2 && C == 3) || (R == 3 && C == 2))
    {
      return (X == 2 || X == 3);
    }
    else if ((R == 2 && C == 4) || (R == 4 && C == 2))
    {
      return (X == 2);
    }
    else if (R == 3 && C == 3)
    {
      return (X == 3);
    }
    else if ((R == 3 && C == 4) || (R == 4 && C == 3))
    {
      return (X == 2 || X == 3 || X == 4);
    }
    else if (R == 4 && C == 4)
    {
      return (X == 2 || X == 4);
    }
  }

  return false;
}

int main()
{
  cin.tie(0);
  ios::sync_with_stdio(false);

  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    int X, R, C;
    cin >> X >> R >> C;

    cout << "Case #" << (i + 1) << ": "
         << (can_solve(X, R, C) ? "GABRIEL" : "RICHARD") << endl;
  }
}
