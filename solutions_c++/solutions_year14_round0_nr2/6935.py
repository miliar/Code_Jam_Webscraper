#include <cstdio>
#include <iostream>
#include <iomanip>
#include <iostream>

typedef long double ftype;
using namespace std;

ftype solve()
{
	ftype farmBuild, farmCookies, needCookies;
	cin >> farmBuild >> farmCookies >> needCookies;
	
	ftype now = 2;
	
	ftype answer = 0;
	while (true)
	{
		ftype can = needCookies / now;
		ftype speedup = farmBuild / now + needCookies / (now + farmCookies);
		
		if (speedup < can)
		{
			answer += farmBuild / now;
			now += farmCookies;
		}
		else break;
	}
	answer += needCookies / now;
	return answer;
}

int main()
{
	freopen("bsmall.in", "r", stdin);
	freopen("bsmall.out", "w", stdout);
	
	int nTests;
	scanf("%d", &nTests);
	
	for (int i = 0; i < nTests; i++)
	{
		ftype ans = solve();
		cout << fixed << setprecision(7) << "Case #" << i + 1 << ": " << ans << "\n";
	}
	
	return 0;
}
