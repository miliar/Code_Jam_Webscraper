/*
 * Google Code Jam 2015. Qualification Eound. Problem B
 * Vladimir Rutsky
 * 11.04.2014
 */

#include <iostream>
#include <algorithm>
#include <array>
#include <iterator>
#include <set>
#include <cassert>
#include <vector>
#include <cstdio>
#include <map>

using namespace std;

string solve(vector<size_t> const & P)
{
  size_t const max_h = *std::max_element(P.begin(), P.end());
  size_t min_time = max_h;

  for (size_t lim = 1; lim != max_h; ++lim)
  {
    size_t time = lim;

    for (size_t i = 0; i != P.size(); ++i)
    {
      size_t const h = P[i];
      if (h > lim)
      {
        size_t const dt = ceil((double)h / lim) - 1;
        time += dt;
      }
    }

    if (time < min_time)
    {
      min_time = time;
    }
  }

  return to_string(min_time);
}

int main()
{
  //FILE * res = std::freopen("small.in", "rt", stdin);
  //FILE * res = std::freopen("B-small-attempt0.in", "rt", stdin);
  FILE * res = std::freopen("B-large.in", "rt", stdin);
  assert(res);

  size_t T;
  cin >> T;

  for (size_t ci = 1; ci <= T; ++ci)
  {
    size_t D;
    cin >> D;

    vector<size_t> P;
    for (size_t i = 0; i != D; ++i)
    {
      size_t pi;
      cin >> pi;
      P.push_back(pi);
    }

    cout << "Case #" << ci << ": " << solve(P) << "\n";
  }
}
