#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <utility>

void solve(int c)
{
  unsigned A, N;
  unsigned ops = 0;
  std::multiset<unsigned> motes;

  std::cout << "Case #" << c << ": ";

  std::cin >> A >> N;
  for (unsigned i = 0; i < N; ++i)
  {
    unsigned M;
    std::cin >> M;
    motes.insert(M);
  }
#if 0
  for (auto i = motes.begin(); i != motes.end() && *i < A; i = motes.begin())
  {
    A += *i;
    motes.erase(i);
  }

  for (auto i = motes.begin(); i != motes.end() && *i < A+A-1; i = motes.begin())
  {
    A += A-1;
    A += *i;
    ++ops;
    motes.erase(i);
  }

  if (motes.empty())
  {
    std::cout << ops << std::endl;
    return;
  }

  std::cout << "====";
#endif
  // If there are still motes, we need to figure out if it is more
  // efficient to remove the remaining motes or to add smaller motes
  // repeatedly. Going to use DP here.

  unsigned total_add_ops = 0;
  unsigned best_so_far = 0;

  for (auto i = motes.begin(); i != motes.end(); ++i)
  {
    unsigned add_ops = 0;

    // Find out how many add operations we need.
    while (A <= *i && add_ops < motes.size())
    {
      A += A - 1;
      ++add_ops;
    }
    A += *i;

    // If the number of of operations required to absorb this mote is
    // greater than the number of remaining motes, just remove all the
    // remaining motes.
    if (std::distance(i, motes.end()) <= add_ops)
    {
      total_add_ops += std::distance(i, motes.end());
      break;
    }
    else
    {
      total_add_ops += add_ops;
    }
  }

  std::cout << ops + total_add_ops << std::endl;
}


int main()
{
  int N;
  std::cin >> N;

  for (int i = 1; i <= N; ++i)
    solve(i);
}
