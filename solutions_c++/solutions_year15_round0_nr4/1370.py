#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
#define vi vector<int>
#define vs vector<string>
#define vl vector<LL>
#define pb push_back
#define endl "\n"

#define RICHARD "RICHARD"
#define GABRIEL "GABRIEL"

string solve()
{
   LL X,R,C;
   cin >> X >> R >> C;
   if (R > C) swap(R,C);
   // R is smaller now

   if (X > C) return RICHARD;
   if ((R*C) % X != 0) return RICHARD;
   if (X >= 2*R + 1) return RICHARD;
   if (X >= 2*R && R > 1) return RICHARD;
   if (X >= 7) return RICHARD;
   return GABRIEL;
}

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for (int i = 1; i <= T; ++i)
   {
      cout  << "Case #" << i << ": " << solve() << endl;
   }

   return 0;
}
