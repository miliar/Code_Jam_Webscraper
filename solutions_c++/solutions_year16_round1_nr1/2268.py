#include <iostream>
#include <string>
#include <deque>


std::string last_word(std::string const &w)
{
  std::deque<char> q;
  for ( auto c: w )
  {
    if ( q.empty() || q.front() > c )
      q.push_back(c);
    else
      q.push_front(c);
  }
  std::string r;
  for ( auto c: q )
    r.push_back(c);
  return r;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    std::string w;
    std::cin >> w;
    std::cout << "Case #" << t << ": " << last_word(w) << '\n';
  }
  return 0;
}
