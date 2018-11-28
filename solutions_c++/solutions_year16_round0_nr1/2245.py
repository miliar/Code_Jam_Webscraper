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

bool trailing_space = true; // for output

struct Solver
{
   ist N;
   ist ans;

   void read_input()
   {
      cin >> N;
   }

   void solve()
   {
      ans = 0;
      int markers[10]={};

      int cnt = 0;

      if (N == 0)
      {
        return;
      }

      while(cnt < 10)
      {
         ans += N;
         for(ist a = ans; a > 0; a /= 10)
         {
           ist d = a % 10;
           if (!markers[d])
           {
             markers[d] = 1;
             ++ cnt;
           }
         }
      }
   }

   void print_output()
   {
      if (ans == 0) cout << "INSOMNIA";
      else cout << ans;
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

