#include <string>
#include <iostream>


int needed(std::string const &s)
{
  int n = 0;
  int standing = 0;
  for ( int i = 0; i < int(s.length()); ++i )
  {
    int d = s[i] - '0';
    if ( d > 0 && i > standing )
    {
      int x = i - standing;
      n += x;
      standing += x;
    }
    standing += d;
  }
  return n;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    std::string x;
    int s;
    std::cin >> s >> x;
    std::cout << "Case #" << t << ": " << needed(x) << '\n';
  }
  return 0;
}
