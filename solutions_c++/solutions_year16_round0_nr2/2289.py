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

map<vi, ist> cache;

struct Solver
{
   string data;
   ist ans;

   void read_input()
   {
      cin >> data;
   }

   void solve()
   {
     ans = 0;

     char prev = 0;

     data.append(1, '+');

     for(auto c: data)
     {
       if (c != prev)
       {
         prev = c;
         ++ ans;
       }
     }

     -- ans;
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

