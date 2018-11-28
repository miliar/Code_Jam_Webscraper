#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

void solve_case(int t);

void solve()
{
   int T;
   cin >> T;

   for (int t = 1; t <= T; t++) {
      solve_case(t);
   }
}

int main()
{
//   std::ifstream in("../A-small-attempt0.in");
//   std::ifstream in("../A-sample.in");
   std::ifstream in("../A-large.in");

   std::cin.rdbuf(in.rdbuf());

//   std::ofstream out("../A-sample.out");
//   std::ofstream out("../A-small.out");
   std::ofstream out("../A-large.out");

   std::cout.rdbuf(out.rdbuf());

   solve();
   return 0;
}

void solve_case(int t)
{
   cout << "Case #" << t << ": ";

   std::string line;
   int k;

   cin >> line >> k;

   int counter = 0;

   for (int i = 0; i < line.length() - (k - 1); i++) {
      if (line[i] == '-') {
         for (int j = i; j < i + k; ++j) {
            line[j] = line[j] == '-' ? '+' : '-';
         }
         counter++;
      }
   }

   bool fail = false;

   for (int i = line.length() - (k - 1); i < line.length(); i++) {
      if (line[i] == '-') {
         fail = true;
      }
   }

   if (fail) {
      cout << "IMPOSSIBLE";
   }
   else {
      cout << counter;
   }

   cout << "\n";
}
