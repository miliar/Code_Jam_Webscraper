/*
 * Google Code Jam 2015. Qualification Eound. Problem C
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

enum numbers_t {
  N1 = 0,
  NI,
  NJ,
  NK,
  N_1,
  N_I,
  N_J,
  N_K
};

numbers_t const mult_table[16][16] =
  {
    { N1,  NI,  NJ,  NK, N_1, N_I, N_J, N_K},
    { NI, N_1,  NK, N_J, N_I,  N1, N_K,  NJ},
    { NJ, N_K, N_1,  NI, N_J,  NK,  N1, N_I},
    { NK,  NJ, N_I, N_1, N_K, N_J,  NI,  N1},
    {N_1, N_I, N_J, N_K,  N1,  NI,  NJ,  NK},
    {N_I,  N1, N_K,  NJ,  NI, N_1,  NK, N_J},
    {N_J,  NK,  N1, N_I,  NJ, N_K, N_1,  NI},
    {N_K, N_J,  NI,  N1,  NK,  NJ, N_I, N_1},
  };

template<class FwdIt>
numbers_t mult(FwdIt first, FwdIt beyond)
{
  numbers_t res = N1;
  for (; first != beyond; ++first)
  {
    res = mult_table[res][*first];
  }

  return res;
}

numbers_t power(numbers_t n, size_t power)
{
  switch (power % 4)
  {
    case 0:
      return N1;
    case 1:
      return n;
    case 2:
      return mult_table[n][n];
    case 3:
      return mult_table[mult_table[n][n]][n];
  }

  assert(false);
  return N1;
}


template<class FwdIt>
size_t find_mult_idx(FwdIt first, FwdIt beyond, numbers_t num, bool reverse = false)
{
  numbers_t cur_mult = N1;
  size_t i = 0;
  for (; first != beyond; ++i, ++first)
  {
    if (reverse)
    {
      cur_mult = mult_table[*first][cur_mult];
    }
    else
    {
      cur_mult = mult_table[cur_mult][*first];
    }

    if (cur_mult == num)
    {
      return i;
    }
  }

  return i;
}

string solve(vector<numbers_t> const & nums, size_t X)
{
  numbers_t const single_mult = mult(nums.begin(), nums.end());
  numbers_t const total_mult = power(single_mult, X);

  if (total_mult != N_1)
  {
    return "NO";
  }

  if (X <= 8)
  {
    vector<numbers_t> rep_nums;
    for (size_t i = 0; i != X; ++i)
    {
      rep_nums.insert(rep_nums.end(), nums.begin(), nums.end());
    }

    size_t const i_idx = find_mult_idx(rep_nums.begin(), rep_nums.end(), NI);
    size_t const k_rev_idx = find_mult_idx(rep_nums.rbegin(), rep_nums.rend(), NK, true);
    if (i_idx == rep_nums.size() || k_rev_idx == rep_nums.size())
      return "NO";
    size_t const k_idx = rep_nums.size() - 1 - k_rev_idx;
    if (i_idx >= k_idx)
      return "NO";

    assert(mult(rep_nums.begin(), rep_nums.end()) == N_1);
    assert(mult(rep_nums.begin(), rep_nums.begin() + i_idx + 1) == NI);
    assert(mult(rep_nums.begin() + k_idx, rep_nums.end()) == NK);
    assert(mult(rep_nums.begin() + i_idx + 1, rep_nums.begin() + k_idx) == NJ);

    return "YES";
  }
  else
  {
    vector<numbers_t> rep_nums;
    for (size_t i = 0; i != 4; ++i)
    {
      rep_nums.insert(rep_nums.end(), nums.begin(), nums.end());
    }

    size_t const i_idx = find_mult_idx(rep_nums.begin(), rep_nums.end(), NI);
    size_t const k_rev_idx = find_mult_idx(rep_nums.rbegin(), rep_nums.rend(), NK, true);
    if (i_idx == rep_nums.size() || k_rev_idx == rep_nums.size())
      return "NO";
    return "YES";
  }

  assert(false);
  return "XXX";
}

int main()
{
  //FILE * res = std::freopen("small.in", "rt", stdin);
  //FILE * res = std::freopen("C-small-attempt0.in", "rt", stdin);
  //FILE * res = std::freopen("C-small-attempt1.in", "rt", stdin);
  FILE * res = std::freopen("C-small-attempt2.in", "rt", stdin);
  //FILE * res = std::freopen("C-large.in", "rt", stdin);
  assert(res);

  size_t T;
  cin >> T;

  for (size_t ci = 1; ci <= T; ++ci)
  {
    size_t L, X;
    cin >> L >> X;
    string S;
    cin >> S;
    assert(S.size() == L);

    vector<numbers_t> nums;
    for (size_t i = 0; i != L; ++i)
    {
      numbers_t const n = numbers_t(S[i] - 'i' + 1);
      nums.push_back(n);
    }

    cout << "Case #" << ci << ": " << solve(nums, X) << "\n";
  }
}
