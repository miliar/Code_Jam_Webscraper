#include <array>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <list>

using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;
using li = list<int>;
using ll = long long;

#define rep(i, n) for (int i = 0; i < n; i++)
#define repa(i, s, e) for (int i = s; i <= e; i++)
#define repd(i, s, e) for (int i = s; i >= e; i--)

pair<int, int> search_highest(const array<int, 10>& l)
{
  int max = -1;
  int second_max = -1;

  for (int i = 9; i >= 0; i--)
  {
    const auto& v = l[i];
    if (v > 0 && max == -1)
    {
      max = i;
    }
    else if (v > 0 && second_max == -1)
    {
      second_max = i;
    }
  }

  return {max, second_max};
}

void print_array(const array<int, 10>& l)
{
	std::cout << "[";
	for(int i : l)
	{
		std::cout << i;
	}
	std::cout << "]" << std::endl;
}

int solve(const array<int, 10>& l)
{
  queue<pair<array<int, 10>, int>> q;
  q.emplace(l, 0);

  int m, s;
  std::tie(m, s) = search_highest(l);

  int score = m;

  while (!q.empty())
  {
    array<int, 10> target;
    int steps;

    std::tie(target, steps) = q.front();
    q.pop();

    int max_idx, second_max_idx;
    std::tie(max_idx, second_max_idx) = search_highest(target);

    int max_count = target[max_idx];
    int half_up = std::ceil(max_idx / 2.0f);
    int to_move = max_idx - half_up;

	int gain = 0;
	if (second_max_idx == -1)
	{
		gain = to_move;
	}
	else
	{
		gain = (max_idx - second_max_idx);
	}

    if (max_idx <= 2 || gain < max_count || max_count > to_move)
    {
      auto tmp = max_idx + steps;
      if (tmp < score)
      {
        score = tmp;
      }
    }
    else
    {
	  for(int m = max_count; m <= to_move; m++)
	  {
		int next_s = steps;
	    auto copy = target;

		auto v = copy[max_idx];
		copy[max_idx] -= v;

		auto sub = max_idx - m;
		copy[sub] += v;
		copy[m] += v;
		next_s += v;

		q.emplace(copy, next_s);
	  }
    }
  }

  return score;
}

int main()
{
  cin.tie(0);
  ios::sync_with_stdio(false);

  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    int D;
    cin >> D;

    array<int, 10> l;
    l.fill(0);

    for (int j = 0; j < D; j++)
    {
      int pi;
      cin >> pi;

      l[pi]++;
    }

    cout << "Case #" << (i + 1) << ": " << solve(l) << endl;
  }
}
