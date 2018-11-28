#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

void solve()
{
	int i,renshu,ans,Smax;
	char p;
	
	scanf("%d ",&Smax);
	renshu = 0;
	ans = 0;
	for (i = 0;i<=Smax;i++)
	{
		p = getchar();
		if (renshu<i && p>'0')
		{
			ans += i - renshu;
			renshu = renshu + ans;
		}
		renshu+=p-'0';
	}
	printf("%d\n",ans);
	
}

int main()
{
	int T;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
