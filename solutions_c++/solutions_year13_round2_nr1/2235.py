#include <cmath>
#include <iostream>
#include <list>
#include <sstream>
#include <string>
using namespace std;

long long process(const long long A, list<long long> m, const long long y);

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  for (int x = 0; x < T; x++)
  {
    long long A, N;
    list<long long> m;
    cin >> A >> N;
    for (long long n = 0; n < N; n++)
    {
      long long s;
      cin >> s;
      m.push_back(s);
    }
    m.sort();
    cout << "Case #" << (x + 1) << ": " << process(A, m, 0) << endl;
  }

  return 0;
}

long long process(const long long A, list<long long> m, const long long y)
{
  long long a = A, Y[2];

  while (!m.empty() && a > m.front())
  {
    a += m.front();
    m.pop_front();
  }
  if (m.empty())
  {
    return y;
  }
  else
  {
    list<long long> M[2] = {m, m};
    if (a > 1)
    {
      long long n = a - 1;
      M[0].push_front(n);
      Y[0] = process(a, M[0], y+1);
      M[0].clear();
    }
    M[1].pop_back();
    Y[1] = process(a, M[1], y+1);
    M[1].clear();
    return (a > 1 && Y[0] < Y[1])?Y[0]:Y[1];
  }
}
