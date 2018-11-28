#include <iostream>
#include <deque>
#include <algorithm>


int n_discs(int cap, std::deque<int> &files)
{
  std::sort(files.begin(), files.end());
  int r = 0;
  while ( not files.empty() )
  {
    ++r;
    int f1 = files.back();
    files.pop_back();
    if ( files.empty() )
      return r;
    int rem = cap - f1;
    if ( rem <= 0 )
      continue;
    size_t lo = 0, hi = files.size() - 1;
    if ( files[lo] > rem )
      continue;
    if ( files[hi] <= rem )
    {
      files.pop_back();
      continue;
    }
    while ( lo + 1 < hi )
    {
      // files[lo] <= rem < files[hi]
      size_t med = lo + (hi - lo)/2;
      if ( files[med] <= rem )
        lo = med;
      else
        hi = med;
    }
    files.erase(files.begin() + lo);
  }
  return r;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    int N, X;
    std::cin >> N >> X;
    std::deque<int> f(N);
    for ( int i = 0; i < N; ++i )
      std::cin >> f[i];
    std::cout << "Case #" << t << ": " << n_discs(X, f) << '\n';
  }
  return 0;
}
