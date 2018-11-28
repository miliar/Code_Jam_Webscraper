#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>

using namespace std;

typedef ptrdiff_t ist;
typedef size_t iut;
typedef vector<ist> vi;
typedef pair<ist, ist> pii;

bool trailing_space = true; // for output

vector<string> ss = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

struct Solver
{
   string S;
   string ans;
   vi counts;

   void read_input()
   {
      cin >> S;
   }

   bool try_n(ist n)
   {
      ist max = 1;
      for(ist i = 0; i < n; ++ i) max *= 10;

      vi a[n];
      for(ist j = 0; j < max; ++ j)
      {
         vi counts2 = counts;
         ist j2 = j;
         bool bad = false;
         for(ist i = 0; i < n; ++ i)
         {
            ist k = j2 % 10;
            for(auto c: ss[k])
            {
               if (-- counts2[c - 'A'] < 0)
               {
                  bad = true;
                  break;
               }
            }
            if (bad) break;
            j2 /= 10;
         }
         bool found = true;
         for(auto &v: counts2) if (v) found = false;
         if (found)
         {
            ist j2 = j;
            for(ist i = 0; i < n; ++ i)
            {
               ist k = j2 % 10;
               ans.insert(ans.begin(), (char)('0' + k));
               j2 /= 10;
            }
            return true;
         }
      }
      return false;
   }

   void solve()
   {
      counts.resize(26);
      for(auto & c: S) ++ counts[c-'A'];
      for(ist n = 1; n <= 6; ++ n)
      {
         try_n(n);
      }
   }

   void print_output()
   {
      cout << ans;
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

