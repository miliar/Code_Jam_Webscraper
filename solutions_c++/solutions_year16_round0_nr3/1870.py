#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <chrono>
#include <numeric>
#include <cassert>

using namespace std;

typedef ptrdiff_t ist;
typedef size_t iut;
typedef vector<ist> vi;
typedef pair<ist, ist> pii;

bool trailing_space = true; // for output

struct Solver
{
   ist N, J;

   void read_input()
   {
      cin >> N >> J;
   }

   ist get_factor(ist n)
   {
     for(ist i = 2; i * i <= n; ++ i)
     {
       if (n%i == 0) return i;
     }
     return 1;
   }

   ist get_n(const vector<int> & markers, int base)
   {
     ist n = 0;
     for(ist i  = 0; i < N; ++ i)
     {
        n *= base;
        n += markers[i];
     }
     return n;
   }

   void print_output()
   {
      if (N == 32)
      {
        vector<ist> factors(9);

        for(int i = 0; i < 9; ++ i)
        {
          factors[i] = i + 2;
          for(ist j = 0; j < 4; ++ j) factors[i] *= factors[i];
          ++ factors[i];
        }
        
        for(ist i = (1 << 15) + 1; i < (1 << 16) && J > 0; i += 2)
        {
          cout << '\n';
          for(int j = 0; j < 16; ++ j)
          {
            cout << (((1 << j) & i)?1:0);
          }
          for(int j = 0; j < 16; ++ j)
          {
            cout << (((1 << j) & i)?1:0);
          }
          for(ist k = 0; k < 9; ++ k) cout << ' ' << factors[k];
          -- J;
        }
      }

      if (N <= 16)
      {
        for(ist i = (1 << (N-1)) + 1; i < (1 << N) && J > 0; i += 2) 
        {
          ist f2 = get_factor(i);
          if (f2 == 1) continue;
          vector<int> markers(N);
          for(ist j = 0; j < N; ++ j)
          {
            if ((1<<j) & i) markers[N-j-1] = 1;
          }
          ist i2 = i;
          vector<ist> fs;
          for(int k = 3; k <= 10; ++ k)
          {
            i2 = get_n(markers, k);
            fs.push_back(get_factor(i2));
            if (fs.back() == 1)
            {
              break;
            }
          }
            if (fs.back() == 1)
            {
              continue;
            }
          cout << '\n';
          cout << i2 << ' ' << f2;
          for(ist k = 3; k <= 10; ++ k)
            cout << ' ' << fs[k-3];
          -- J;
        }
      }
   }

   void execute()
   {
      read_input();
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

