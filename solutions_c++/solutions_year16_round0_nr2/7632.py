#include <bits/stdc++.h>

using namespace std;

using LL = long long;
using ULL = unsigned long long;
#define vi vector<int>
#define vs vector<string>
#define vl vector<LL>
#define pb push_back
#define endl "\n"

ULL solve(const string& input)
{
   auto sz = input.size();
   assert(sz > 0);
   char curr_state = input[0];
   ULL flips = 0;
   size_t idx = 0;
   while (idx <= (sz - 1))
   {
      if (idx == sz - 1)
      {
         if (curr_state == '+')
         {
         } else
         {
            curr_state = '-';
            flips++;
            idx++;
         }
         break;
      } else if (input[idx] == input[idx + 1])
      {
         idx++;
      } else
      {
         curr_state = input[idx + 1];
         flips++;
         idx++;
      }
   }
   return flips;
}

int main()
{
   ios_base::sync_with_stdio(false);
   ULL T = 0;
   cin >> T;
   for (ULL i = 1; i <= T; ++i)
   {
      string input;
      cin >> input;
      cout << "Case #" << i << ": " << solve(input) << endl;
   }

   return 0;
}
