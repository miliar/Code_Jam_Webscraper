# include <cstdio>
# include <cstring>
# include <iostream>
# define NR 100100
# define REP(i, a, b) for (int i = (a); i <= (b); i ++)
using namespace std;
char s[NR];
inline void Solve ()
{
	scanf  ("%s", s + 1);int n = strlen (s + 1);
	int ans = 0;
	REP (i, 1, n)
	{
		int j = i;
		for( ; s[j + 1] == s[j]; j ++);
		ans ++;
		i = j;
	}
	if (s[n] == '+') ans --;
	cout << ans << endl;
}
int main()
{
	freopen ("FB.in", "r", stdin);
	freopen ("FB.out", "w", stdout);
	int T;cin >> T;
	REP (i, 1, T)
	{
		printf ("Case #%d: ", i);
		Solve ();
	}
	return 0;
}
