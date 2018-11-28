#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#pragma warning(disable:4996)

using namespace std;
typedef long long ll;


int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   int nTests;
   scanf("%d", &nTests);
   for (int test = 0; test < nTests; ++test)
   {
      ll N;
      scanf("%lld", &N);
      if (N == 0)
      {
         printf("Case #%d: INSOMNIA\n", test + 1);
         continue;
      }

      set<char> usedDigits;
      ll curN = 0;
      while (usedDigits.size() != 10)
      {
         curN += N;
         string s = to_string(curN);
         usedDigits.insert(s.begin(), s.end());
      }
      printf("Case #%d: %lld\n", test + 1, curN);
   }
   return 0;
}