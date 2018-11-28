#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>


int n_pref(std::vector<std::string> const &words)
{
  std::set<std::string> p;
  for ( auto &w : words )
  {
    for ( size_t i = 0; i <= w.length(); ++i )
      p.insert(w.substr(0, i));
  }
  return p.size();
}


bool good(int N, std::vector<int> const &part)
{
  std::vector<char> pres(N);
  for ( auto p: part )
    pres[p] = 1;
  for ( auto c: pres )
    if ( c != 1 )
      return false;
  return true;
}


bool ending(int N, std::vector<int> const &part)
{
  for ( auto p: part )
    if ( p != N - 1 )
      return false;
  return true;
}


std::pair<int, int> get_max(int N, std::vector<std::string> const &words)
{
  std::vector<int> part(words.size());
  std::vector<std::vector<std::string>> servers(N);
  int worst = 0, wc = 0;
  do
  {
    if ( good(N, part) )
    {
      for ( auto &s: servers )
        s.clear();
      for ( size_t i = 0; i != words.size(); ++i )
        servers[part[i]].push_back(words[i]);
      int np = 0;
      for ( auto &s: servers )
        np += n_pref(s);
      if ( np == worst )
        ++wc;
      else if ( np > worst )
      {
        wc = 1; worst = np;
      }
    }
    if ( ending(N, part) )
      break;
    for ( size_t i = 0; i != part.size(); ++i )
    {
      ++part[i];
      if ( part[i] <= N - 1 )
        break;
      part[i] = 0;
    }
  } while ( true );
  return std::make_pair(worst, wc);
}



std::pair<int, int> solve()
{
  int M, N;
  std::cin >> M >> N;
  std::vector<std::string> words(M);
  for ( int i = 0; i < M; ++i )
    std::cin >> words[i];
  return get_max(N, words);
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    auto p = solve();
    std::cout << "Case #" << t << ": " << p.first << ' ' << p.second << '\n';
  }
  return 0;
}
