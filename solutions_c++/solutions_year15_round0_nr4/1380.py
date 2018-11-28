#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int t, ys;
int x, r, c;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("dataD.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d%d%d",&x,&r,&c);
		if (r > c) swap(r, c);

		bool ans = false;
		if (x == 1)
		{
			ans = true;
		}
		else if (x == 2)
		{
			if (((r * c) & 1) == 0) ans = true;
		}
		else if (x == 3)
		{
			if (r == 2 && c == 3) ans = true;
			if (r == 3 && c == 3) ans = true;
			if (r == 3 && c == 4) ans = true;
		}
		else if (x == 4)
		{
			if (r == 3 && c == 4) ans = true;
			if (r == 4 && c == 4) ans = true;
		}

		printf("Case #%d: %s\n", ++ys, ans?"GABRIEL":"RICHARD");
	}

	return 0;
}