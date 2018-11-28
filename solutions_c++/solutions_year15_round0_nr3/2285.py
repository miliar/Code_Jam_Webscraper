#include <algorithm>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <list>
#include <queue>

using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;
using li = list<int>;
using ll = long long;

#define rep(i, n) for (int i = 0; i < n; i++)
#define repa(i, s, e) for (int i = s; i <= e; i++)
#define repd(i, s, e) for (int i = s; i >= e; i--)

enum class Sign
{
  normal_1,
  normal_i,
  normal_j,
  normal_k,
  negative_1,
  negative_i,
  negative_j,
  negative_k,
};

bool is_negative(const Sign& s)
{
  return (s == Sign::negative_1 || s == Sign::negative_i ||
          s == Sign::negative_j || s == Sign::negative_k);
}

std::string sign_str(const Sign& s)
{
  switch (s)
  {
    case Sign::normal_1:
      return "normal_1";
    case Sign::normal_i:
      return "normal_i";
    case Sign::normal_j:
      return "normal_j";
    case Sign::normal_k:
      return "normal_k";
    case Sign::negative_1:
      return "negative_1";
    case Sign::negative_i:
      return "negative_i";
    case Sign::negative_j:
      return "negative_j";
    case Sign::negative_k:
      return "negative_k";
  }
}

Sign normalize(const Sign& s)
{
  if (!is_negative(s))
  {
    return s;
  }
  else
  {
    switch (s)
    {
      case Sign::negative_1:
        return Sign::normal_1;
      case Sign::negative_i:
        return Sign::normal_i;
      case Sign::negative_j:
        return Sign::normal_j;
      case Sign::negative_k:
        return Sign::normal_k;
    }
  }
}

Sign opposite(const Sign& s)
{
  switch (s)
  {
    case Sign::normal_1:
      return Sign::negative_1;
    case Sign::normal_i:
      return Sign::negative_i;
    case Sign::normal_j:
      return Sign::negative_j;
    case Sign::normal_k:
      return Sign::negative_k;
    case Sign::negative_1:
      return Sign::normal_1;
    case Sign::negative_i:
      return Sign::normal_i;
    case Sign::negative_j:
      return Sign::normal_j;
    case Sign::negative_k:
      return Sign::normal_k;
  }
}

Sign multiply(const Sign& left, const Sign& right)
{
  bool will_negative = ((is_negative(left) && !is_negative(right)) ||
                        (!is_negative(left) && is_negative(right)));

  auto l = normalize(left);
  auto r = normalize(right);

  Sign result;

  switch (l)
  {
    case Sign::normal_1:
      switch (r)
      {
        case Sign::normal_1:
          result = Sign::normal_1;
          break;
        case Sign::normal_i:
          result = Sign::normal_i;
          break;
        case Sign::normal_j:
          result = Sign::normal_j;
          break;
        case Sign::normal_k:
          result = Sign::normal_k;
          break;
      }
      break;
    case Sign::normal_i:
      switch (r)
      {
        case Sign::normal_1:
          result = Sign::normal_i;
          break;
        case Sign::normal_i:
          result = Sign::negative_1;
          break;
        case Sign::normal_j:
          result = Sign::normal_k;
          break;
        case Sign::normal_k:
          result = Sign::negative_j;
          break;
      }
      break;
    case Sign::normal_j:
      switch (r)
      {
        case Sign::normal_1:
          result = Sign::normal_j;
          break;
        case Sign::normal_i:
          result = Sign::negative_k;
          break;
        case Sign::normal_j:
          result = Sign::negative_1;
          break;
        case Sign::normal_k:
          result = Sign::normal_i;
          break;
      }
      break;
    case Sign::normal_k:
      switch (r)
      {
        case Sign::normal_1:
          result = Sign::normal_k;
          break;
        case Sign::normal_i:
          result = Sign::normal_j;
          break;
        case Sign::normal_j:
          result = Sign::negative_i;
          break;
        case Sign::normal_k:
          result = Sign::negative_1;
          break;
      }
      break;
  }

  if (will_negative)
  {
    return opposite(result);
  }
  else
  {
    return result;
  }
}

