#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int T, n;
map<int, int> m, d;

void div(int x)
{
	while (x)
	{
		d[x % 10] = 1;
		x /= 10;
	}
}

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);
	scanf("%d", &T);
	for (int cse = 1; cse <= T; cse++)
	{
		m.clear();
		d.clear();
		scanf("%d", &n);
		int x = n;
		bool ans = 0;
		while (m[x] != 1)
		{
			m[n] = 1;
			div(x);
			if (d.size() == 10)
			{
				ans = 1;
				break;
			}
			x += n;
		}
		if (ans)
			printf("Case #%d: %d\n", cse, x);
		else
			printf("Case #%d: INSOMNIA\n", cse);
	}
	return 0;
}

