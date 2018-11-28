#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>

typedef long long int lld;

struct cards {
  int when;
  int number;
};
bool operator<(cards const& l, cards const& r)
{ return l.when < r.when; }

lld mod(lld d) { return d%1000002013; }
lld mod_sub(lld a, lld b) { return mod(1000002013+a-b); }

lld distance_cost(int n, int from, int to)
{
  lld x = to - from;
  return mod(x*n - x*(x+1)/2);
}

int main()
{
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cin.exceptions(std::ios_base::failbit | std::ios_base::badbit);
  int testcases = 0; std::cin >> testcases;

  std::vector<cards> in, out, stack;
  in.reserve(1001);
  out.reserve(1001);
  stack.reserve(1001);

  for (int case_nr=1; case_nr<=testcases; ++case_nr) {
    std::cout << "Case #" << case_nr << ": ";

    lld expected_cost = 0;
    lld actual_cost = 0;

    int n, m; std::cin >> n >> m;
    in.clear(); out.clear();
    
    for (int i=0; i<m; ++i) {
      int o, e, p; std::cin >> o >> e >> p;
      in .push_back({o, p});
      out.push_back({e, p});
      expected_cost = mod(expected_cost + p*distance_cost(n, o, e));
    }
    std::sort(in.begin(), in.end());
    std::sort(out.begin(), out.end());

    auto in_it = in.begin(), in_end = in.end();
    auto out_it = out.begin(), out_end = out.end();

    stack.clear();
    for (; out_it != out_end; ++out_it) {
      for (; in_it != in_end && in_it->when <= out_it->when; ++in_it)
        stack.push_back(*in_it);

      int howmany = out_it->number;
      while (howmany > 0) {
        int leaving = std::min(howmany, stack.back().number);
        howmany -= leaving;
        lld dc = distance_cost(n, stack.back().when, out_it->when);
        actual_cost = mod(actual_cost + leaving*dc);
        if (leaving == stack.back().number)
          stack.pop_back();
        else
          stack.back().number -= leaving;
      }
    }

    std::cout << mod_sub(expected_cost, actual_cost) << '\n';
  }
}

/*
 * Local variables:
 * mode:c++
 * compile-command:"rm -f fast-ticket && g++ -g -ggdb3 -O0 -D_GLIBCXX_DEBUG -Wall -Wextra -pedantic -Wno-long-long -std=c++11 ticket.cc -o ticket && for f in *.in; do echo \"--- $f -------------\"; ./ticket <$f; done && g++ -Ofast -fwhole-program -march=native -std=c++11 ticket.cc -o fast-ticket"
 * end:
 */