class Searcher
{
public:
  Searcher(const std::string& s, int L)
    : str{s}, repeat_num{L}, end_is{}, start_ks{}
  {
    Sign res = Sign::normal_1;

    for (auto c : s)
    {
      if (c == 'i')
      {
		  res = multiply(res, Sign::normal_i);
      }
      else if (c == 'j')
      {
		res = multiply(res, Sign::normal_j);
      }
      else if (c == 'k')
      {
		res = multiply(res, Sign::normal_k);
      }
    }

	reduced_own = res;
  }

  bool search()
  {
    auto res = this->search_ik();

    if (!res)
    {
      return false;
    }


	for (int i = 0; i < end_is.size(); i++)
	{
		int start_j = end_is[i] + 1;

		auto it = std::find_if(start_ks.begin(), start_ks.end(),
				[start_j](const int& a)->bool
				{
					return a > start_j;
				});

		if(it != start_ks.end())
		{
			int num = *it - start_j;
			if (calc(start_j, num) == Sign::normal_j)
			{
				return true;
			}
		}
	}

    return false;
  }

private:
  std::string str;
  Sign reduced_own;
  int repeat_num;
  std::vector<int> end_is;
  std::vector<int> start_ks;

  enum class Type
  {
    search_i,
    search_j,
    search_k
  };

  bool search_ik()
  {
    if (str.size() * repeat_num < 3)
    {
      return false;
    }

    // search k
    for (int i = 1; i <= (str.size() * repeat_num - 2); i++)
    {
	  int start = (str.size() * repeat_num - i);
	  int num = i;

      if (calc(start, num) == Sign::normal_k)
      {
        start_ks.emplace_back(start);
      }
    }

    if (start_ks.size() == 0)
    {
      return false;
    }

    // search i
    for (int i = 1; i <= (str.size() * repeat_num - 2); i++)
    {
      if (calc(0, i) == Sign::normal_i)
      {
        end_is.emplace_back(i - 1);
      }
    }

    if (end_is.size() == 0)
    {
      return false;
    }

	// sort
	std::sort(end_is.begin(), end_is.end(), std::less<int>());
	std::sort(start_ks.begin(), start_ks.end(), std::less<int>());

    return true;
  }

  Sign calc(int start, int num)
  {
	int local_idx = (start % str.size());
	int remain_num = str.size() - local_idx;

	int idx = start;
    Sign s{Sign::normal_1};

	if (num >= (remain_num + str.size()))
	{
		for (int i = 0; i < remain_num; i++)
		{
			auto c = get_char(idx + i);
			s = multiply(s, c);
		}

		int div = (int)(num - remain_num) / str.size();
		int mod = (num - remain_num) % str.size();

		for (int i = 0; i < div; i++)
		{
			s = multiply(s, reduced_own);
		}

		for (int i = 0; i < mod; i++)
		{
			s = multiply(s, get_char(i));
		}
	}
	else
	{
      for (int i = 0; i < num; i++)
      {
        auto c = get_char(idx + i);
        s = multiply(s, c);
      }
    }

    return s;
  }

  Sign get_char(int idx)
  {
    char c = str[idx % str.size()];
    if (c == 'i')
    {
      return Sign::normal_i;
    }
    else if (c == 'j')
    {
      return Sign::normal_j;
    }
    else if (c == 'k')
    {
      return Sign::normal_k;
    }
  }
};

int main()
{
  cin.tie(0);
  ios::sync_with_stdio(false);

  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    int T;
    int L;
    cin >> T >> L;

    std::string str;
    cin >> str;

    Searcher s{str, L};

    cout << "Case #" << (i + 1) << ": " << (s.search() ? "YES" : "NO") << endl;
  }
}
