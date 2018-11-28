#include <iostream>
#include <vector>
#include <algorithm>


int score(std::vector<int> const &c, std::vector<int> const &f)
{
  int N = f.size();
  while ( N > 1 )
  {
    bool good = true;
    for ( int i = 0; i < N; ++i )
    {
      if ( i < N - 1 )
      {
        if ( f[c[i]] == c[i + 1] )
          continue;
      }
      else if ( f[c[i]] == c[0] )
        continue;
      if ( i > 0 )
      {
        if ( f[c[i]] == c[i - 1] )
          continue;
      }
      else if ( f[c[i]] == c[N - 1] )
        continue;
      good = false;
      break;
    }
    if ( good )
      return N;
    --N;
  }
  return 0;
}


int brute(std::vector<int> const &f)
{
  int N = f.size();
  std::vector<int> c(N);
  for ( int i = 0; i < N; ++i )
    c[i] = i;
  int best = 0;
  do
  {
    best = std::max(best, score(c, f));
  } while ( std::next_permutation(c.begin(), c.end()) );
  return best;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    int N;
    std::cin >> N;
    std::vector<int> f(N);
    for ( int i = 0; i < N; ++i )
    {
      std::cin >> f[i];
      --f[i];
    }
    std::cout << "Case #" << t << ": " << brute(f) << '\n';
  }
  return 0;
}
