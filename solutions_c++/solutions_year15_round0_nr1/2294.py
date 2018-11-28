#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
#define vi vector<int>
#define vs vector<string>
#define vl vector<LL>
#define pb push_back
#define endl "\n"


LL solve()
{
   LL Smax;
   cin >> Smax;
   string s;
   cin >> s;

   LL ans = 0;
   LL curr_standing = 0;
   for (auto i = 0; i <= Smax; ++i)
   {
      if (curr_standing < i)
      {
         ans += i - curr_standing;
         curr_standing = i;
      }
      curr_standing += s[i] - '0';
   }

   return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
	   LL ret = solve();
	   cout  << "Case #" << i << ": " << ret << endl;
	}

	return 0;
}
