#include <cstdio>
#include <iostream>
#include <cstring>
#include <set>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int _, cases = 1;
	cin >> _;
	while (_--)
	{
		int r, v;
		set <int> sRow;
		cin >> r;
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				cin >> v;
				if (i == r) sRow.insert(v);
			}
		}
		int res = -1;
		cin >> r;
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				cin >> v;
				if (i == r && sRow.find(v) != sRow.end())
				{
					if (res < 0) res = v;
					else res = 0;
				}
			}
		}
		printf("Case #%d: ", cases++);
		if (res > 0) printf("%d\n", res);
		else if (!res) puts("Bad magician!");
		else puts("Volunteer cheated!");
	}
	return 0;
}