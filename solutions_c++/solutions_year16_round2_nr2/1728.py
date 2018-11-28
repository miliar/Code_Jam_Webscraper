#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <chrono>
#include <numeric>

using namespace std;

typedef ptrdiff_t ist;
typedef size_t iut;
typedef vector<ist> vi;
typedef pair<ist, ist> pii;

bool trailing_space = false; // for output

struct Solver
{
   ist N;
   string s1, s2;
   ist ans1, ans2;
   ist smallest_diff = (1 << 19);

   void read_input()
   {
      cin >> s1 >> s2;
      N = s1.length();
   }

   void get_diff(ist v11, ist v22, ist i)
   {
      if (i == N)
      {
        ist diff = v11 - v22;
        if (diff < 0) diff = -diff;
        if (diff < smallest_diff)
        {
          smallest_diff = diff;
          ans1 = v11;
          ans2 = v22;
        }
        return;
      }
      v11 *= 10;
      v22 *= 10;
      auto c1 = s1[i];
      auto c2 = s2[i];

      ++ i;

      ist v1 = v11;
      ist v2 = v22;

      if (c1 != '?')
      {
        v1 += c1 - '0';
      }
      if (c2 != '?')
      {
        v2 += c2 - '0';
      }

      if (c1 != '?' && c2 != '?')
      {
         get_diff(v1, v2, i);
      }

      if (v11 > v22)
      {
        if (c2 == '?') v2 += 9;
        get_diff(v1, v2, i);
      }
      else if (v11 < v22)
      {
        if (c1 == '?') v1 += 9;
        get_diff(v1, v2, i);
      }
      else
      {
        if (c1 == '?' && c2 == '?')
        {
          get_diff(v1, v2, i);
          get_diff(v1, v2 + 1, i);
          get_diff(v1 + 1, v2, i);
        }
        else if (c1 == '?')
        {
          v1 += c2 - '0';

          if (c2 != '0')
          {
            get_diff(v1 - 1, v2, i);
          }

          get_diff(v1, v2, i);

          if (c2 != '9')
          {
            get_diff(v1 + 1, v2, i);
          }
        }
        else if (c2 == '?')
        {
          v2 += c1 - '0';

          if (c1 != '0')
          {
            get_diff(v1, v2 - 1, i);
          }

          get_diff(v1, v2, i);

          if (c1 != '9')
          {
            get_diff(v1, v2 + 1, i);
          }
        }
      }
   }

   void solve()
   {
     ist smallest_diff = (1 << 19);
     get_diff(0, 0, 0);
   }

   void print_output()
   {
     cout << ' ' << setfill('0') << setw((int)N) << ans1 << ' ' << setw((int)N) << ans2;
   }

   void execute()
   {
      read_input();
      solve();
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

