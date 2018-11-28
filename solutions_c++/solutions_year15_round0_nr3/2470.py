#include <cstdlib>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>


int table[4][4] = { {1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1} };


int sign(int x)
{
  return (x > 0) - (x < 0);
}


int mult(int q1, int q2)
{
  return sign(q1)*sign(q2)*table[std::abs(q1) - 1][std::abs(q2) - 1];
}


int inv(int q)
{
  if ( std::abs(q) == 1 )
    return q;
  return -q;
}



bool can_split(std::vector<char> const &digs)
{
  std::vector<size_t> b1;
  int q1 = 1;
  for ( size_t i = 0; i != digs.size(); ++i )
  {
    q1 = mult(q1, digs[i]);
    if ( q1 == 2 )
      b1.push_back(i);
  }
  std::vector<size_t> b2;
  int q3 = 1;
  for ( size_t i = digs.size(); i > 0; --i )
  {
    q3 = mult(digs[i - 1], q3);
    if ( q3 == 4 )
      b2.push_back(i - 1);
  }
  std::vector<char> so_far(digs.size());
  {
    int q = 1;
    for ( size_t i = 0; i != digs.size(); ++i )
    {
      q = mult(q, digs[i]);
      so_far[i] = q;
    }
  }
  std::reverse(b2.begin(), b2.end());
  for ( size_t i: b1 )
    for ( size_t j: b2 )
      if ( i + 1 < j )
      {
        int bq = mult(inv(so_far[i]), so_far[j - 1]);
        if ( bq == 3 )
          return true;
      }
  return false;
}


bool can_split(int x, std::string const &s)
{
  std::vector<char> digs;
  digs.reserve(x*s.length());
  for ( int i = 0; i < x; ++i )
    for ( size_t i = 0; i != s.length(); ++i )
    {
      char c = s[i];
      digs.push_back(c - 'i' + 2);
    }
  return can_split(digs);
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    int L, X;
    std::cin >> L >> X;
    std::string s;
    std::cin >> s;
    std::cout << "Case #" << t << ": " << (can_split(X, s) ? "YES\n" : "NO\n");
  }
  return 0;
}
