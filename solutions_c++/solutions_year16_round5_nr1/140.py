#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
#define X first
#define Y second

const int maxn = 20005;
int dp[2][maxn][2];

int tp(char a)
{
	return (a=='C'?0:1);
}
int stupid(string s)
{
	int n = s.size();
	vector<int> c(n);
	for (int i = 0; i < n; i++) c[i] = i;
	int best = 0;
	do {
		bool ok = 1;
		for (int i = 0; i < n; i++)
		   if (c[c[i]] != i || c[i] == i) ok = 0;
		bool pok = ok;
		for (int i = 0; i < n; i++) 
		  for (int j = i+1; j < n; j++)
		     if (c[i] > i && c[j] > j && c[i] > j && c[j] > c[i]) ok = 0;
		//if (pok) for (int i = 0; i < n; i++) cout << c[i] << ' ';
		//if (pok) cout << " --- " << ok << endl;
	    if (ok)
	    {
			int score = 0;
			for (int i = 0; i < n; i++)
			   if (c[i] > i)
			   {
				   score += (s[i] == s[c[i]]? 10 : 5);
			   } 
			best = max(best, score);
		}
	} while (next_permutation(c.begin(), c.end()));
	return best;
}

void solve(int test)
{
	string s;
	cin >> s;
	int n = (int)s.size();
	for (int i = 0; i < 2; i++)
	   for (int j = 0; j <= n; j++)
	      dp[0][j][i] = -(int)1e9;
	dp[0][1][tp(s[0])] = 0;
	for (int i = 1; i < n; i++)
	{
		int q = (i&1)^1;
		for (int j = 0; j <= n; j++)
		   for (int last = 0; last < 2; last++)
			  dp[q^1][j][last] = -(int)1e9;
		for (int j = 0; j <= n; j++)
		   for (int last = 0; last < 2; last++)
		   {
			   if (j == 0) dp[q][j][last] = max(dp[q][j][last], dp[q][j][last^1]);
			   int nxt = tp(s[i]);
			   if (last == nxt && j > 0)
			   {
				   dp[q^1][j-1][last^1] = max(dp[q^1][j-1][last^1], dp[q][j][last] + 1);
			   }
			   else 
			   {
				   dp[q^1][j+1][nxt] = max(dp[q^1][j+1][nxt], dp[q][j][last]);
				   if (j > 0) 
				     dp[q^1][j-1][last^1] = max(dp[q^1][j-1][last^1], dp[q][j][last]);
			   }
		   }
	}
	int ans = (int)((ll)max(dp[(n&1)^1][0][0], dp[(n&1)^1][0][1])*5ll + 5 * (ll)n/2);
	if (n <= 10)
	{
		cerr << "s=" << s << endl;
		cerr << ans << ' ' << stupid(s) << endl;
		 assert(ans == stupid(s));
    }
	cout << "Case #" << test << ": " << (ll)max(dp[(n&1)^1][0][0], dp[(n&1)^1][0][1])*5ll + 5 * (ll)n/2  << "\n";
}





int main()
{
	int tests;
	cin >> tests;
	for (int i = 0; i < tests; i++)
	{
		solve(i+1);
	}
	return 0;
}
