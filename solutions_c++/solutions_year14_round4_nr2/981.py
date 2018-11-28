#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <chrono>
#include <cassert>

using namespace std;

typedef ptrdiff_t ist;
typedef size_t iut;
typedef vector<ist> vi;
typedef pair<ist, ist> pii;

bool trailing_space = true; // for output

struct Solver
{
   ist N;
   vi as;
   ist ans;

   void read_input()
   {
      cin >> N;
      as.resize(N);
      for (auto &a : as) cin >> a;
   }

   ist solve(ist i,  vi::iterator max_i)
   {
      ist s = 0;
      if (max_i > as.begin() + i)
      {
         rotate(as.begin() + i, max_i, max_i + 1);
         s += max_i - as.begin() - i;
      }
      else if (max_i < as.begin() + i)
      {
         rotate(max_i, max_i + 1, as.begin() + i + 1);
         s += i - (max_i - as.begin());
      }

      for (ist j = 0; j < i; ++j)
      for (ist k = j + 1; k < i; ++ k)
      {
         if (as[k] < as[j]) ++s;
      }

      for (ist j = i + 1; j < N; ++j)
      for (ist k = j + 1; k < N; ++k)
      {
         if (as[k] > as[j]) ++s;
      }

      if (max_i > as.begin() + i)
      {
         rotate(as.begin() + i, as.begin() + i + 1, max_i + 1);
      }
      else if (max_i < as.begin() + i)
      {
         rotate(max_i, as.begin() + i, as.begin() + i + 1);
      }

      return s;
   }

   void solve()
   {
#if 0
      auto max_i = max_element(as.begin(), as.end());

      ans = solve(0, max_i);

      vi as2 = as;

      for (ist i = 1; i < N; ++i)
      {
         auto ans2 = solve(i, max_i);
         assert(as2 == as);
         if (ans2 < ans) ans = ans2;
      }
#endif

      ans = 0;
      while (as.size() > 2)
      {
         auto min_i = min_element(as.begin(), as.end());
         ans += std::min(min_i - as.begin(), as.end() - min_i - 1);
         as.erase(min_i);
      }
   }

   void print_output()
   {
      cout << ans;
   }

   void execute()
   {
      read_input();
      chrono::time_point<chrono::high_resolution_clock> start = chrono::high_resolution_clock::now();
      solve();
      chrono::time_point<chrono::high_resolution_clock> finish = chrono::high_resolution_clock::now();
      cerr << "PERF: size: " << N << " time: " << chrono::duration_cast<chrono::microseconds>(finish - start).count() << " us\n";
      print_output();
   }
};


int main()
{
   int T = 0;
   cin >> T;
   for (int i = 0; i < T; ++ i)
   {
      cerr << "Solving Case #" << i + 1 << '\n';
      cout << "Case #" << i + 1 << ':';
      if (trailing_space) cout << ' ';
      Solver s;
      s.execute();
      cout << '\n';
   }

   return 0;
}

