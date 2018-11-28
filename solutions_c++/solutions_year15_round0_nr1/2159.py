/*
 * Google Code Jam 2015. Qualification Eound. Problem A
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

string solve(string const & S)
{
  size_t standing = S[0] - '0';
  size_t to_come = 0;

  for (size_t shiness_level = 1; shiness_level != S.size(); ++shiness_level)
  {
    size_t const num_people = S[shiness_level] - '0';

    if (num_people != 0)
    {
      size_t now_coming = 0;
      if (standing < shiness_level)
      {
        now_coming = shiness_level - standing;
      }

      to_come += now_coming;
      standing += num_people + now_coming;
    }
  }

  return to_string(to_come);
}

int main()
{
  //FILE * res = std::freopen("small.in", "rt", stdin);
  //FILE * res = std::freopen("A-small-attempt0.in", "rt", stdin);
  FILE * res = std::freopen("A-large.in", "rt", stdin);
  assert(res);

  size_t T;
  cin >> T;

  for (size_t ci = 1; ci <= T; ++ci)
  {
    size_t Smax;
    cin >> Smax;
    string S;
    cin >> S;

    cout << "Case #" << ci << ": " << solve(S) << "\n";
  }
}
