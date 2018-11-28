#include <bits/stdc++.h>
using namespace std;
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)

int main()
{
	int T; cin >> T;
	f(_, 1, T)
	{
		string s; int k;
		cin >> s >> k;
		int i, ans = 0;
		for(i = 0; i + k <= (int) s.length(); ++i)
			if(s[i] == '-')
			{
				++ans;
				g(j, i, i + k)
					s[j] = '-' + '+' - s[j];
			}
		bool ok = true;
		for(; i < (int) s.length(); ++i)
			if(s[i] == '-')
				ok = false;
		if(ok)
			printf("Case #%d: %d\n", _, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", _);
	}
	return 0;
}
